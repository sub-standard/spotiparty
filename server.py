from flask import Flask, request, jsonify
from pprint import pprint
from handle_messages import handle_add_user, handle_add_song, send_text
from spotify import spotify_queuer
import spotipy
import requests as r
import re
from flask_cors import CORS, cross_origin


from state import state


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
        state["rooms"][str(state["next_room_id"] )] = {"phone-numbers": [], "access_token": req_json["access_token"],"userid": userid, "playlist_id": req_json["playlist_id"], "spotify_queue": spotify_queuer(userid,req_json["access_token"],req_json["playlist_id"])} #create a new room with empty phone numbers
        print(state)
        return jsonify({'code': str(state["next_room_id"])})



@app.route('/webhooks/nexmo', methods=['GET','POST'])
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

    return 200




app.run(port=3000, host="127.0.0.1")
