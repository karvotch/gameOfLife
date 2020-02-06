#!/usr/bin/env python

# WS server example

import asyncio
import websockets

async def hello(websocket, path):
    while True:
        name = await websocket.recv()

        #print(f"< {name}")
        print(name)
        #name = int(name)
        #name += 2
        #name = f"{name}"

        await websocket.send(name)

start_server = websockets.serve(hello, "192.168.1.18", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
