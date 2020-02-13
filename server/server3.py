#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import json


playerCount = 0
count = 0
playerColors = ["lime", "red", "yellow", "blue", "purple", "orange"]
dataJSON = {}

async def server(websocket, path):
    global playerCount
    global playerColors

    playerColor = f'{{"color": "{playerColors[playerCount]}", "playerID": "{playerCount}"}}'
    playerCount += 1

    await websocket.send(playerColor)

    while True:
        global dataArray

        #data = await websocket.recv()
        data = websocket.recv()

        print(type(data))
        


        #json.dumps(dataJSON, separators=(',', ':'))

        if(len(dataJSON) > 0):
            await websocket.send(json.dumps(dataJSON, separators=(',', ':')))

        if(type(data) == 'str'):
            data = json.loads(data)
            addToJSON(data)

def addToJSON(data):
    global dataJSON
    if(len(data) > 1):
        dataJSON[data['0']] = data['1']
        print(dataJSON)
        print(len(dataJSON))
    return 0

#start_server = websockets.serve(server, "192.168.1.18", 8000, ping_interval=None)
start_server = websockets.serve(server, "192.168.1.18", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
