from json import dumps, loads
from datetime import datetime
from uuid import uuid4
from requests import get, post


CONVEY_UUID = str(uuid4())
BASE_URL = "https://bhl-counter.herokuapp.com"


def _now():
    return int(datetime.now().timestamp())


def _serialize_out_data(uuid, timestamp):
    out_data_map = {"conveyUUID": uuid, "timestamp": timestamp}
    return dumps(out_data_map)


def _deserialize_in_data(data):
    return loads(data)


def entered():
    enter_data = _serialize_out_data(CONVEY_UUID, _now())
    post(f"{BASE_URL}/enter", enter_data)


def exited():
    exit_data = _serialize_out_data(CONVEY_UUID, _now())
    post(f"{BASE_URL}/exit", exit_data)


def get_stats():
    stats = get(f"{BASE_URL}/stats/{CONVEY_UUID}").content
    return _deserialize_in_data(stats)
