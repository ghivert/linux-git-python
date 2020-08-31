# Linux / Git / Python

## Vérifier les derniers dépôts public sur Github.

Le but du projet va être d’extraire des informations de GitHub, puis d’automatiser le tout pour le faire périodiquement et envoyer une notification sur notre bureau. Dans un premier temps, l’idée est de découvrir l’API de Github, puis ensuite d’extraire des informations sur des dépôts publics, avant d’automatiser le tout, rajouter quelques fonctionnalités, puis pouvoir cibler un utilisateur en particulier.

# Premier jour

- Créer un script qui [vérifie les derniers dépôts publics sur Github](https://docs.github.com/en/rest/reference/repos#list-public-repositories) et logs ses opérations dans un fichier.
- Créer un script qui [vérifie quels sont les dépôts les plus populaires depuis le début de l’année](https://docs.github.com/en/rest/reference/search#search-repositories) et logs ses opérations dans un fichier.
- Les programmer régulièrement à l’aide d’un cron Linux.
- Les transformer en "daemon", qui tourneront en tâche de fond en permanence et feront les requêtes régulièrement.
- Envoyer une notification à chaque fois qu’un nouveau dépôt public est créé. Cliquer sur la notification doit ouvrir le dépôt sur un navigateur.
- Envoyer un mail avec un récapitulatif à chaque fin de journée des nouvelles étoiles sur les dépôts les plus populaires.
- Stocker le tout dans un fichier JSON directement sur l’ordinateur.
- Ajouter une option pour faire la même chose pour un utilisateur précis : tous ses dépôts publics, combien d’étoiles tous les jours, combien de nouvelles. Il va falloir configurer comment surveiller un utilisateur.
- Ajouter l’option d’être informé des nouveaux followers sur Github.
