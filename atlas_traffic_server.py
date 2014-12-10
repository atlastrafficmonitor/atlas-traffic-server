import asyncio
import signal
import sys
import time
import websockets
import json
from IPython import embed
from random import randint

i = 0

@asyncio.coroutine



def handler(websocket, path):
    while True:
        if not websocket.open:
            break

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
