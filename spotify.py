import pprint
import sys
import requests as r
import spotipy
import spotipy.util as util

with open("client_id.txt", r) as f):
    client_id = f.read()

with open("client_secret.txt", r) as f):
    client_secret = f.read()

with open("token.txt", r) as f):
    token = f.read()

# token = "BQDVhemM91QW1DXyFWp65YuwIsEoZLRsD2nmmenkusKznZJwoJ28hQ0JdM0qHBWzNns1ztPbRkzodViZDJYPkYfVIZ-KEqgWYwsgG8jhF2P-LGO4LD_fCPCFzffX5djVaWNihsKczrEw2pK4qpdCyLGtuJJvXjJuMZU0UtSo7AZU1BEDwUs"

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
        devices = r.get("https://api.spotify.com/v1/me/player/devices", json={"Authorization":self.token })
        print(devices)
        device_id = devices["devices"][0]["id"]
        sp = spotipy.Spotify(auth=token)
        sp.next_track(device_id)

# pp = pprint.PrettyPrinter(indent=4)
# # pp.pprint(sp.current_user_playlists())
me = spotify_queuer("jordanmussi",token,"6OdNS5du8uvvQ8JmLhhxHy")
me.skip_track()
