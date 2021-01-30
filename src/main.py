import logging
import json
import webview

from sys import platform
from multiprocessing import Process

from app import get_server

with open("config.json") as cfg:
    config = json.load(cfg)

DEBUG = config["debug"]

log = logging.getLogger()
log.setLevel(logging.INFO if DEBUG else logging.WARNING)

def main():
    try:
        server: Process = get_server()
        server.start()

        webview.create_window("Kaila Companion", "http://127.0.0.1:15219")

        if platform == "win32":
            webview.start(debug=DEBUG, gui="cef")
        else:
            webview.start(debug=DEBUG)

        server.terminate()
    except Exception as e:
        log.error(e)

if __name__ == "__main__":
    main()
