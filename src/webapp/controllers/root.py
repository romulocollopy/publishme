from sanic.response import json


async def hello_world(request):
    return json({"hello": "world"})
