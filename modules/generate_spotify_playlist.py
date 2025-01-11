import spotipy
from spotipy.oauth2 import SpotifyOAuth
import utils.messages as messages

def get_token_info(language, sp_oauth):
    token_info = sp_oauth.get_cached_token()

    # In case the token is not cached, ask the user to authorize the app
    if not token_info:
        auth_url = sp_oauth.get_authorize_url()

        print(messages.GET_TOKEN_MESSAGE[language].format(auth_url = auth_url))
        response = input(messages.TYPE_URL_MESSAGE[language])

        code = sp_oauth.parse_response_code(response)
        token_info = sp_oauth.get_access_token(code)

    return token_info

def get_spotify_auth(language):
    # Get the user's credentials for the Spotify API
    client_id = input(messages.CLIENT_ID_MESSAGE[language])
    client_secret = input(messages.CLIENT_SECRET_MESSAGE[language])
    redirect_uri = "https://developer.spotify.com/"

    # Get authorization to use the Spotify API
    sp_oauth = SpotifyOAuth(
        client_id = client_id,
        client_secret = client_secret,
        redirect_uri = redirect_uri,
        scope = 'playlist-modify-private playlist-modify-public'
    )

    token_info = get_token_info(language, sp_oauth)

    return spotipy.Spotify(auth = token_info['access_token'])


def generate_playlist(sp, dump_file, language):
    # Read the file with the song names and store them in a list
    with open(dump_file, 'r') as file: songs = file.readlines()

    # Create a new playlist with the name entered by the user
    playlist_name = input(messages.PLAYLIST_NAME_MESSAGE[language])
    print()

    playlist = sp.user_playlist_create(
        sp.me()['id'],
        playlist_name,
        public = False
    )

    playlist_id = playlist['id']

    # Add the songs to the playlist using the Spotify API
    not_found = []

    for song in songs:
        # Clean the song name string and remove the '.mp3' extension
        song = song.strip().replace('.mp3', '')
        if song[0].isdigit(): song = song.split(' ', 1)[-1]

        # Search for the song in Spotify
        results = sp.search(q=song, type='track', limit=1)

        # Add the song to the playlist
        if results['tracks']['items']:
            song_id = results['tracks']['items'][0]['id']
            song_name = results['tracks']['items'][0]['name']
            song_artist = results['tracks']['items'][0]['artists'][0]['name']

            sp.playlist_add_items(playlist_id, [song_id])
            print(messages.SONG_ADDED_MESSAGE.format(artist=song_artist, song=song_name))
        else:
            not_found.append(song)

    if not_found:
        print('\n' + messages.SOME_SONGS_NOT_FOUND_MESSAGE[language])
        for song in not_found: print(messages.SONG_NOT_FOUND_MESSAGE.format(song=song))
    else:
        print('\n' + messages.PLAYLIST_CREATED_MESSAGE[language])


def generate_spotify_playlist(dump_file, language):
    sp = get_spotify_auth(language)
    generate_playlist(sp, dump_file, language)