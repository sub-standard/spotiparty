from flask import Flask, request, jsonify
from pprint import pprint

app = Flask(__name__)

@app.route("/webhooks/inbound-message", methods=['POST'])
def inbound_message():
    data = request.get_json()
    pprint(data)
    return "200"

app.run(port=3000,host="127.0.0.1")