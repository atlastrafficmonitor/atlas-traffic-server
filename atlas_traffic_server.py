import asyncio
import datetime
import signal
import sys
import time
import websockets
<<<<<<< Updated upstream
import json
from IPython import embed
from random import randint

i = 0
=======

from event import Event

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

>>>>>>> Stashed changes

@asyncio.coroutine



def handler(websocket, path):
    while True:
        if not websocket.open:
            break

<<<<<<< Updated upstream
        global i
        i = i + .5

        if i == 10:
            i= 0

        yield from websocket.send(json.dumps({
  "totalEntries" : str(1),
  "secondsSinceLastEntry" : "1.25",
  #"timestamp" : time.strftime("%H:%M"),
  "timestamp" : "0" + str(i) + ":00",
  "swarm" : "true"
}))
        yield from asyncio.sleep(1)
=======
        event = Event("exit", 10)

        yield from websocket.send(event.serialize())
        yield from asyncio.sleep(1.0)
>>>>>>> Stashed changes

        event.mongoify()

def boot_server(host, port):
    print('Atlas server is listening on http://', host, ':', port, sep='')

    return websockets.serve(handler, host, port)

def main():
    server = boot_server('0.0.0.0', 3000)
    event_loop = asyncio.get_event_loop()

    try:
        event_loop.run_until_complete(server)
        event_loop.run_forever()
    except KeyboardInterrupt:
        print('\nCtrl-C (SIGINT) caught. Exiting...')
    finally:
        server.close()
        event_loop.close()

if __name__ == "__main__":
    main()
