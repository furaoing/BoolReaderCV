# -*- coding: utf-8 -*-


import socket

from config import my_port
from config import my_host
import json


class Actor(object):
    """ define our socket actor """
    def __init__(self, _my_socket):
        self.my_socket = _my_socket

    def score(self, image_pth):
        self.my_socket.send(bytes(image_pth, encoding="utf-8"))
        json_str = self.my_socket.recv(1024).decode(encoding="utf-8")

        result_obj = json.loads(json_str)
        # result is a string object

        score = None
        error = None

        if "error" in result_obj.keys():
            error = result_obj["error"]
            print("Return Code: " + str(error))

        if "score" in result_obj.keys():
            score = result_obj["score"]
            print("Scoring Result: " + str(score))
        return score, error

        # return a float value and a error code


class img_handler(object):

    def __init__(self, _actor):
        self.s = socket.socket()
        # create a socket object
        self.host = my_host
        self.port = my_port
        self.s.connect((self.host, self.port))
        self.my_actor = _actor(self.s)

    def proc(self, image_pth):
        score, error = self.my_actor.score(image_pth)
        return score, error

if __name__ == "__main__":
    image_pth = r"/home/furaoing/roy_tensorflow_cv/face++test_ws/debug_test/5.jpg"

    s = socket.socket()
    # create a socket object
    host = "127.0.0.1"
    port = my_port
    s.connect((host, port))

    my_actor = Actor(s)
    result = my_actor.score(image_pth)
    print(result)
