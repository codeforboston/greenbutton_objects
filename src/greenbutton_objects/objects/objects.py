from dataclasses import dataclass, field
from datetime import datetime, timedelta
from decimal import Decimal
from typing import List, Optional, Tuple

import greenbutton_objects.data.espi as espi
from greenbutton_objects.objects import UNIT_SYMBOL_DESCRIPTIONS, QualityOfReading, ServiceKind, UnitSymbol
from greenbutton_objects.util import get_value


@dataclass
class DateTimeInterval:
    start: datetime
    duration: timedelta


@dataclass(order=True)
class IntervalReading:
    """Specific value measured by a meter or other asset.

    Each Reading is associated with a specific ReadingType.

    :ivar cost: [correction] Specifies a cost associated with this reading,
        in hundred-thousandths of
        the currency specified in the ReadingType for this reading.
        (e.g., 840 = USD, US dollar)
        NaN means there was no cost received from the feed
    :ivar quality_of_reading: One or more quality of reading values for the
        current interval reading.
    :ivar time_period: The date time and duration of a reading. If not specified,
        readings for each “intervalLength” in ReadingType are present.
    :ivar raw_value: [correction] Value in units specified by ReadingType (not scaled)
    :ivar consumption_tier: [extension] Code for consumption tier associated with reading.
    :ivar tou: [extension] Code for the TOU type of reading.
    :ivar cpp: [extension] Critical peak period (CPP) bucket the reading
        value is attributed to. Value
        0 means not applicable. Even though CPP is usually considered a specialized
        form of time of use 'tou', this attribute is defined explicitly for flexibility.
    :ivar parent: Reference to the parent interval block
    """

    time_period: DateTimeInterval
    raw_value: float

    consumption_tier: Optional[int] = None
    tou: Optional[int] = None
    cpp: int = 0

    parent: Optional["IntervalBlock"] = None
    cost: float = float("NaN")
    quality_of_reading: QualityOfReading = QualityOfReading.MISSING
    reading_type: Optional[espi.ReadingType] = None

    __cached_value: Optional[float] = None

    @property
    def start(self) -> datetime:
        if self.time_period is None:
            return datetime.utcfromtimestamp(0)
        #  The type checking is ignored for the lines below
        #  because these conditions should never happen
        #  unfortunately some providers produce feeds that are not compatible
        #  with the defined XSD schema
        if type(self.time_period.start) is str:  # type: ignore
            time_start = datetime.utcfromtimestamp(int(Decimal(self.time_period.start)))  # type: ignore
        elif type(self.time_period.start) is int:  # type: ignore
            time_start = datetime.utcfromtimestamp(self.time_period.start)  # type: ignore
        else:
            time_start = self.time_period.start
        return time_start

    @property
    def value(self) -> float:
        if (
            self.__cached_value is None
            and self.reading_type is not None
            and self.parent is not None
            and self.parent.multiplier is not None
        ):
            self.__cached_value = self.raw_value * self.parent.multiplier
        else:
            raise ValueError("Cannot auto scale raw_value. Not enough data")
        return self.__cached_value


@dataclass
class IntervalBlock:
    uri: str
    interval: DateTimeInterval
    readings: List[IntervalReading] = field(default_factory=list)

    multiplier: Optional[float] = None
    reading_power_of_ten: Optional[float] = None

    def compute_multiplier(self, reading_type: espi.ReadingType) -> None:
        reading_power_ten = get_value(
            reading_type.power_of_ten_multiplier,
            src_type=espi.UnitMultiplierKindValue,
            dest_type=espi.UnitMultiplierKindValue,
            missing_val=espi.UnitMultiplierKindValue.VALUE_0,
        )
        self.reading_power_of_ten = reading_power_ten.value
        self.multiplier = 10.0**self.reading_power_of_ten


@dataclass
class MeterReading:
    title: str
    uri: str
    reading_type: espi.ReadingType
    interval_readings: Tuple[IntervalReading, ...] = field(default_factory=tuple)
    intervalBlock: Tuple[IntervalBlock, ...] = field(default_factory=tuple)

    __uom_symbol = None
    __uom_description = None

    def patch(self) -> None:
        for r in self.interval_readings:
            r.reading_type = self.reading_type

    @property
    def uom_symbol(self) -> str:
        if self.__uom_symbol is None:
            self.__set_unit_of_measure()
        return self.__uom_symbol  # type: ignore

    @property
    def uom_description(self) -> str:
        if self.__uom_description is None:
            self.__set_unit_of_measure()
        return self.__uom_description  # type: ignore

    def __set_unit_of_measure(self) -> None:
        uom_value = get_value(
            self.reading_type.uom,
            src_type=espi.UnitSymbolKindValue,
            dest_type=UnitSymbol,
            missing_val=UnitSymbol.MISSING,
        )
        uom_strs = UNIT_SYMBOL_DESCRIPTIONS[uom_value.value].split(",")
        self.__uom_description = uom_strs[0]
        self.__uom_symbol = uom_strs[-1]


@dataclass
class UsagePoint:
    """
    Logical point on a network at which consumption or production is either
    physically measured (e.g., metered) or estimated (e.g., unmetered streetlights).

    :ivar title: The title of the usage point.
    :ivar uri: The URI that identifies this usage point in the atom feed

    :ivar meter_readings: Collected meter readings.
    :ivar service_kind: Type of service (Electricity, Natural Gas, etc.)
    :ivar electric_power_usage_summary: (deprecated) summary of electricity usage
    :ivar local_time_parameters: Timestamp adjustment rules
    :ivar status: Specifies the current status of this usage
          point. Valid values include: 0 = off 1 =on, -1 = unknown


    """

    title: str
    uri: str

    meter_readings: Tuple[MeterReading, ...]
    service_kind: ServiceKind
    electric_power_usage_summary: Optional[espi.ElectricPowerUsageSummary] = None
    local_time_parameters: Optional[espi.TimeConfiguration] = None
    status: int = -1
