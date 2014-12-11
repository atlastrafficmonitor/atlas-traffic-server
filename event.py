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
    def __init__(self):
        self.gmtime = time.time()
        self.strftime = time.strftime("%I:%M")

    def serialize(self):
        return {
            "gmtime" : self.gmtime,
            "stftime" : self.strftime
        }

    def mongoify(self):
        return collection.insert(self.serialize())
