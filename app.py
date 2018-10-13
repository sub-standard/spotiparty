import requests
import spotipy

spotify = spotipy.Spotify()
<<<<<<< HEAD

req = requests.get(server, auth=('user',"pass"))
=======
req = requests.get("127.0.0.1", auth=('user'))
>>>>>>> 46c47696fdb2e24779c6b5817b549e3f36810f8f
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




