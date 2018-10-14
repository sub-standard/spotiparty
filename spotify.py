import pprint
import sys
import requests as r
from threading import Thread
import time
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
        self.queue = []

    def add_song_to_playlist(self,track_id):
        sp = spotipy.Spotify(auth=self.token)
        scope = 'playlist-modify-public'
        # sp.trace = False
        # i_of_track = -1
        # if len(self.queue) == 0:
        #     self.queue.append([track_id,1])
        #     self.update_queue()
        #     return
        #
        # for index, tracks in enumerate(self.queue):
        #
        #     print("track already in queue")
        #     if tracks[0] == track_id:
        #         tracks[1] = tracks[1] + 1
        #         i_of_track = index
        #         self.queue.sort(key=lambda x: x[1])
        #         self.update_queue()
        #         return "songs position updated"
        #
        # if i_of_track == -1:
        #     print("track wasn't in queue")
        #     self.queue.append([track_id,1])
        sp.user_playlist_add_tracks(self.username,self.playlist_id,[track_id])



    # def update_queue(self):
    #     sp = spotipy.Spotify(auth=self.token)
    #     track_ids = []
    #     if not self.queue:
    #         return
    #     for tuple in self.queue:
    #         track_ids.append(tuple[0])
    #     track_ids.reverse()
    #     sp.user_playlist_replace_tracks(self.username, self.playlist_id, track_ids)
    #
    # #
    # # def next_song(self):
    # #     self.queue = (self.queue[:-1])[:]
    # #     time.sleep(2)
    # #     print(self.queue)
    # #     self.update_queue()


    def skip_track(self):
        devices = r.get("https://api.spotify.com/v1/me/player/devices", headers={"Authorization": "Bearer " + self.token }).json()
        print(devices)
        device_id = devices["devices"][0]["id"]
        r.post("https://api.spotify.com/v1/me/player/next", headers={"Authorization": "Bearer " + self.token})

