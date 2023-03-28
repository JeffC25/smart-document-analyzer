import asyncio
import aiohttp
import Flask
import json

class Request:
    def __init__(self, url, method, headers=None, payload=None):
        self.url = url
        self.method = method
        self.headers = headers
        self.payload = payload

requests = [
    Request('exampleURL', 'GET'),
    Request('exampleURL', 'POST', 
        headers={'header-info': 'exampleHeader'}, 
        payload={'content': 'exampleContent'})
]

async def processRequest(request):
    async with aiohttp.ClientSession() as session:
        if request.method == 'GET':
            async with session.get(request.url, headers=request.headers) as response:
                response_json = await response.json()
        elif request.method == 'POST':
            async with session.post(request.url, headers=request.headers, json=request.payload) as response:
                response_json = await response.json()

async def main():
    tasks = [process_request(request) for request in requests]
    await asyncio.gather(*tasks)

asyncio.run(main())