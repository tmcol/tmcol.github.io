#!/usr/bin/env python

import asyncio
import websockets
import json

dataDict = {}
dataLock = asyncio.Lock()


class Counter:
  def __init__(self, v):
    self.v = v;
    self.l = asyncio.Lock()
    
  async def getInc(self):
    with (await self.l):
      self.v += 1
      return self.v
      
endpoints = Counter(0)

async def phone(websocket, path):
  print(websocket, path)
  
  device = int(await websocket.recv())
  
  with (await dataLock):
    dataDict[device] = []
    
  ep = await endpoints.getInc()
    
  print("Got device " + str(device) + " at endpoint " + str(ep))
  await websocket.send("Registered")
  
  while 1:
    try:
      resp = await websocket.recv()
      print("Got data from", device)
      
      newData = json.loads(resp);
      with (await dataLock):
        dataDict[device].extend(newData)
        
      print("Set data")
    except websockets.exceptions.ConnectionClosed:
      print("Endpoint closed: ", ep)
      break
      
    
    
async def display(websocket, path):
  print(websocket, path)
  
  
  ep = await endpoints.getInc()
  await websocket.send("You are endpoint: " + str(ep))
  
  while 1:
    request = await websocket.recv()
    device = int(request.split(',')[0])
    index = int(request.split(',')[1])
    
    print("Display requesting: ", device, index)
    
    with (await dataLock):
      response = dataDict[device][index:]
    await websocket.send(json.dumps(response))
    
    print("Sent to display");
    

async def command(websocket, path):
  while 1:
    request = await websocket.recv()
    
    r, d = request.split(',')
    
    with (await dataLock):
      if r == "clearall":
        dataDict = {}
      if r == "clear":
        dataDict[int(d)] = []


async def hello(websocket, path):
  print("new device")
  name = await websocket.recv()
    
  if name == "phone":
    await websocket.send("What is your ID?")
    await phone(websocket, path)
    
  elif name == "display":
    await websocket.send("Ready to send")
    await display(websocket, path)
    
  else:
    await websocket.send("Issue command")
    await command(name)
    
    

start_server = websockets.serve(hello, port = 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()