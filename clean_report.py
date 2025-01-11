import json
import unicodedata


def clean_value(value):
    if not isinstance(value, dict):
        return value

    if 'result' in value:
        result = value['result']

        cleaned_dict = {
            'artist': result.get('artist', None),
            'title': result.get('title', None),
            'album': result.get('album', None),
            'release_date': result.get('release_date', None),
        }

        if 'spotify' in value['result']:
            spotify = value['result']['spotify']

            cleaned_dict.update({
                'spotify.uri': spotify.get('uri', None),
                'spotify.track_number': spotify.get('track_number', None),
                'spotify.href': spotify.get('href', None),
                'spotify.id': spotify.get('id', None),
            })

        for k, v in cleaned_dict.items():
            if isinstance(v, str):
                v = unicodedata.normalize('NFKD', v).encode(
                    'ascii', 'ignore').decode('ascii')
                cleaned_dict[k] = v

        return cleaned_dict


def clean_key(key):
    key = key.split('/')[-1]
    key = key.replace('.mp3', '')
    key = unicodedata.normalize('NFKD', key).encode(
        'ascii', 'ignore').decode('ascii')
    key = ' '.join(key.split())
    return key


def clean_report():
    with open('report2.json', 'r') as f:
        data = json.load(f)

        null_data = {clean_key(k): v for k, v in data.items() if v is None}
        cleaned_data = {clean_key(k): clean_value(v)
                        for k, v in data.items() if v is not None}

        with open('report_cleaned2.json', 'w') as f:
            json.dump(cleaned_data, f, indent=2)

        with open('report_null2.json', 'w') as f:
            json.dump(null_data, f, indent=2)


def divide_report_spotify():
    with open('reports/report_spotify.json', 'r') as f:
        data = json.load(f)

        with_spotify = {k: v for k, v in data.items() if 'spotify.uri' in v}
        withouth_spotify = {k: v for k, v in data.items() if 'spotify.uri' not in v}

        with open('report_spotify.json', 'w') as f:
            json.dump(with_spotify, f, indent=2)
            
        with open('report_no_spotify.json', 'w') as f:
            json.dump(withouth_spotify, f, indent=2)
            
divide_report_spotify()