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

#pick an artist and search top 10 songs from artist

artist = input("Please choose an artist: ")

#get artist uri from spotify based on what artist the user typed in

#first, search for an artist. Then, convert result into a string to find the spotify id
artist_search = str(sp.search(q="artist:{}".format(artist), type="track"))

#find the spotify id from the string using a regular expression that matches a spotify id
get_uri = re.search('([0-9]+([a-zA-Z]+[0-9]+)+)[a-zA-Z]+', artist_search)

print("spotify:artist:{}".format(get_uri.group(0)))

#turn the spotify id into a spotify uri
artist_uri = "spotify:artist:{}".format(get_uri.group(0))

#find top tracks of artist using the artist uri
results = sp.artist_top_tracks(artist_uri)

#print name of track, audio link, and cover art link for the artist
for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
