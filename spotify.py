import pprint
import sys

import spotipy
import spotipy.util as util

client_id = "2ceb460f532b46ac9e50a3fd7a9db083"
client_secret = "cdf24df5318d4dca90cada78ac3df7aa"

class spotify_queuer:
    def __init__(self,username,token, playlist_id):
        self.username = username
        self.token = token
        self.playlist_id = playlist_id
        self.client_id = client_id
        self.client_secret = client_secret

    def add_song_to_playlist(self,track_id,playlist_id,username):
        sp = spotipy.Spotify(auth=token)
        scope = 'playlist-modify-public'
        sp.trace = False
        results = sp.user_playlist_add_tracks(username, playlist_id, [track_id])
        print(results)

    def skip_track(self):
        devices = r.get("https://api.spotify.com/v1/me/player/devices", auth = "Authorization: Bearer {" + self.token + "}")
        device_id = devices["devices"][0]["id"]
        sp = spotipy.Spotify(auth=token)
        sp.next_track(device_id)
