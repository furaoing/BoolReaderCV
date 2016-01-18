# -*- coding: utf-8 -*-

import tornado.web
import json
from image import imgFile_to_b64Str
from lib import random_str
import os
import copy


class ApiHandle(tornado.web.RequestHandler):

    def post(self):
        byte_data = self.request.body
        raw_data = byte_data.decode(encoding="utf-8")

        img_pth = raw_data

        res = None

        try:
            with open(img_pth, "rb") as f:
                f.read()
        except:
            res = -1

        if res != -1:
            try:
                res = imgFile_to_b64Str(img_pth)
            except:
                res = -2

        self.write(res)

