# -*- coding: utf-8 -*-

from img_handler_lib import img_handler
from img_handler_lib import Actor


class Editor(object):
    def __init__(self):
        self.handler = img_handler(Actor)

    def sort(self, tmp_obj):
        return sorted(tmp_obj, key=lambda obj: obj["score"], reverse=True)
        # TODO: Guarranty the order of original images where scores are equal

    def edit(self, pkg_rep):
        tmp_obj = list()
        for item in pkg_rep["data"]:
            id = item["id"]
            img_pth = item["img_pth"]

            score, error = self.handler.proc(img_pth)
            if score >= 0:
                tmp_obj.append({"id": id, "score": score})
            else:
                pass
                # dump all unqualified images
        sorted_obj = self.sort(tmp_obj)
        sorted_id = [item["id"] for item in sorted_obj]
        return_pkg = {"error": 0, "img_result": sorted_id}

        self.handler.close()

        return return_pkg

