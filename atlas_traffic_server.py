import asyncio
import signal
import sys
import time
import websockets

@asyncio.coroutine
def handler(websocket, path):
    while True:
        yield from websocket.send("Hello!")
        time.sleep(1)

def boot_server(host, port):
    start_server = websockets.serve(handler, host, port)
    asyncio.get_event_loop().run_until_complete(start_server)

    print('Atlas server is listening on http://', host, ':', port, sep='')

def graceful_exit(signum, frame):
    # Clean up event loop
    asyncio.get_event_loop().stop()
    print('\nCtrl-C (sigint) caught. Exiting...')
    exit(1)

def main():
    boot_server('0.0.0.0', 8765)
    signal.signal(signal.SIGINT, graceful_exit)
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()
