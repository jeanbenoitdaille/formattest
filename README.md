# formattest
Formater le test avec format 
Beaucoup de lignes de codes qui ne font pas forcément de sens à prime abord dans cet exercice, nous allons donc pas à pas expliquer la logique derrière cette solution.

Tout d'abord, nous déclarons un certain nombre de variables : le texte à afficher, la longueur du texte (dans la variable 'longueur') et les deux symboles que nous allons utiliser ('symbole1' et 'symbole2').

Nous commençons ensuite par afficher le premier symbole, multiplié par la longueur de la chaîne de caractère :

    >>> print(symbole1*longueur)
    -------------

Nous passons ensuite avec une boucle for à travers chaque lettre du mot :

    for lettre in texte:

Vient ensuite, la partie un peu plus complexe de l'exercice. Nous utilisons toute la puissance que nous permet la méthode format avec la syntaxe suivante :

    print("{0}{1:^{2}}{0}".format(symbole2, lettre, longueur - 2))

Tout d'abord, nous définissons deux balises au début et à la fin de la chaîne de caractère, représentées par les accolades entourant le 0 : {0}  

Cela nous permet d'afficher la symbole 2 au début et à la fin.


Puis, nous utilisons la syntaxe suivante : 

    {1:^{2}}

Le 1 signifie que l'on insère à l'intérieur de cette accolade le 2e argument passé à la méthode format (la variable 'lettre', donc chaque lettre de notre variable texte, récupérée grâce à la boucle for).

La deuxième partie, avec les deux points et l'accent circonflexe, signifie que l'on veut ajouter un 'padding' avant et après cette lettre : en gros, python va ajouter autant d'espaces que nécessaire avant et après la variable que l'on insère dans l'accolade, afin que le nombre total de caractère soit égal au nombre passé.
Ce nombre, on lui passe grâce à l'accolade qui contient le 2, signifiant que l'on va passer ce nombre comme 3e argument à la méthode format. On passe comme nombre 'longueur - 2', donc la longueur du texte, minus les 2 symboles que l'on place au début et à la fin de la chaîne de caractère (rappelez-vous, les accolades avec le 0) :

    >>> print("{0}{1:^{2}}{0}".format(symbole2, lettre, longueur - 2))
    |     B     |

Ainsi, on s'assure que la longueur totale de la ligne, soit égale à la longueur de la première ligne.

Puis on termine notre script par le même print que pour afficher la première ligne, afin de refermer notre boîte :

    print(symbole1*longueur)
