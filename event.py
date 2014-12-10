import random
import statistics
import time

from pymongo import MongoClient

# Event
# ----
#
# An event is the abstract interface for an event containing the information
# necessary for the visual system. It has methods to deal with serializing the
# data into a consumable format by the client, and logic for saving the events
# to a persistent data store (MongoDB). It is important to note than an Event,
# as described by the interface, consists of two data readings from an Arduino.


client = MongoClient('atlas-installation.ianks.com', 27017)
db = client.atlas_traffic_monitor
collection = db.event


class Event:
    def __init__(self, readings):
        self.event_type = self._determine_event_type_from_readings(readings)
        self.pressure_reading_avg = self._pressure_reading_avg(readings)
        self.gmtime = time.time()
        self.strftime = time.strftime("%I:%M")
        self.readings = [r.serialize() for r in readings]

    def serialize(self):
        return {
            "eventType" : self.event_type,
            "gmtime" : self.gmtime,
            "pressureReading" : self.pressure_reading,
            "stftime" : self.strftime
        }

    def mongoify(self):
        return collection.insert(self.serialize())

    def _determine_event_type_from_readings(self, readings):
        first = self.readings[0].sensor_location
        second = self.readings[1].sensor_location

        # If the first reading is from a front sensor, that means entry.
        if first  == 'front' and second =='back':
            return 'entry'
        elif first  == 'back' and second == 'front':
            return 'exit'
        else:
            return random.sample(['entry', 'exit'], 1)

    def _pressure_reading_avg(self, readings):
        return mean([r.pressure_amplitude for r in readings])
