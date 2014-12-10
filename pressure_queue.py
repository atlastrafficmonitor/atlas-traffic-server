import datetime

class PressureQueue:
    def __init__(self):
        self.readings = []

    def ready_for_event_creation(self):
        return len(self.readings) == 2

    def should_be_refreshed(self):
        return _is_time_expired() and _is_odd_amt_of_readings

    def _refresh_queue(self):
        self.readings = []

        return true

    def _is_time_expired(self, event_time):
        return event_time - datetime.timedelta(seconds=5)

    def _is_odd_amt_of_readings(self):
        length = len(self.readings)

        return length > 0 and length != 2
