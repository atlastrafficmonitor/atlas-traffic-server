import asyncio
import datetime
import json
import signal
import sys
import time
import websockets

from event import Event

@asyncio.coroutine
def handler(websocket, path):
    while True:
        if not websocket.open:
            break

        event = Event("exit", 10)

        yield from websocket.send(json.dumps(event.serialize()))
        yield from asyncio.sleep(1.0)

        event.mongoify()

@asyncio.coroutine
def pressure_data_handler():
    while True:
        print('Hello')
        yield from asyncio.sleep(1.0)

def boot_server(host, port):
    print('Atlas server is listening on http://', host, ':', port, sep='')

    return websockets.serve(handler, host, port)

def main():
    server = boot_server('0.0.0.0', 8765)
    event_loop = asyncio.get_event_loop()

    tasks = [
            server,
            asyncio.async(pressure_data_handler())
            ]

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
