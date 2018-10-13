from flask import Flask, request, jsonify
from pprint import pprint
from handle_messages import handle_add_user, handle_add_song, send_text
from spotify import spotify_queuer
import re
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from state import state
import requests

app = Flask(__name__)
rooms = state["rooms"]



@app.route('/create-room', methods=['POST','OPTIONS'])
@cross_origin()
def create_room():
    print("recieved a request")
    if request.is_json:
        json = request.get_json() #accept spotify access token
        print(json)
        username
        state["next_room_id"] += 1
        state["rooms"][str(state["next_room_id"] )] = {"phone-numbers": [], "access_token": json["access_token"],"username": username, "playlist_id": json["playlist_id"], "spotify_queue": spotify_queuer(json["username"],json["access_token"],json["playlist_id"])} #create a new room with empty phone numbers
        return jsonify({'code': str(state["next_room_id"])})



@app.route('/nexmo', methods=['GET', 'POST','OPTIONS'])
@cross_origin()
def delivery_receipt():
    print("recieved a request")
    if request.is_json:
        pprint(request.get_json())
        text_message = request.get_json['text']
        sender = request.get_json['msisdn'] #sender phone number
        if text_message[:4] == "join":
            room_number = str(re.search(r"join (\d+)",text_message).group(1)) #extract room number to join from text message
            if room_number is None:
                send_text("room does not exist", sender)
            else:
                handle_add_user(sender, room_number)
        elif text_message[:3] == "add":
            song_query = re.search(r"^add (.+)$" , text_message).group(1) #extract song to add to playlsist from text message
            handle_add_song(song_query)


    else:
        data = dict(request.form) or dict(request.args)
        pprint(data)

    return None




app.run(port=3000, host="127.0.0.1")
