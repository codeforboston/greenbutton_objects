from typing import Any, List, TypeVar

import greenbutton_objects.objects as ob
from greenbutton_objects.atom import EntryForest
from greenbutton_objects.data import espi
from greenbutton_objects.util import get_first, get_value

T = TypeVar("T")


class ObjectFeed:
    def __init__(self) -> None:
        self.usage_points: List[ob.UsagePoint] = []

    def build(self, entry_forest: EntryForest) -> "ObjectFeed":
        usage_points = EntryForest.get_elements_by_type(espi.UsagePoint, entry_forest.roots)

        for up_node in usage_points:
            # TODO: We are assuming that there is only one UsagePoint object
            #       within the usage point node
            up = up_node.first_content()

            local_time_params = up_node.safe_get_content(espi.LocalTimeParameters)
            electric_power_usage_summary = up_node.safe_get_content(espi.ElectricPowerUsageSummary)

            meter_readings: List[ob.MeterReading] = []
            for mr_node in up_node.get_related_of_type(espi.MeterReading):
                reading_type: espi.ReadingType | None = mr_node.safe_get_content(espi.ReadingType)

                interval_block_nodes = mr_node.get_related_of_type(espi.IntervalBlock)
                interval_blocks: List[ob.IntervalBlock] = []

                combined_readings: List[ob.IntervalReading] = []
                for interval_block_node in interval_block_nodes:
                    interval_block_content = get_first(interval_block_node.content)

                    for interval_block in interval_block_content.content:  # type: ignore
                        block = ob.IntervalBlock(
                            uri=interval_block_node.uri, interval=interval_block.interval
                        )

                        self.process_readings(block, interval_block)
                        interval_blocks.append(block)
                        combined_readings.extend(block.readings)

                reading = ob.MeterReading(
                    title=mr_node.title,
                    uri=mr_node.uri,
                    reading_type=reading_type if reading_type else espi.ReadingType(),
                    intervalBlock=tuple(interval_blocks),
                    readings=tuple(combined_readings),
                )

                for ib in reading.intervalBlock:
                    ib.compute_multiplier(reading.reading_type)
                reading.patch()

                meter_readings.append(reading)

            service_kind = up.service_category.kind
            if service_kind == "" or service_kind is None:
                # TODO: We are forcing natural gas here. But we should either use
                #       hint given to us, apply heuristic rules or throw error
                service_kind = ob.ServiceKind.GAS
                for mr in meter_readings:
                    mr.reading_type.uom = ob.UnitSymbol.THERM.value
                    mr.reading_type.power_of_ten_multiplier = espi.UnitMultiplierKindValue.VALUE_MINUS_3
                    for ib in mr.intervalBlock:
                        ib.compute_multiplier(mr.reading_type)

            else:
                service_kind = ob.ServiceKind(service_kind.value)

            self.usage_points.append(
                ob.UsagePoint(
                    title=up_node.title,
                    service_kind=service_kind,
                    local_time_parameters=local_time_params,
                    electric_power_usage_summary=electric_power_usage_summary,
                    meter_readings=tuple(meter_readings),
                    uri=up_node.uri,
                )
            )

        return self

    def process_readings(self, block: ob.IntervalBlock, interval_block: espi.IntervalBlock) -> None:
        # TODO: If quality of reading is not in readings it might be in the
        #       top level description
        readings = []
        for interval_reading in interval_block.interval_reading:
            reading_values = self.filter_allowed(interval_reading)
            if interval_reading.reading_quality:
                quality = interval_reading.reading_quality[0].quality
                quality_of_reading = get_value(
                    quality,
                    missing_val=ob.QualityOfReading.MISSING,
                    src_type=espi.QualityOfReadingValue,
                    dest_type=ob.QualityOfReading,
                )
                reading_values["quality_of_reading"] = quality_of_reading
            reading_values["raw_value"] = interval_reading.value
            readings.append(ob.IntervalReading(**reading_values, parent=block))
        block.readings = readings

    allowed_reading_keys = ("consumption_tier", "cost", "cpp", "time_period", "tou")

    def filter_allowed(self, interval_reading: espi.IntervalReading) -> dict[str, Any]:
        reading_values = {}
        for k, v in interval_reading.__dict__.items():
            if k in self.allowed_reading_keys and v is not None:
                reading_values[k] = v
        return reading_values
