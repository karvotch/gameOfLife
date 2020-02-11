#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import json


playerCount = 0
count = 0
playerColors = ["green", "red", "yellow", "blue", "purple", "orange"]
dataArray

async def hello(websocket, path):
    global playerCount
    global playerColors

    playerColor = f'{{"color": "{playerColors[playerCount]}", 
                        "playerCount": "{playerCount}"}}'

    await websocket.send(playerColor)
    playerCount += 1

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

def addToArray(data) {
    dataArray.push(data)
}

start_server = websockets.serve(data, "192.168.1.18", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
