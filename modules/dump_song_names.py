import os
import utils.messages as messages
import re
from unidecode import unidecode

def clean_song_name(song):
    # Remove the file extension
    if '.mp3' in song: song = song.replace('.mp3', '')
    if '.m4a' in song: song = song.replace('.m4a', '')
    if '.wav' in song: song = song.replace('.wav', '')
    if '.flac' in song: song = song.replace('.flac', '')
    if '.ogg' in song: song = song.replace('.ogg', '')

    # Remove special characters
    song = re.sub(r'[^a-zA-Z0-9\s]', '', song)

    # Remove accents
    song = unidecode(song)

    # Replace '-' and '_' with spaces
    if '-' in song: song = song.replace('-', ' ')
    if '_' in song: song = song.replace('_', ' ')

    # Remove thins between parentheses
    song = re.sub(r'\([^)]*\)', '', song)
    song = re.sub(r'\[[^)]*\]', '', song)
    song = re.sub(r'\{[^)]*\}', '', song)

    # Remove the track number from the song name
    if song[0].isdigit(): song = song.split(' ', 1)[-1]

    # Remove multiple spaces and convert the string to lowercase
    return ' '.join(song.lower().split())


def dump_song_names(language):
    # Get the folder name from the user
    folder = input('\n' + messages.FOLDER_NAME_MESSAGE[language])

    # Generate a .txt file with the names of the songs in the folder
    dump_file = "dump_file.txt"
    if os.path.exists(dump_file): os.remove(dump_file)

    # Write the names of the songs in the .txt file
    with open(dump_file, 'w') as dump:
        for _, _, files in os.walk(folder):
            for file in files: dump.write(clean_song_name(file) + '\n')

    print(messages.DUMP_FILE_MESSAGE[language] + "\n")

    return dump_file