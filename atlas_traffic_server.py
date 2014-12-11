import asyncio
import datetime
import json
import signal
import sys
import time
import websockets
import os
import RPi.GPIO as GPIO

from event import Event


# Main asynchronous routines for data acquisition and dispersion.
# ===============================================================


@asyncio.coroutine
def handler(websocket, path):
    while True:
        if not websocket.open:
            break

        for queue in pressure_queues:
            if queue.ready_for_event_creation():
                event = Event(queue.readings)
                serialized_event = json.dumps(event.serialize())

                yield from websocket.send(serialized_event)

                event.mongoify()


@asyncio.coroutine
def pressure_data_handler(location, pin):
    GPIO.setup(pin, GPIO.IN)

    while True:
        if GPIO.input(pin) == 1:
            print(location)
            yield from asyncio.sleep(1.0)


# ===============================================================


def boot_server(host, port):
    print('Atlas server is listening on http://', host, ':', port, sep='')

    return websockets.serve(handler, host, port)

def init_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

def main():
    init_gpio()
    server = boot_server('0.0.0.0', 8765)
    event_loop = asyncio.get_event_loop()
    tasks = [
            server,
            asyncio.async(pressure_data_handler("front_door", 35))]

    try:
        event_loop.run_until_complete(asyncio.wait(tasks))
        event_loop.run_forever()
    except KeyboardInterrupt:
        print('\nCtrl-C (SIGINT) caught. Exiting...')
    finally:
        server.close()
        event_loop.close()

if __name__ == "__main__":
    main()
