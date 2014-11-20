import asyncio
import time
import websockets

@asyncio.coroutine
def handler(websocket, path):
    while(True):
        greeting = "handler!"
        yield from websocket.send(greeting)
        time.sleep(1)

start_server = websockets.serve(handler, '0.0.0.0', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
