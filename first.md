# Linux / Git / Python

1. Installation de l’environnement

- Utiliser une machine virtuelle sous Linux (Ubuntu par exemple) ou directement sur un ordinateur Linux ou macOS.
- [Télécharger VirtualBox](https://www.virtualbox.org/)
- [Télécharger Ubuntu](https://ubuntu.com/download/desktop)
- [Suivre le tutorial suivant pour installer son environnement](https://brb.nci.nih.gov/seqtools/installUbuntu.html)

- Il faut récupérer son environnement de développement.

```bash
sudo apt update
sudo apt install build-essential libssl-dev libffi-dev python3-dev
```

- Installer un éditeur de texte : [Visual Studio Code](https://code.visualstudio.com/) ou [Atom](https://atom.io/)

```bash
# Pour Atom
sudo snap install atom --classic

# Pour VS Code
sudo snap install code --classic
```

- Installer git

```bash
sudo apt install git
```

- Installer Python s’il n’est pas déjà installé.

```bash
python3 -V
# Doit indiquer un numéro de version >= 3.7.0, sinon
sudo apt install python3
```

- Installer pip pour utiliser des packages Python

```bash
sudo apt install python3-pip
```



2. Vérifier les derniers dépôts public sur Github.

- Créer un script qui [vérifie les derniers dépôts publics sur Github](https://docs.github.com/en/rest/reference/repos#list-public-repositories) et logs ses opérations dans un fichier.
- Créer un script qui [vérifie quels sont les dépôts les plus populaires depuis le début de l’année](https://docs.github.com/en/rest/reference/search#search-repositories) et logs ses opérations dans un fichier.
- Les programmer régulièrement à l’aide d’un cron Linux.
- Les transformer en "daemon", qui tourneront en tâche de fond en permanence et feront les requêtes régulièrement.

Bonus :

- Envoyer une notification à chaque fois qu’un nouveau dépôt public est créé. Cliquer sur la notification doit ouvrir le dépôt sur un navigateur.
