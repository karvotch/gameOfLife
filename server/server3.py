#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import json


playerCount = 0
count = 0
playerColors = ["lime", "red", "yellow", "blue", "purple", "orange"]
dataJSON = {}

#isReceivedData = False

async def server(websocket, path):
    global playerCount
    global playerColors

    playerColor = f'{{"color": "{playerColors[playerCount]}", "playerID": "{playerCount}"}}'
    playerCount += 1

    await websocket.send(playerColor)

    while True:
        global dataJSON
        global isReceiveData

        #print(type(websocket.recv()))
        #data = await websocket.recv()
        #data = websocket.recv()
        #receiveData = asyncio.create_task(websocket.recv())
        #data = await receiveData
        receiveData = asyncio.create_task(receivingData(websocket))
        #data = await receiveData
        await receiveData
        sendData = asyncio.create_task(sendingData(websocket))
        await sendData

        #if(len(dataJSON) > 0):
        #    await websocket.send(json.dumps(dataJSON, separators=(',', ':')))

        #if(type(data) == type(" ")):
        #    data = json.loads(data)
        #    addToJSON(data)


async def receivingData(websocket):
    global playerCount
    global count
    #global isReceiveData
    data = await websocket.recv()
    #isReceiveData = True
    data = json.loads(data)
    addToJSON(data)
    #count += 1
    #return data


async def sendingData(websocket):
    global isReceiveData
    global dataJSON
    global count
    global playerCount
    #while not isReceiveData:
    while True:
        if(len(dataJSON) > 0):
            if(count <= 0):
                count = playerCount
            await websocket.send(json.dumps(dataJSON, separators=(',', ':')))
            count -= 1
            if(count <= 0):
                clearSendData()


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
