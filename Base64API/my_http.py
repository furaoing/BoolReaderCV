# -*- coding: utf-8 -*-

import tornado.httpserver, tornado.ioloop, tornado.options, tornado.web, os.path, random, string
from tornado.options import define, options
from api import ApiHandle
import os
import logging
import time

import sys

define("port", default=8080, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/Base64API", ApiHandle)
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

    # Script Initialization Start

    """
    pid = os.getpid()
    with open("upload.pid", "w") as f:
        f.write(str(pid))
    """

    # Script Initialization End

    main()
