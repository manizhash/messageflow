import time
from datetime import datetime

import requests


def print_message(message):
    pass


after = 0

while True:
    response = requests.get(
        "http://127.0.0.1:5000/messages",
        params={"after": after}
    )
    messages = response.json()["messages"]
    for message in messages:
        print_message(message)
        after = message["time"]

    time.sleep(1)
