from flask import Flask, request, jsonify
from pprint import pprint
from handle_messages import handle_add_user, handle_add_song, send_text
import re
from state import state
app = Flask(__name__)

@app.route('/create-room', methods=['POST'])
def create_room():
    print("recieved a request")
    if request.is_json:
        key = request.get_json()
        state["next_room_id"] += 1
        state["rooms"][str(state["next_room_id"] )] = {"phone-numbers": [], "access_token": key["auth_key"] }
        return "create_room: " + str(state["next_room_id"])



@app.route('/nexmo', methods=['GET', 'POST'])
def delivery_receipt():
    print("recieved a request")
    if request.is_json:
        pprint(request.get_json())
        text_message = request.get_json['text']
        sender = request.get_json['msisdn']
        if "room" in text_message:
            room_number = re.search(r"join (\d+)",text_message)
            if room_number == None:
                send_text("incorect command", sender)
            else:
                handle_add_user(sender, room_number)
        elif "add" in text_message:
            song_query = re.search(r"add (.+)" , text_message)
            handle_add_song(song_query)

    else:
        data = dict(request.form) or dict(request.args)
        pprint(data)


    return None

app.run(port=3000, host="127.0.0.1")
