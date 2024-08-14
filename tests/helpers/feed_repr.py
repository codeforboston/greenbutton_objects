from datetime import timedelta
from math import isnan

from greenbutton_objects import objects as ob
from greenbutton_objects.feed.feed import ObjectFeed


def parse_feed_representation(feed: ObjectFeed) -> str:
    """
    Return a string representation of the test_parse result.

    The representation includes the Usage Points, Meter Readings, and
    Interval Readings.
    """
    result = []

    # Get all usage point containers and elements
    for up in feed.usage_points:
        result.append("UsagePoint (%s) Service: %s (%s) " % (up.title, up.service_kind.name, up.status))

        # Get meter readings containers and elements
        for mr in up.meter_readings:
            result.append("Meter Reading (%s) %s:" % (mr.title, mr.uom_description))
            result.append("\n")

            for interval_reading in mr.interval_readings:
                result.append(
                    "    %s, %s: %g%s"
                    % (
                        interval_reading.start.strftime("%Y-%m-%d %H:%M:%S+00:00"),
                        str(timedelta(seconds=interval_reading.time_period.duration)),  # type: ignore
                        interval_reading.value,
                        mr.uom_symbol,
                    )
                )
                if not isnan(interval_reading.cost):
                    result.append("(%s%s)" % ("$", interval_reading.cost / 100000))
                    # TODO: Hard-coding $ for now as current code does
                    #  not handle currency correctly
                if interval_reading.quality_of_reading != ob.QualityOfReading.MISSING:
                    result.append(" [%s]" % interval_reading.quality_of_reading.name)
                result.append("\n\n")

    return "".join(result)
