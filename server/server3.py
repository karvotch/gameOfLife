#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import json


playerCount = 0
count = 0
playerColors = ["green", "red", "yellow", "blue", "purple", "orange"]
dataArray = []

async def data(websocket, path):
    global playerCount
    global playerColors

    playerCount += 1
    playerColor = f'{{"color": "{playerColors[playerCount-1]}", "playerCount": "{playerCount}"}}'

    await websocket.send(playerColor)

    while True:
        data = await websocket.recv()
        #data = json.loads(data)
        #addToJSON(data)

        print(data)

        #json.dumps(jsonArray, separators=(',', ':'), data)

        #await websocket.send(data)
        #await websocket.send(jsonArray)
        await websocket.send(dataArray)

        addToArray(data)

def addToArray(data):
    dataArray.append(data)

start_server = websockets.serve(data, "192.168.1.18", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
