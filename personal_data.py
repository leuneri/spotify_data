import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from pathlib import Path  

import json

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
playlists = sp.user_playlists('secular1')
playlist_uri = []
while playlists:
    for i, playlist in enumerate(playlists['items']):
        playlist_uri.append(playlist['uri'][17:])
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

information = []
# i = playlist_uri[0]
# print(sp.playlist_tracks(i))

# for i in playlist_uri:
#     information.append(sp.playlist_tracks(i))

a = playlist_uri[0]
x = sp.playlist_tracks(a)

json_object = json.dumps(x)
with open("sample.json", "w") as outfile:
    outfile.write(json_object)


# df = pd.DataFrame.from_records(i)
# filepath = Path('C:/Users/ericl/spotify_data/information.csv')  
# filepath.parent.mkdir(parents=True, exist_ok=True)  
# df.to_csv(filepath)  