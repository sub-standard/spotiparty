import pprint
import sys

import spotipy
import spotipy.util as util

client_id = "2ceb460f532b46ac9e50a3fd7a9db083"
client_secret = "cdf24df5318d4dca90cada78ac3df7aa"
token = "BQDVhemM91QW1DXyFWp65YuwIsEoZLRsD2nmmenkusKznZJwoJ28hQ0JdM0qHBWzNns1ztPbRkzodViZDJYPkYfVIZ-KEqgWYwsgG8jhF2P-LGO4LD_fCPCFzffX5djVaWNihsKczrEw2pK4qpdCyLGtuJJvXjJuMZU0UtSo7AZU1BEDwUs"

class spotify_queuer:
    def __init__(self,username,token, playlist_id):
        self.username = username
        self.token = token
        self.playlist_id = playlist_id
        self.client_id = client_id
        self.client_secret = client_secret

    def add_song_to_playlist(self,track_id,playlist_id,username):
        sp = spotipy.Spotify(auth=self.token)
        sp.
        scope = 'playlist-modify-public'
        sp.trace = False
        results = sp.user_playlist_add_tracks(username, playlist_id, [track_id])
        print(results)

spotify_queuer("jordanmussi",token,)
