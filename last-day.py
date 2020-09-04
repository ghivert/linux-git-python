import requests
import json

def query_github():
    url = "enter-github-api-url"
    response = requests.get(url)
    data = response.json()
    for dict in data:
        print(dict["name"])
        print(dict["description"])

# Si jamais vous tombez sur une Erreur 403:
def read_from_local_data():
    path = './repositories.json' # chemin vers repositories.json ou repositories-stars.json pour la deuxième question
    file = open(path)
    content = file.read()
    file.close()
    return json.loads(content)
