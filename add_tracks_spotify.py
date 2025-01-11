# Get data from report_spotify.json and report_no_spotify_search.json
# Add each song to the specified playlist using the Spotify API

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import json
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# Load the report file
with open('reports/report_spotify.json', 'r') as file:
    data = json.load(file)

# Spotify API credentials (replace with your own)
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
PLAYLIST_ID = os.getenv("PLAYLIST_ID")

def authenticate():
    scopes = [
      "user-library-read",
      "playlist-modify-public",
      "playlist-modify-private",
      "playlist-read-private",
    ]
    scope_string = " ".join(scopes)

    sp = Spotify(auth_manager=SpotifyOAuth(
        client_id = SPOTIFY_CLIENT_ID,
        client_secret = SPOTIFY_CLIENT_SECRET,
        redirect_uri = SPOTIFY_REDIRECT_URI,
        scope = scope_string,
        open_browser = False
    ))

    return sp

# Authenticate with Spotify
sp = authenticate()

# Sort data by: release_date, artist, album, spotify.track_number
def safe_sort_key(item):
    release_date = item[1].get('release_date', '') or ''

    # Convert release_date to datetime object
    if release_date:
        release_date = datetime.strptime(release_date, '%Y-%m-%d')
    else:
        release_date = datetime.strptime('9999-12-31', '%Y-%m-%d')

    artist = item[1].get('artist', '').lower() or ''
    album = item[1].get('album', '').lower() or ''
    track_number = item[1].get('spotify.track_number', 0) or 0

    return (release_date, artist, album, track_number)

data = dict(sorted(data.items(), key=safe_sort_key))

# Add each song to the specified playlist using the Spotify API with URI
uris = [ value['spotify.uri'] for value in data.values() if 'spotify.uri' in value ]

# Send in batches of 50
for i in range(0, len(uris), 50):
    try:
        sp.playlist_add_items(PLAYLIST_ID, uris[i:i+50])
        print(f'Songs added to the playlist: {i+1} to {i+50}')
    except Exception as e:
        print(f"Error: {e}")
        print('Failed to add songs to the playlist')