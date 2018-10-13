from state import state

def handle_add_user(sender, room_number):
    rooms = state['rooms']
    if room_number in rooms:
        room = rooms[room_number]
        room['phone_number'].append(sender)
        send_text(sender, "added to room " + room_number)


def handle_add_song():
    pass



def send_text():
    pass
