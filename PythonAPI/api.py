# -*- coding: utf-8 -*-

import tornado.web
import json
from image import b64Str_to_imgFile
from lib import random_str
from img_pkg_editor import Editor
from py_utility import system
import os
from config import http_config
import copy
import queue



class ApiHandle(tornado.web.RequestHandler):

    def post(self):
        byte_data = self.request.body
        raw_data = byte_data.decode(encoding="utf-8")

        pkg_obj = json.loads(raw_data)
        # pkg_obj = {"error": 0, "img_result": ["123", "234"]}
        # res = json.dumps(pkg_obj)

        trash_queue = queue.Queue()

        for item in pkg_obj["data"]:
            b64_str = item["b64"]

            f_name = random_str(6) + r"." + http_config.img_suffix
            relative_pth = os.path.join(http_config.img_folder, f_name)
            img_pth = system.create_abs_path(relative_pth)
            b64Str_to_imgFile(b64_str, img_pth)

            item["img_pth"] = img_pth

            trash_queue.put(img_pth)
            #  Put img_pth into queue for later clean up

        pkg_rep = copy.deepcopy(pkg_obj)
        editor = Editor()
        # short socket connection
        # TODO: Change short connection to long connection
        res_obj = editor.edit(pkg_rep)

        res = json.dumps(res_obj)

        """ File Clean Up  """
        try:
            while not trash_queue.empty():
                os.remove(trash_queue.get())
        except Exception:
            print("Queue Operation Error")

        self.write(res)

