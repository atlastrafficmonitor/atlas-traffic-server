import datetime
from reading import Reading


# PressureQueue
# =============

# A PressureQueue is the data structure that stores data readings from an
# Arduino. It is use as a mechanism to keep tabs on the Reading events that
# have happened. Reading events are not deterministic, and are subject to
# noise, and misreadings. For example, if someone enters the building and
# only one footstep is read from the pressure sensors. We cannot tell if the
# person was exiting or entering the building at that point, so we randomly
# choose one under the assumption that if someone enters the room, they will
# eventually leave.


class PressureQueue:
    def __init__(self):
        self.readings = []

    def ready_for_event_creation(self):
        if self._should_be_refreshed():
            sensor_location = random.sample(['back', 'front'], 1)
            pressure_reading = random.randint(10, 100)
            now = datetime.datetime.now()
            dummy_reading = Reading(sensor_location, pressure_reading, now)
            self.readings.append(dummy_reading)

        return len(self.readings) == 2

    def append(self, item):
        return self.readings.append(item)

    def _should_be_refreshed(self):
        return _is_odd_amt_of_readings() and _is_time_expired()

    def _refresh_queue(self):
        self.readings = []

        return true

    def _is_time_expired(self):
        five_secs_ago = datetime.datetime.now() - datetime.timedelta(seconds=5)

        return self.readings[0].time > five_secs_ago

    def _is_odd_amt_of_readings(self):
        length = len(self.readings)

        return length != 2 and length > 0
