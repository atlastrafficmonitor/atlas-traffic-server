from pymongo import MongoClient
import time

class Event:
    client = MongoClient('atlas-installation.ianks.com', 27017)
    db = client.atlas_traffic_monitors
    collection = db.event

    def __init__(self, event_type, pressure_reading):
        self.event_type = event_type
        self.gmtime = time.time()
        self.pressure_reading = pressure_reading
        self.strftime = time.strftime("%I:%M")

    def mongoify(self):
        return collection.insert(self.serialize())

    def serialize(self):
        return {
            "eventType" : self.event_type,
            "gmtime" : self.gmtime,
            "pressureReading" : self.pressure_reading,
            "stftime" : self.strftime
        }
