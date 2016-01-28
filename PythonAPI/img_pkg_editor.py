# -*- coding: utf-8 -*-

from img_handler_lib import img_handler
from img_handler_lib import Actor
from tensorflow_lib.__init__ import tf_handler
from py_utility import system


def tf_ref(img_pth):
    kws = {"website", "web site", "internet site", "site"}
    timer = system.RunningTimer()
    tf_result = tf_handler.tf_inference(img_pth)
    time_elapsed = timer.end()
    print("TF Time Consumed:"+ time_elapsed.__str__())
    print("TF result:"+tf_result.__str__())

    is_chart = False

    for item in tf_result:
        label = item["label"]
        for kw in kws:
            if kw in label:
                is_chart = True
                return is_chart
            else:
                pass

    # classify all images with tensorflow labelling "website" as chart images
    return is_chart


class Editor(object):
    def __init__(self):
        self.handler = img_handler(Actor)

    def sort(self, tmp_obj):
        return sorted(tmp_obj, key=lambda obj: obj["score"], reverse=True)
        # Guarrantied: the order of original images where scores are equal

    def edit(self, pkg_rep):
        return_error = None
        tmp_obj = list()
        for item in pkg_rep["data"]:
            id = item["id"]
            img_pth = item["img_pth"]

            try:
                score, error = self.handler.proc(img_pth)
            except:
                return_error = -2

            if error == 0:
                if score >= 0:
                    try:
                        is_chart = tf_ref(img_pth)
                        chart_punishment = 0.5 if is_chart else 0
                        score -= chart_punishment
                    except Exception:
                        print("Tensorflow Image Reading Exception Happened")
                    print("score: " + score.__str__())
                    tmp_obj.append({"id": id, "score": score})
                else:
                    pass
                    # dump all unqualified images
                return_error = error
            else:
                return_error = error
                # expecting -1, indicting image read failed

        sorted_obj = self.sort(tmp_obj)
        sorted_id = [item["id"] for item in sorted_obj]
        return_pkg = {"error": return_error, "img_result": sorted_id}

        """
           :return code spec:
                0 => No Error
               -1 => Read Image Failed
               -2 => Server End Error
        """

        self.handler.close()

        return return_pkg

