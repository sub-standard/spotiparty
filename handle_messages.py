from state import state, phones
from app import get_track_id
import nexmo


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
    if not (sender in phones):
        return str(200)
    room = phones[sender]
    print(room)
    token = state[room]["access_token"]
    queue = state[room]["spotify_queue"]
    song_id = get_track_id(song_name,token)
    queue.add_song_to_playlist(song_id)


def send_text(sender, text):

    client = nexmo.Client() #Nexmo API key / Secret key
    client.send_message({'from': 'Spotify Player', 'to': sender, 'text': text})

    client = nexmo.Client('355a63c2', 'vZQnmEP5A8lZhtYE')
    client.send_message({'from': 'Spotify Player', 'to': sender, 'text': text})

def handle_skip_song(sender):
    room = phones[sender]
    token = state[room]["access_token"]
    queue = state[room]["spotify_queue"]

