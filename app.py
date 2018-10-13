import spotipy
import nltk as nl
# import Levenshtein_search as lev
token = "BQBvNJRBoNSPlHBuDDmHbY6joAFt7IhcrJKgaCcfR1MSPNrQgHz2jAkiib5-PRwueWIey8RvaKJv5nmjgI003f-7Wb_W7Y27SPaWqP7utdVM8g5fCaDVVcB71N3iHr0oN9_tlyW669hVvU8fVngu7NQ3UU8dFbIS3O9K_WpBOihb3zSu7kM"

def get_track_id(query,token):
    spotify = spotipy.Spotify(auth=token)
    results = spotify.search(query, limit=1)
    return results['tracks']['items'][0]['id']
# def get_track_name(query,token):
#     spotify = spotipy.Spotify(auth=token)
#     results1 = spotify.search(name, limit = 100)
#     the_song = ""
#     max = 0
#     for i in range(0, len(results1)):
#         word = results1(i)
#         max1 = lev.ratio(query, word)
#         if(max1>max):
#             max = max1
#             the_song = word
#
#     return the_song
#
# get_track_name("bump'n'grind",token)
# def track_on_lyrics(query,token):
#
#     eLyrics = []
#
#     for item in gdata:
#         title = item.find_all('a', {'itemprop': 'name'})[0].text
#         lyricsdotcom = 'http://www.lyrics.com'
#         for link in item('a'):
#             try:
#                 lyriclink = lyricsdotcom + link.get('href')
#                 req = requests.get(lyriclink)
#                 lyricsoup = BeautifulSoup(req.content)
#                 lyricdata = lyricsoup.find_all('div', {'id': re.compile('lyric_space|lyrics')})[0].text
#                 eLyrics.append([title, lyricdata])
#             except:
#                 pass








