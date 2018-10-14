import spotipy
import nltk as nl
import Levenshtein_search as lev
import difflib
# token = "BQBlaWxoykhL6HQpm_D1w0yuL62sZvRi_cw5vXH8lTer45zv-ORJ9VeW45AExpUcsEBg6y661VqS6HbdX36S1XBJp9RQV6j6Nh2SCcDYeHNpRcGNSSv1sRkew5LYmaK28Gf4wTDNh5_5Iejux_IGg1LE637rFsd4TYDfpvLXvbD5PVHtM979c2Ts"

def get_track_id(query,token):
    print(query)
    if(query == ""):
        return None
    spotify = spotipy.Spotify(auth=token)
    results = spotify.search("track:" + query, type="track", limit=1)
    if(len(results['tracks']['items']) == 0):
        return get_track_id(query[:-1],token)
    print(results['tracks']['items'][0]['name'])
    return results['tracks']['items'][0]['id']


def get_track_name(query, token):
    if (query == ""):
        return None
    spotify = spotipy.Spotify(auth=token)
    results1 = spotify.search(query, limit=50)
    # print (results1)
    the_song = ""
    max = 0
    if len(results1['tracks']['items']) == 0:
        return get_track_name(query[:-1], token)
    for item in results1['tracks']['items']:
        # print (item['name'])
        word = item['name']
        max1 = difflib.SequenceMatcher(None, word, query).ratio()
        # print(max1)
        if (max1 >= max):
            max = max1
            the_song = word

    return the_song







# print(get_track_name("super massive blak hole", token))



