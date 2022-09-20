#Goal: a game where you pick an artist, and Spotify returns 5 second clips of songs for you to guess. 

#log into spotify

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import random
import re

cid = 'b2079ac4f9724c90a3f89deb9726d640'
secret = 'da41045a0037497ebc373568a7af1fa2'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

#get artist info
def get_artist_id(artist):
    search_results = sp.search(q = artist, limit = 10, type = "artist")
    artist_id =  search_results["artists"]["items"][0]["id"]
    return artist_id

#get artist top 10 tracks
def artist_top_tracks(my_artist_id):
    search_results = sp.artist_top_tracks(artist_id = my_artist_id)
    return search_results


artist = input("Please enter an artist name: ")
my_artist_id = get_artist_id(artist)
print("Your artist's URI is: \n{}".format(my_artist_id))
print("Top tracks for this artist are: \n")
print(artist_top_tracks(my_artist_id))


