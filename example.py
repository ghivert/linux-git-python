import os
import requests
from bs4 import BeautifulSoup

# Interagir avec l’OS
def reader():
    current_working_directory = os.getcwd()
    files = os.listdir()
    print(current_working_directory)
    print(files)

reader()
os.chdir('/bin')
reader()

# Lire un fichier
file = open('./test.py')
print(file.read())

# Interagir avec le monde extérieur (HTTP)
results = requests.get('https://google.com')
parser = BeautifulSoup(results.text)
for link in parser.find_all('a'):
    print(link)
