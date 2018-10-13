from flask import Flask, request, jsonify
from pprint import pprint
from handle_messages import handle_add_user, handle_add_song
from state import state

print(state)

app = Flask(__name__)

@app.route('/create-room', methods=['POST'])
def create_room(auth_key):
    state["next_room_id"] += 1
    state["rooms"][str(state["next_room_id"] )] = {"phone-numbers": [], "access_token": auth_key }
    return "create_room"


@app.route('/nexmo', methods=['GET', 'POST'])
def delivery_receipt():
    if 'add_user':
        handle_add_user()

    if 'add_song':
        handle_add_song()

    return None

app.run(port=3000, host="127.0.0.1")
