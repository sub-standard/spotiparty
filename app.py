import spotipy
import requests

spotify = spotipy.Spotify()
req = requests.get(server, auth=('user',"pass"))
print(req.text)


