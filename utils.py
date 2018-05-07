import base64
import json


def encode_list(list_obj):
    return [obj_to_hash(obj) for obj in list_obj]


def decode_list(list_hash):
    return [hash_to_obj(hashed_obj) for hashed_obj in list_hash]


def obj_to_hash(obj):
    json_string = json.dumps(obj)
    return base64.b64encode(str.encode(json_string)).decode("utf-8")


def hash_to_obj(hashed_obj):
    json_string = base64.b64decode(hashed_obj).decode("utf-8")
    return json.loads(json_string)
