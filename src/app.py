import asyncio
import json

from multiprocessing import Process
from hypercorn.config import Config as HypercornConfig
from hypercorn.asyncio import serve as hypercorn_serve
from sanic import Sanic

from blueprint import base

with open("config.json") as cfg:
    config = json.load(cfg)

app = Sanic(name="app")

app.blueprint(base)

hypercorn_config = HypercornConfig()
hypercorn_config.bind = ["127.0.0.1:15219"]

def start_server():
    """
    Run the hypercorn ASGI server.
    """
    asyncio.run(hypercorn_serve(app, hypercorn_config))

def get_server() -> Process:
    """
    Return a multiprocessing.Process that runs the hypercorn ASGI server.
    """
    return Process(target=start_server)
