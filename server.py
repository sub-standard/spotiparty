from flask import Flask, request, jsonify
from pprint import pprint
from nexmo import handle_join, handle_add_song

app = Flask(__name__)

@app.route('/create-room', methods=['GET', 'POST'])
def create_room():
    """
    Creates a room in the state
    """
    return None


@app.route('/nexmo', methods=['GET', 'POST'])
def delivery_receipt():
    if 'add_user':
        handle_add_user()

    if 'add_song':
        handle_add_song()

    return None

app.run(port=3000, host="127.0.0.1")


