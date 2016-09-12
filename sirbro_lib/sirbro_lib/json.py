import inspect 
import simplejson as json
from pprint import pprint




class jsonUtil(object):

    def __init__(self):
        pass

    def dump_json(self, obj, **param):
        return json.dumps(obj, param)

    def dict_to_bytes(the_dict):
        return json.dumps(the_dict).encode()

    def readJson(self, file):

        with open(file) as data_file:
                json_data = json.load(data_file)

        return json_data

    def printJson(self, json_data):
        pprint(json_data)

    def props(self, obj, depth=0):
        depth += 1
        pr = {}
        for name in dir(obj):
            try:
                value = getattr(obj, name)
                if not name.startswith('__') and not inspect.ismethod(value) and not callable(value):
                    print(name)
                    pr[name] = value
                    if value.__repr__().startswith('<') and depth < 5:
                        pr[name] = props(value, depth=depth)
            except Exception as err:
                print(err)
                continue

        return pr

