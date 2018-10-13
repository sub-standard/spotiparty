import requests
import spotipy

spotify = spotipy.Spotify()

req = requests.get(server, auth=('user',"pass"))
print(req.text)


if len(req.text) > 1:
    name = ' '.join(req.text[1:])
else:
    name = 'Sample'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print artist['name'], artist['images'][0]['url']




