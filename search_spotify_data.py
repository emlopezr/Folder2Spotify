from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Load the report file
with open('reports/report_no_spotify.json', 'r') as file:
    data = json.load(file)

# Spotify API credentials (replace with your own)
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
PLAYLIST_ID = os.getenv("SPOTIFY_PLAYLIST_ID")

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

def search_spotify(artist, title):
    """Search Spotify for a track by artist and title."""
    query = f"{title} {artist}"
    results = sp.search(q=query, type="track", limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        return {
            'spotify.uri': track.get('uri'),
            'spotify.track_number': track.get('track_number'),
            'spotify.href': track.get('external_urls').get('spotify'),
            'spotify.id': track.get('id'),
        }
    return None

# Iterate over the data and update with Spotify details
for key, value in data.items():
    artist = value.get('artist', '')
    title = value.get('title', '')

    if artist and title:
        spotify_data = search_spotify(artist, title)
        if spotify_data:
            value.update(spotify_data)

# Save the updated data back to the file
with open('reports/report_search_spotify.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Updated report saved as 'reports/report_search_spotify.json'")
