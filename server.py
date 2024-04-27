import time
from datetime import datetime

from flask import Flask, request, abort

app = Flask(__name__)
messages = []


@app.route("/status")
def status():
    dt = datetime.now()
    return {
        "status": True,
        "name": "Mini messenger",
        "time": dt.strftime("%d.%b %H:%M:%S"),
    }


@app.route("/send", methods=["POST"])
def send_message():
    data = request.json
    if not isinstance(data, dict):
        return abort(400)

    name = data.get("name")
    text = data.get("text")

    if not isinstance(name, str) or len(name) == 0:
        return abort(400)

    if not isinstance(text, str) or \
            len(text) == 0 or len(text) > 1000:
        return abort(400)

    message = {
        "name": name,
        "text": text,
        "time": time.time()
    }
    messages.append(message)

    return {"ok": True}


@app.route("/messages")
def get_messages():
    try:
        after = float(request.args["after"])
    except:
        return abort(400)

    response = []
    for message in messages:
        if message["time"] > after:
            response.append(message)
        if len(response)>50:
            response=response[-50:]

    return {"messages": response[:50]}


app.run()
