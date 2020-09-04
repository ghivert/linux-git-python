import requests
import json

def query_github():
    # Si jamais pas de 403
    url = "enter-github-api-url"
    response = requests.get(url)
    data = response.json()

    # Si jamais 403
    path = './repositories.json' # chemin vers repositories.json ou repositories-stars.json pour la deuxième question
    data = read_from_local_data(path)

    for dict in data:
        print(dict["name"])
        print(dict["description"])

# Si jamais vous tombez sur une Erreur 403:
def read_from_local_data(path):
    file = open(path)
    content = file.read()
    file.close()
    return json.loads(content)
