import spotipy
import requests

spotify = spotipy.Spotify()
req = requests.get("127.0.0.1", auth=('user'))
print(req.text)


