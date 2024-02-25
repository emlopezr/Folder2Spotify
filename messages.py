SELECT_LANGUAGE_MESSAGE = "Select your language / Selecciona tu idioma:"
ENGLISH_OPTION_MESSAGE = "1. English"
SPANISH_OPTION_MESSAGE = "2. Español"
ENTER_NUMBER_MESSAGE = "Enter the corresponding number / Introduce el número correspondiente: "
INVALID_OPTION_MESSAGE = "Invalid option / Opción inválida\n"

GH_REPO_LINK = "https://github.com/emlopezr/Folder2Spotify"
SPOTIFY_API_LINK = "https://developer.spotify.com/dashboard/applications"


EXPLANATION_MESSAGE = {
    "ES": f"""Este programa te permite crear una playlist en Spotify con las canciones que tengas en una carpeta.\nEs importante que las canciones tengan el nombre del artista y el nombre de la canción en el nombre del archivo para que el programa pueda buscarlas en Spotify de manera efectiva, por ejemplo: "Artista - Canción.mp3". En caso de que el nombre del archivo no siga este formato, el programa encontrará una canción con pero no necesariamente será la que buscas.\nPara usar este programa necesitas tener una cuenta de Spotify, un ID de cliente y una clave secreta de cliente. Puedes obtener estos datos en la página de desarrolladores de Spotify ({SPOTIFY_API_LINK}).\nPara una guía más detallada sobre cómo usar este programa, visita el repositorio en GitHub: ({GH_REPO_LINK}) y lee el archivo README.md\n""",

    "EN": f"""This program allows you to create a playlist on Spotify with the songs you have in a folder.\nIt is important that the songs have the artist's name and the song's name in the file name so that the program can search for them on Spotify effectively, for example: "Artist - Song.mp3". If the file name does not follow this format, the program will find a song but it may not be the one you are looking for.\nTo use this program you need to have a Spotify account, a client ID and a client secret. You can get this data on the Spotify Developer Dashboard ({SPOTIFY_API_LINK}).\nFor a more detailed guide on how to use this program, visit the GitHub repository: ({GH_REPO_LINK}) and read the README.md file.\n"""
}

FOLDER_NAME_MESSAGE = {
    "EN": "Enter the folder name with the songs: ",
    "ES": "Introduce el nombre de la carpeta con las canciones: "
}

DUMP_FILE_MESSAGE = {
    "EN": "The file with the song names has been created",
    "ES": "Se ha creado el archivo con los nombres de las canciones"
}

PLAYLIST_NAME_MESSAGE = {
    "EN": "Enter the name of the playlist: ",
    "ES": "Introduce el nombre de la playlist: "
}

SONG_ADDED_MESSAGE = "☑ {artist} - {song}"
SONG_NOT_FOUND_MESSAGE = "⚠ '{song}'"

PLAYLIST_CREATED_MESSAGE = {
    "EN": "All songs have been added to the playlist",
    "ES": "Se han agregado todas las canciones a la playlist"
}

SOME_SONGS_NOT_FOUND_MESSAGE = {
    "EN": "Some songs were not found in Spotify",
    "ES": "Algunas canciones no se encontraron en Spotify"
}

CLIENT_ID_MESSAGE = {
    "EN": "Enter your Spotify client ID: ",
    "ES": "Introduce tu ID de cliente de Spotify: "
}

CLIENT_SECRET_MESSAGE = {
    "EN": "Enter your Spotify client secret: ",
    "ES": "Introduce tu clave secreta de cliente de Spotify: "
}

GET_TOKEN_MESSAGE = {
    "EN": "Go to this URL to authorize the app:\n{auth_url}",
    "ES": "Ve a esta URL para autorizar la aplicación:\n{auth_url}"
}

TYPE_URL_MESSAGE = {
    "EN": "Enter the redirect URL:\n",
    "ES": "Introduce la URL de redirección:\n"
}

THANKS_MESSAGE = {
    "EN": "Thanks for using this program",
    "ES": "Gracias por usar este programa"
}

SIGNATURE_MESSAGE = "<3 - @emlopezr (GitHub)"
