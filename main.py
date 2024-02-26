from utils.select_language import select_language
from modules.dump_song_names import dump_song_names
from modules.generate_spotify_playlist import generate_spotify_playlist
import utils.messages as messages

def main():
    language = select_language()

    print(messages.EXPLANATION_MESSAGE[language])

    dump_file = dump_song_names(language)
    generate_spotify_playlist(dump_file, language)

    print('\n' + messages.THANKS_MESSAGE[language])
    print(messages.SIGNATURE_MESSAGE)

if __name__ == "__main__": main()