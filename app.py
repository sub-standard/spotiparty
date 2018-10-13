import requests
import spotipy

token = "BQDVhemM91QW1DXyFWp65YuwIsEoZLRsD2nmmenkusKznZJwoJ28hQ0JdM0qHBWzNns1ztPbRkzodViZDJYPkYfVIZ-KEqgWYwsgG8jhF2P-LGO4LD_fCPCFzffX5djVaWNihsKczrEw2pK4qpdCyLGtuJJvXjJuMZU0UtSo7AZU1BEDwUs"

spotify = spotipy.Spotify(auth=token)

# req.text = a query string
# if len(req.text) > 1:
#     name = ' '.join(req.text[1:])
# else:
#     name = 'Sample'
name = "adele"
results = spotify.search(name, limit=1)
items = results['tracks']['items'][0]['id']

print (results['tracks']['items'][0])




