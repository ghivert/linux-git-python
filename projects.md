# Linux / Git / Python

## Vérifier les derniers dépôts public sur Github.

Le but du projet va être d’extraire des informations de GitHub, puis d’automatiser le tout pour le faire périodiquement et envoyer une notification sur notre bureau. Dans un premier temps, l’idée est de découvrir l’API de Github, puis ensuite d’extraire des informations sur des dépôts publics, avant d’automatiser le tout, rajouter quelques fonctionnalités, puis pouvoir cibler un utilisateur en particulier.

# Python

Pour rappel, installer `requests` : `pip3 install requests`.

En utilisant les modules `os` et `requests` de Python et les livres du dossier `books`, réaliser les exercices suivants :

- Écrire un script capable de trouver le titre et l’auteur de chaque livre.
- En utilisant le script précédent, écrire un script qui renomme chaque livre avec le nom `[nom du livre]-[nom de l’auteur].txt`. Le nom devra être tout en minuscule et les espaces (` `) seront remplacés par des blancs soulignés (`_`).
- Écrire un script qui compte le nombre de mots de chaque livre.
- Écrire un script qui comptabilise le nombre d’occurrences de chaque mot pour chaque livre.
- À partir du script précédent, écrire un script qui comptabilise le nombre de chaque mot **tous livres confondus**. Indiquer les 10 mots les plus utilisés et les imprimer.

- Écrire un script qui extrait les informations de `http://www.gutenberg.org/robot/harvest` et récupère tous les liens vers les livres.
- Compléter le script pour télécharger les livres en zip depuis chacun des liens (utiliser `zipfile`).
- Extraire les livres et les nommer convenablement.

Bonus :

- Extraire tous les livres du site en utilisant les offsets de page.
