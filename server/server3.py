#!/usr/bin/env python

# WS server example

import asyncio
import websockets


playerCount = 0
playerColors = ["green", "red", "yellow", "blue", "purple", "orange"]
count = 0

async def hello(websocket, path):
    global count
    global playerCount
    global playerColors
    #playerColor = ["color", playerColors[count]]
    playerColor = f'{{"color": "{playerColors[count]}"}}'


    await websocket.send(playerColor)
    #await websocket.send(playerColor[0])
    #await websocket.send(playerColor[1])
    count += 1
    playerCount += 1
    while True:
        data = await websocket.recv()

        #print(f"< {name}")
        print(data)
        #name = int(name)
        #name += 2
        #name = f"{name}"

        await websocket.send(data)

start_server = websockets.serve(data, "192.168.1.18", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
