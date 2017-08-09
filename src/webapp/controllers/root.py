from sanic.response import json as json_response


async def hello_world(request):
    return json_response({"hello": "world"})
