import pprint
import sys
import requests as r
import spotipy
import spotipy.util as util

client_id = "2ceb460f532b46ac9e50a3fd7a9db083"
client_secret = "cdf24df5318d4dca90cada78ac3df7aa"
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

token = "BQBvNJRBoNSPlHBuDDmHbY6joAFt7IhcrJKgaCcfR1MSPNrQgHz2jAkiib5-PRwueWIey8RvaKJv5nmjgI003f-7Wb_W7Y27SPaWqP7utdVM8g5fCaDVVcB71N3iHr0oN9_tlyW669hVvU8fVngu7NQ3UU8dFbIS3O9K_WpBOihb3zSu7kM"
# pp = pprint.PrettyPrinter(indent=4)
# # pp.pprint(sp.current_user_playlists())
me = spotify_queuer("jordanmussi",token,"6OdNS5du8uvvQ8JmLhhxHy")
me.skip_track()
