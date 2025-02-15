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
MAX_GUESTS = 20
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
        state["rooms"][str(state["next_room_id"] )] = {"skip_song": [],"phone_numbers": [], "access_token": req_json["access_token"],"userid": userid, "playlist_id": req_json["playlist_id"], "spotify_queue": spotify_queuer(userid,req_json["access_token"],req_json["playlist_id"])} #create a new room with empty phone numbers
        print(state)
        return jsonify({'code': str(state["next_room_id"])})



@app.route('/webhooks/nexmo', methods=['GET','POST'])
@cross_origin()
def delivery_receipt():
    text_message = request.get_json()['text'].lower()
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
    elif text_message == "skip":
        handle_skip_song(sender)

    return str(200)

#
# @app.route('/room-guests', methods=['GET'])
# @cross_origin()
# def request_guests():
#     print("recieved a request")
#     if request.get_json() == None:
#         return str(200)
#     room_id = request.get_json()["code"]
#
#     return jsonify({'guests': len(state["rooms"][room_id]["phone_numbers"])})

@app.route('/room-guests/<code>', methods=['GET'])
@cross_origin()
def request_guests(code):
    print("recieved a request")
    print(code)
    if not (code in state["rooms"]):
        return jsonify({'guests': '0'})
    return jsonify({'guests': len(state["rooms"][code]["phone_numbers"])})

#
# @app.route('/next-song/<code>', methods=['GET'])
# @cross_origin()
# def update_next_song(code):
#     print("next song")
#     state['rooms'][code]["spotify_queue"].next_song()
#     return str(200)

def handle_add_user(sender, room_number):
    rooms = state['rooms']
    if room_number not in rooms:
        send_text(sender, "that room does not exist")
    elif len(rooms[room_number]['phone_numbers']) >= MAX_GUESTS:
        send_text(sender, "max guests reached")
    else:
        room = rooms[room_number]
        room['phone_numbers'].append(sender) #adds phone number to that room
        phones[sender] = room_number
        send_text(sender, "added to room " + room_number)


def handle_add_song(song_name,sender):
    if not (sender in phones):
        return
    room = phones[sender]
    print(room)
    token = state["rooms"][room]["access_token"]
    queue = state["rooms"][room]["spotify_queue"]
    song_id = get_track_id(song_name,token)
    if song_id is None:
        send_text(sender, "sorry I cannot find that song")
    else:
        queue.add_song_to_playlist(song_id)

def send_text(sender, text):
    client = nexmo.Client('355a63c2', 'vZQnmEP5A8lZhtYE')
    client.send_message({'from': 'Spotify Player', 'to': sender, 'text': text})



def handle_skip_song(sender):
    if not(sender in phones):
        return
    room = phones[sender]
    phones_in_room = state['rooms'][room]["phone_numbers"]
    token = state['rooms'][room]["access_token"]
    queue = state['rooms'][room]["spotify_queue"]
    skippers = state['rooms'][room]["skip_song"]
    if not(sender in skippers):
        skippers.append(sender)
    if(len(sender) / len(phones_in_room)) > 0.4:
        queue.skip_track()




def handle_leave_room(sender):
    if sender in phones:
        guests = state["rooms"][phones[sender]]["phone_numbers"]
        del guests[sender]
        del phones[sender]
    else:
        send_text("you are not in a room")


app.run(port=3000, host="127.0.0.1")

