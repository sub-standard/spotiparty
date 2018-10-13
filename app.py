import requests
import spotipy
import pprint
from spotify import spotify_queuer
token = "BQBvNJRBoNSPlHBuDDmHbY6joAFt7IhcrJKgaCcfR1MSPNrQgHz2jAkiib5-PRwueWIey8RvaKJv5nmjgI003f-7Wb_W7Y27SPaWqP7utdVM8g5fCaDVVcB71N3iHr0oN9_tlyW669hVvU8fVngu7NQ3UU8dFbIS3O9K_WpBOihb3zSu7kM"



def get_track_id(query,token):
    spotify = spotipy.Spotify(auth=token)
    results = spotify.search(name, limit=1)
    return results['tracks']['items'][0]['id']





