1. Définissez une fonction `max()` qui prend deux nombres comme arguments et renvoie le plus grand d'entre eux. Utilisez la construction if-then-else disponible en Python. (Il est vrai que Python a la fonction `max()` intégrée, mais l'écrire soi-même est néanmoins un bon exercice).

2. Définissez une fonction `max_of_three()` qui prend trois nombres comme arguments et renvoie le plus grand d'entre eux.

3. Définissez une fonction qui calcule la longueur d'une liste ou d'une chaîne de caractères donnés. (Python a intégré la fonction `len()`, mais l'écrire soi-même est néanmoins un bon exercice ).

4. Écrivez une fonction qui prend un caractère (c'est-à-dire une chaîne de longueur 1) et qui retourne `True` si c'est une voyelle, `False` sinon.

5. Écrivez une fonction `translate()` qui traduira un texte en "rövarspråket" (suédois pour "langue du voleur"), c'est-à-dire, doublez chaque consonne et placez une occurrence de "o" entre les deux. Par exemple, `translate("this is fun")` devrait retourner la chaîne "tothohisos isos fofunon".

6. Définissez une fonction `sum()` et une fonction `multiply()` qui additionnent et multiplient (respectivement) tous les nombres dans une liste de nombres. Par exemple, `sum([1, 2, 3, 4])` devrait retourner 10, et `multiply([1, 2, 3, 4])` devrait retourner 24.

7. Définissez une fonction `reverse()` qui calcule l'inversion d'une chaîne de caractères. Par exemple, `reverse( "I am testing" )` devrait retourner la chaîne "gnitset ma I".

8. Définissez une fonction `is_palindrome()` qui reconnaît les palindromes (c'est-à-dire les mots qui se ressemblent écrits à l'envers). Par exemple, `is_palindrome("radar")` doit retourner True.

9. Écrivez une fonction `is_member()` qui prend une valeur (c'est-à-dire un nombre, une chaîne de caractères, etc.) x et une liste de valeurs a, et qui renvoie `True` si x est un membre de a, `False` sinon. (Notez que c'est exactement ce que fait l'opérateur `in`, mais pour les besoins de l'exercice, vous devez prétendre que Python n'a pas cet opérateur).

10. Définissez une fonction `overlapping()` qui prend deux listes et renvoie `True` si elles ont au moins un membre en commun, `False` sinon. Vous pouvez utiliser votre fonction `is_member()`, ou l'opérateur `in`, mais pour les besoins de l'exercice, écrivez le également en utilisant deux boucles for imbriquées.

11. Définissez une fonction `generate_n_chars()` qui prend un entier n et un caractère c et renvoie une chaîne de n caractères, composée uniquement de c:s. Par exemple, `generate_n_chars( 5, "x" )` devrait retourner la chaîne "xxxxx" (Python est inhabituel dans la mesure où vous pouvez écrire une expression `5 \* "x"` qui sera évaluée à "xxxxx". Pour les besoins de l'exercice, vous devez ignorer que le problème peut être résolu de cette manière).

12. Définissez une procédure `histogram()` qui prend une liste d'entiers et imprime un histogramme à l'écran. Par exemple, `histogram( [ 4, 9, 7 ] )` devrait imprimer ce qui suit :

```
****
*********
*******
```

13. La fonction `max()` de l'exercice 1) et la fonction `max_of_three()` de l'exercice 2) ne fonctionneront que pour deux et trois nombres, respectivement. Mais supposons que nous ayons un nombre beaucoup plus important de nombres, ou supposons que nous ne puissions pas dire à l'avance combien ils sont… Écrivez une fonction `max_in_list()` qui prend une liste de nombres et renvoie le plus grand.

14. Écrivez un programme qui fait correspondre une liste de mots à une liste d'entiers représentant les longueurs des mots correspondants.

15. Écrivez une fonction `find_longest_word()` qui prend une liste de mots et retourne la longueur du plus long.

16. Écrivez une fonction `filter_long_words()` qui prend une liste de mots et un entier n et retourne la liste des mots qui sont plus longs que n.

17. Rédiger une version d'un identificateur de palindrome qui accepte également les palindromes de phrases telles que :
    "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", ou l'exclamation "Dammit, I'm mad!".
    Notez que la ponctuation, les majuscules et l'espacement sont généralement ignorés.

18. Un pangramme est une phrase qui contient toutes les lettres de l'alphabet anglais au moins une fois, par exemple : "The quick brown fox jumps over the lazy dog". Votre tâche ici est d'écrire une fonction pour vérifier une phrase afin de voir si c'est un pangramme ou non.

19. "99 Bottles of Beer" est une chanson traditionnelle aux États-Unis et au Canada. Elle est populaire pour les longs voyages, car elle a un format très répétitif, facile à mémoriser et peut prendre beaucoup de temps à chanter. Les paroles simples de la chanson sont les suivantes :
    « Take one down, pass it around, 98 bottles of beer on the wall. »
    Le même verset est répété, à chaque fois avec une bouteille de moins. La chanson est terminée lorsque le ou les chanteurs atteignent le zéro. Votre tâche ici est d'écrire un programme Python capable de générer tous les vers de la chanson.

20. Représenter un petit lexique bilingue comme un dictionnaire Python de la manière suivante :

`{"merry" : "god", "christmas" : "jul", "and" : "och", "happy":gott", "new" : "nytt", "year" : "år" }`

Et utilisez le pour traduire vos cartes de Noël de l'anglais au suédois. C'est-à-dire, écrivez une fonction `translate()` qui prend une liste de mots anglais et renvoie une liste de mots suédois.

21. Écrivez une fonction `char_freq()` qui prend une chaîne de caractères et construit une liste de fréquence des caractères qu'elle contient. Représentez la liste de fréquence comme un dictionnaire Python. Essayez-le avec quelque chose comme :

    `char_freq("abbabcbdbabdbdbabababcbcbab")`

22. En cryptographie, le chiffrement de César est une technique de cryptage très simple dans laquelle chaque lettre du texte en clair est remplacée par une lettre à un nombre fixe de positions dans l'alphabet. Par exemple, avec un décalage de 3, A serait remplacé par D, B deviendrait E, et ainsi de suite. Cette méthode porte le nom de Jules César, qui l'utilisait pour communiquer avec ses généraux. ROT-13 ("rotation de 13 places") est un exemple largement utilisé de chiffre de César où le décalage est de 13. En Python, la clé pour ROT-13 peut être représentée au moyen du dictionnaire suivant :

```
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
```

Votre tâche dans cet exercice est de mettre en œuvre un encodeur/décodeur de ROT-13. Une fois que vous aurez terminé, vous serez en mesure de lire le message secret suivant :
`Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!`
Notez que puisque l'anglais compte 26 caractères, votre programme ROT-13 pourra à la fois encoder et décoder les textes écrits en anglais.

23. Définissez une fonction simple de "correction orthographique" `correct()` qui prend une chaîne de caractères et veille à ce que 1) deux ou plusieurs occurrences du caractère espace soient compressées en une, et 2) insère un espace supplémentaire après un point si celui-ci est directement suivi d'une lettre. Par exemple, `correct("This is very funny and cool.Indeed!")` devrait retourner : "This is very funny and cool. Indeed!". Conseil : Utilisez des expressions régulières !

24. La forme verbale à la troisième personne du singulier en anglais se distingue par le suffixe -s, qui est ajouté à la racine de la forme infinitive : run > runs. Un ensemble de règles simples peut être donné comme suit :

    a. Si le verbe se termine par y, on le supprime et on ajoute ies
    b. Si le verbe se termine par o, ch, s, sh, x ou z, ajoutez es
    c. Par défaut, il suffit d'ajouter s
    Votre tâche dans cet exercice est de définir une fonction `make_3sg_form()` qui, donnée à un verbe à l'infinitif, renvoie sa forme à la troisième personne du singulier. Testez votre fonction avec des mots comme try, brush, run et fix. Notez cependant que les règles doivent être considérées comme heuristiques, dans le sens où vous ne devez pas vous attendre à ce qu'elles fonctionnent pour tous les cas. Conseil : Vérifiez la méthode de chaîne de caractères `endswith()`.

25. En anglais, le participe présent est formé en ajoutant le suffixe -ing à la forme infinie : go > going. Un ensemble simple de règles heuristiques peut être donné comme suit :
    a. Si le verbe se termine par e, laisser tomber le e et ajouter ing (be, see, flee, knee, etc.)
    b. Si le verbe se termine par ie, changez ie en y et ajoutez ing
    c. Pour les mots composés de consonne-voyelle-consonne, doublez la dernière lettre avant d'ajouter -ing
    d. Par défaut, il suffit d'ajouter -ing
    Votre objectif dans cet exercice est de définir une fonction `make_ing_form()` qui, en donnant un verbe à l'infinitif, retourne sa forme de participe présent. Testez votre fonction avec des mots tels que lie, see, move et hug. Cependant, vous ne devez pas vous attendre à ce que des règles aussi simples fonctionnent dans tous les cas.
