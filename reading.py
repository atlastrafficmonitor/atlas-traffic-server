import datetime


# Reading
# ----
#
# A Reading is the first level of abstraction above the the raw serial data
# recieved from a Raspberry Pi. The constuctor takes the raw text from a serial
# port and constructs a more useful object about it. It includes the location
# of the sensor and the pressure reading from the sensors.


class Reading:
    def __init__(self, raw):
        self.pressure_reading = pressure_reading_from_raw(raw)
        self.location = location_from_raw(location)
        self.time = datetime.datetime.now()

    def pressure_reading_from_raw(raw):
        pass

    def location_from_raw(raw):
        pass
