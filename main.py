from sanic import Sanic
from sanic.response import json
from datetime import datetime
from inspect import isawaitable

from config import HOST, PORT
from utls import get_data


app = Sanic("test_project")


def middleware(func):
    async def wrapper(request, *args):
        response = func(request, *args)
        if isawaitable(response):
            response = await response
        response.headers['date'] = datetime.today().isoformat()
        return response
    return wrapper


@app.route("/")
@middleware
async def test(request):
    data = get_data()
    return json(data)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
