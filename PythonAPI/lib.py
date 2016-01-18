# -*- coding: utf-8 -*-

import random
import string


def random_str(length):
    my_str = "".join((random.choice(string.ascii_letters) for i in range(length)))
    return my_str
