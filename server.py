from flask import Flask, request, jsonify
from pprint import pprint
# from handle_messages import handle_add_user, handle_add_song, send_text
from spotify import spotify_queuer
import spotipy
import requests as r
import nexmo
import re
from flask_cors import CORS, cross_origin
from app import get_track_id


# from state import state, phones

state = {"next_room_id": 999, "rooms":{}}

phones = {} #key = phone num, val = phone num

app = Flask(__name__)
rooms = state["rooms"]
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route('/create-room', methods=['POST','OPTIONS'])
@cross_origin()
def create_room():
    print("recieved a request")
    if request.is_json:
        req_json = request.get_json() #accept spotify access token
        print(req_json)
        userid = r.get("https://api.spotify.com/v1/me", headers={"Authorization": "Bearer " + req_json["access_token"]}).json()["id"]
        state["next_room_id"] += 1
        state["rooms"][str(state["next_room_id"] )] = {"phone_numbers": [], "access_token": req_json["access_token"],"userid": userid, "playlist_id": req_json["playlist_id"], "spotify_queue": spotify_queuer(userid,req_json["access_token"],req_json["playlist_id"])} #create a new room with empty phone numbers
        print(state)
        return jsonify({'code': str(state["next_room_id"])})



@app.route('/webhooks/nexmo', methods=['GET','POST'])
@cross_origin()
def delivery_receipt():
    text_message = request.get_json()['text']
    sender = request.get_json()['msisdn'] #sender phone number
    print(text_message)
    if "join" in text_message:
        print("I crash here")
        room_number = str(re.search(r"join (\d+)",text_message).group(1)) #extract room number to join from text message
        if room_number is None:
            send_text("room does not exist", sender)
        else:
            handle_add_user(sender, room_number)
    elif text_message[:3] == "add":
        song_query = re.search(r"^add (.+)$" , text_message).group(1) #extract song to add to playlsist from text message
        handle_add_song(song_query, sender)



    return str(200)

def handle_add_user(sender, room_number):
    rooms = state['rooms']
    if room_number in rooms:
        room = rooms[room_number]
        room['phone_numbers'].append(sender) #adds phone number to that room
        phones[sender] = room_number
        send_text(sender, "added to room " + room_number)
    else:
        send_text(sender, "that room does not exist")


def handle_add_song(song_name,sender):
    print(state)
    room = phones[sender]
    print(room)
    token = state["rooms"][room]["access_token"]
    queue = state["rooms"][room]["spotify_queue"]
    song_id = get_track_id(song_name,token)
    queue.add_song_to_playlist(song_id)

def send_text(sender, text):
    client = nexmo.Client('355a63c2', 'vZQnmEP5A8lZhtYE')
    client.send_message({'from': 'Spotify Player', 'to': sender, 'text': text})

def handle_skip_song(sender):
    room = phones[sender]
    token = state[room]["access_token"]
    queue = state[room]["spotify_queue"]


app.run(port=3000, host="127.0.0.1")

@app.route('/room-guests', methods=['POST'])
@cross_origin
def request_guests():
    print("recieved a request")
    room_id = request.get_json()["code"]
    return jsonify({'guests': len(state["rooms"][room_id]["phone_numbers"])})
