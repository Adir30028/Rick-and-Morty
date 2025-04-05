import requests

BASE_URL = "https://rickandmortyapi.com/api/character"

def fetch_all_characters():
    characters = []
    next_url = BASE_URL
    while next_url:
        response = requests.get(next_url)
        data = response.json()
        characters.extend(data['results'])
        next_url = data['info']['next']
    return characters

def filter_characters(characters):
    filtered = []
    for char in characters:
        if (
            char['species'] == 'Human' and
            char['status'] == 'Alive' and
            char['origin']['name'].lower().startswith('earth')
        ):
            filtered.append({
                'Name': char['name'],
                'Location': char['location']['name'],
                'Image': char['image']
            })
    return filtered
