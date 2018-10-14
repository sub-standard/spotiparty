import pprint
import sys
import requests as r
import spotipy
import spotipy.util as util

with open("client_id.txt", "r") as f:
    client_id = f.read()

with open("client_secret.txt", "r") as f:
    client_secret = f.read()




class spotify_queuer:
    def __init__(self,username,token, playlist_id):
        self.username = username
        self.token = token
        self.playlist_id = playlist_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username

    def add_song_to_playlist(self,track_id):
        sp = spotipy.Spotify(auth=self.token)
        scope = 'playlist-modify-public'
        sp.trace = False
        results = sp.user_playlist_add_tracks(self.username, self.playlist_id, [track_id])
        print(results)

    def skip_track(self):
        devices = r.get("https://api.spotify.com/v1/me/player/devices", headers={"Authorization": "Bearer " + self.token }).json()
        print(devices)
        device_id = devices["devices"][0]["id"]
        r.post("https://api.spotify.com/v1/me/player/next", headers={"Authorization": "Bearer " + self.token})

