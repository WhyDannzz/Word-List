import requests

api_key = '191fedc0-0f31-4047-99fa-767fe0010cea'
word = 'Anime'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)