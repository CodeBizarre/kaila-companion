from pathlib import Path

from sanic import Blueprint
from sanic.response import HTTPResponse, html

files = {f.name.split(".")[0]: str(f.absolute()) for f in Path("web/").glob("*.html")}

for file, path in files.items():
    with open(path) as f:
        files[file] = f.read()

base = Blueprint("blueprint")
base.static("/static", "web/static")

@base.route("/shutdown_server")
async def shutdown_server(_):
    raise SystemExit

@base.route("/")
async def news(_) -> HTTPResponse:
    return html(files["news"])

@base.route("/books")
async def books(_) -> HTTPResponse:
    return html(files["books"])

@base.route("/characters")
async def characters(_) -> HTTPResponse:
    return html(files["characters"])

@base.route("/notes")
async def notes(_) -> HTTPResponse:
    return html(files["notes"])

@base.route("/storyteller")
async def storyteller(_) -> HTTPResponse:
    return html(files["storyteller"])

@base.route("about")
async def about(_) -> HTTPResponse:
    return html(files["about"])
