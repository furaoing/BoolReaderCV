# -*- coding: utf-8 -*-

import tornado.httpserver, tornado.ioloop, tornado.options, tornado.web, os.path, random, string
from tornado.options import define, options
from api import ApiHandle
import os
import logging
import time
import sys

from config import http_config


def parse_port():
    int_port = None
    if len(sys.argv) > 1:
        _port = sys.argv[1]
        int_port = int(_port)
    else:
        pass
    return int_port


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/ImgAPI", ApiHandle)
        ]
        tornado.web.Application.__init__(self, handlers)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Sorry, this page is intentionally left blank")


def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    port = None

    if parse_port():
        port = parse_port()
    else:
        port = http_config.api_port
        # if no argument given, use default port in config.py
    try:
        define("port", default=port, help="run on the given port", type=int)
    except Exception:
        print("Define Port Not Succeed")
        raise Exception

    # Script Initialization Start

    """
    pid = os.getpid()
    with open("upload.pid", "w") as f:
        f.write(str(pid))
    """

    # Script Initialization End

    main()
