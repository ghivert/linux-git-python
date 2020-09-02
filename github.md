# Projet

- Créer un script qui [vérifie les derniers dépôts publics sur Github](https://docs.github.com/en/rest/reference/repos#list-public-repositories) et logs ses opérations dans un fichier.
  1. En utilisant le module `requests`, appeler l’API GitHub à l’aide d’une requête GET.
  2. Récupérer la réponse qui est sous format JSON. Pour vérifier le format du JSON, il est possible de l’afficher directement dans Chrome en consultant la page `https://api.github.com/repositories` !
  3. Pour chaque élément de la réponse, écrire le nom du dépôt dans un fichier, et sa description _si elle existe_.

- Créer un script qui [vérifie quels sont les dépôts les plus populaires depuis le début de l’année](https://docs.github.com/en/rest/reference/search#search-repositories) et logs ses opérations dans un fichier. Les dépôts les plus populaires sont les dépôts avec le plus d’étoiles.
  1. En utilisant le module `requests`, appeler l’API GitHub à l’aide d’une requête GET. Attention, il faut bien former l’URL : il est nécessaire de rajouter des paramètres dans l’URL.
  2. Récupérer la réponse qui est sous format JSON. Encore une fois, pour vérifier que tout se passe bien, il est possible d’afficher directement le résultat de la requête dans Chrome.
  3. Pour chaque élément de la réponse, écrire le nom du dépôt dans un fichier et sa description, ainsi que son nombre d’étoiles.

- Les programmer régulièrement à l’aide d’un cron Linux.
  1. Éditer le fichier crontab pour exécuter le script python régulièrement.

- Plutôt que de stocker les résultats de nos requêtes dans un fichier texte, nous souhaitons les stocker le tout dans un fichier JSON directement sur l’ordinateur.
  1. Dans chaque script, stocker ses résultats dans un dictionnaire Python.
  2. En utilisant [le module `JSON`](https://docs.python.org/fr/3/library/json.html) et `dumps`, transformer le dictionnaire Python en une chaîne de caractères.
  3. En utilisant `open()` et `file.write()`, écrire la string dans un fichier que l’on nommera `data.json`.
  4. À chaque démarrage du programme, utiliser `open()` et `file.read()`, ainsi que le module `JSON` et `loads`, lire le fichier `data.json` et l’utiliser comme dictionnaire de base.

- Modifier légèrement le script pour faire en sorte de surveiller un utilisateur précis. Relever tous ses dépôts publics, puis pour chacun, vérifier périodiquement s’il a reçu de nouvelles étoiles. Proposez comment le faire, puis l’implémenter.

- Proposez une manière d’envoyer une notification sur le bureau à chaque nouveau dépôt créé par l’utilisateur. Faites aussi en sorte de pouvoir envoyer la notification par email. Envoyez également un email en fin de journée pour récapituler toutes les informations qui se sont déroulés durant la journée.

- Ajoutez un moyen de surveiller et notifier lors de nouveaux followers sur GitHub.
