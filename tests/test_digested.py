from math import isnan

from greenbutton_objects import parse
from greenbutton_objects.data.espi import LocalTimeParameters
from greenbutton_objects.objects import QualityOfReading, ServiceKind
from greenbutton_objects.objects.objects import UsagePoint

from .helpers.feed_repr import parse_feed_representation


def test_electric_containerized(data_dir):
    """
    Very quick test that runs only one of of the files from each source
    """

    data_file = data_dir / "abridged" / "electric_containerized.xml"

    usage_points = parse.parse_feed(str(data_file)).usage_points

    assert type(usage_points[0]) is UsagePoint
    assert len(usage_points) == 1

    up = usage_points[0]
    assert up.title == "Coastal Multi-Family 12hr"
    assert up.service_kind == ServiceKind.ELECTRICITY
    assert "Customer/3/UsagePoint/1" in up.uri

    assert up.electric_power_usage_summary.quality_of_reading.value == QualityOfReading.UNVALIDATED.value

    assert up.local_time_parameters is not None

    lcl_time_params: LocalTimeParameters = up.local_time_parameters
    assert lcl_time_params.dst_offset == 3600
    assert lcl_time_params.tz_offset == -8 * 60 * 60

    mr = up.meter_readings[0]
    assert mr.title == "Hourly Electricity Consumption"
    assert "Point/1/MeterReading/0" in mr.uri
    assert len(mr.intervalBlock) == 2
    assert len(mr.readings) == 8

    assert mr.readings[0].value == 450
    assert isnan(mr.readings[0].cost)
    assert mr.readings[0].quality_of_reading == QualityOfReading.MISSING

    iblock = mr.intervalBlock[0]
    assert len(iblock.readings) == 4

    assert mr.readings[0].parent == iblock


def test_gas_containerized(data_dir):
    """
    Very quick test that runs only one of of the files from each source
    """

    data_file = data_dir / "abridged" / "gas_containerized.xml"

    usage_points = parse.parse_feed(str(data_file)).usage_points

    assert type(usage_points[0]) is UsagePoint
    assert len(usage_points) == 1

    up = usage_points[0]
    assert up.title == "101 DOG ST BOBTOWN MA US 12345-9032"
    assert up.service_kind == ServiceKind.GAS
    assert "User/1111111/UsagePoint/01" in up.uri

    assert up.local_time_parameters is not None

    lcl_time_params: LocalTimeParameters = up.local_time_parameters
    assert lcl_time_params.dst_offset == 3600
    assert lcl_time_params.tz_offset == 5 * 60 * 60

    mr = up.meter_readings[0]
    assert mr.title == ""
    assert "Point/01/MeterReading/01" in mr.uri
    assert len(mr.intervalBlock) == 3
    assert len(mr.readings) == 3

    # Not this is not normalized
    assert mr.readings[0].value == 12.000
    assert mr.readings[0].cost == 2806000
    assert mr.readings[0].quality_of_reading == QualityOfReading.VALIDATED

    iblock = mr.intervalBlock[0]
    assert len(iblock.readings) == 1

    assert mr.readings[0].parent == iblock


def test_gas_direct(data_dir):
    """
    Very quick test that runs only one of of the files from each source
    """

    data_file = data_dir / "abridged" / "gas_direct.xml"

    usage_points = parse.parse_feed(str(data_file)).usage_points

    assert type(usage_points[0]) is UsagePoint
    assert len(usage_points) == 1

    up = usage_points[0]
    assert up.title == "1 MAIN ST, ANYTOWN ME 12345"
    assert up.service_kind == ServiceKind.GAS
    assert "90/UsagePoint/NET_USAGE" in up.uri

    assert up.local_time_parameters is None

    mr = up.meter_readings[0]
    assert mr.title == ""
    assert "Point/NET_USAGE/MeterReading/1" in mr.uri
    assert len(mr.intervalBlock) == 1
    assert len(mr.readings) == 5

    # Not this is not normalized
    assert mr.readings[0].value == 37.000
    assert mr.readings[0].cost == 5100000
    assert mr.readings[0].quality_of_reading == QualityOfReading.MISSING

    iblock = mr.intervalBlock[0]
    assert len(iblock.readings) == 5

    assert mr.readings[0].parent == iblock


def test_gas_direct_pb(data_dir):
    """
    Very quick test that runs only one of of the files from each source
    """

    data_file = data_dir / "natural_gas" / "ngma_gas_provider_2024-07-16.xml"

    atom_forest = parse.parse_feed(str(data_file))
    repr = parse_feed_representation(atom_forest)
    assert (
        repr.split("\n")[3] == "    2024-07-16 18:26:24+00:00, 30 days, 0:00:00: 15 therm($33.06) [VALIDATED]"
    )
