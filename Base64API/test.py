# -*- coding: utf-8 -*-

import json
a = '{"data":[{"id":123, "b64":"7jaXije"},{"id":234, "b64":"7jaXije"},{"id":567, "b64":"7jaXije"}]}'
json_str = json.loads(a)
print(json_str)