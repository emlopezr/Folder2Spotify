import os
import messages

def dump_song_names(language):
    # Get the folder name from the user
    folder = input(messages.FOLDER_NAME_MESSAGE[language])

    # Create a .txt file with the names of the songs in the folder
    dump_file = f"{folder}.txt"

    # If the file already exists, delete it
    if os.path.exists(dump_file): os.remove(dump_file)

    # Write the names of the songs in the .txt file
    with open(dump_file, 'w') as dump:
        for _, _, files in os.walk(folder):
            for file in files: dump.write(file + '\n')

    print(messages.DUMP_FILE_MESSAGE[language] + "\n")

    return dump_file