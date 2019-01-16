import asyncio
import websockets


async def test():
    async with websockets.connect('ws://youthful-driver.glitch.me/') as websocket:
        await websocket.send("Test WebSocket")

        response = await websocket.recv()
        print(response)


asyncio.get_event_loop().run_until_complete(test())

