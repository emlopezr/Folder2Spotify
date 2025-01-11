import requests
import json
import os
from clean_report import clean_report
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('AUDD_API_TOKEN')
BASE_DIR = 'songs_mp3'

def get_filepaths(base_dir):
    mp3_files = []
    non_mp3_files = []

    for root, _, files in os.walk(base_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith('.mp3'):
                mp3_files.append(file_path)
            else: non_mp3_files.append(file_path)

    return mp3_files, non_mp3_files

def identify_song(file_path):
    url = 'https://api.audd.io/'
    data = { 'api_token': API_TOKEN, 'return': 'spotify' }
    files = { 'file': open(file_path, 'rb') }

    response = requests.post(url, data=data, files=files)

    try:
        resp_json = response.json()

        if resp_json['result'] is None:
            print('- Song not found')
            return None

        return resp_json

    except Exception as e:
        print(f"Error: {e}")
        print(f"Response: {response.text}")
        return None

# mp3_files, non_mp3_files = get_filepaths(BASE_DIR)

non_mp3_files = []

mp3_files = []
with open('remaining_files.txt', 'r') as f:
    for line in f: mp3_files.append(line.strip())

final_response = {}

if not mp3_files:
    print('No mp3 files found in the directory')
    exit()

if non_mp3_files:
    print('Non mp3 files found in the directory')
    for file in non_mp3_files: print(f"- {file}")


# Just first 225 files (due to API limitations)
# Save the rest of the files for later in a Txt file
if len(mp3_files) > 225:
    with open('remaining_files.txt', 'w') as f:
        for file in mp3_files[225:]: f.write(f"{file}\n")

    mp3_files = mp3_files[:225]
    print('Only first 225 files will be processed due to API limitations\n')

for file in mp3_files:
    print(f"{file}...")

    try:
        response = identify_song(file)
        final_response[file] = response
        print()
    except Exception as e:
        continue

with open('report2.json', 'w') as f:
    json.dump(final_response, f, indent=2)

clean_report()
print('Reports generated successfully')