import pprint
import sys

import spotipy
import spotipy.util as util


class spotify_queuer:
    def __init__(self,username,token, playlist_id):
        self.username = username
        self.token = token
        self.playlist_id = playlist_id

    def add_song_to_playlist(self,track_id,playlist_id,username):
        scope = 'playlist-modify-public'
        self.token = util.prompt_for_user_token(username, scope)
        sp = spotipy.Spotify(auth=self.token)
        sp.trace = False
        results = sp.user_playlist_add_tracks(username, playlist_id, [track_id])
        print(results)

    def skip_track(self):
        devices = r.get("https://api.spotify.com/v1/me/player/devices", auth = "Authorization: Bearer {" + self.token + "}")
        device_id = devices["devices"][0]["id"]
