<div align="center">
    <font size="13" color="red">Structures de données en Python I</font>
    <br>
    <font size="13">Les bases du langage Python</font>
</div>
<br>
L'objectif de ce document est de présenter les concepts de base du langage de programmation Python.

# La notion de variable

Un programme manipule des données. Ce terme de **données**, certes un peu vague, désigne tout ce qui peut être numérisé et stocké dans la mémoire d'une machine, par exemple&nbsp;:

* les nombres (entiers, réels, etc)
* le texte (caractères, mots, documents, etc)
* le multimédia (images, audio, vidéo).

La liste ci-dessus n'est bien sûr pas exhaustive. Pour stocker des données dans la mémoire d'une machine, la technique de base consiste à utiliser dans les programmes des **variables**. Une variable désigne une zone de la mémoire dans laquelle est mémorisée un objet. Elle possède&nbsp;:

* un **nom de variable** qui lui est propre (deux variables ne peuvent avoir le même nom)&nbsp;;
* un **type** qui permet de préciser la nature de l'objet qu'elle contient&nbsp;;
* une **valeur** qui est égale à l'objet qu'elle contient.

On peut donc écrire un programme Python dans lequel on manipule&nbsp;:

* une variable de nom `jour`, de type `chaîne de caractères (string)`, ayant pour valeur l'objet chaîne `'lundi'`&nbsp;;
* une variable de nom `mois`, de type `entier (int)`, ayant pour valeur le nombre (objet) entier `25`.


## Nom de variable

Conformément à ce qui est indiqué dans la PEP 8 (PEP 8 pour Python Extension Proposal est un ensemble de règles visant à homogénéiser le code, et à définir de bonnes pratiques de codage en Python), un nom de variable en Python doit respecter les règles suivantes&nbsp;:

* ne comporter que des lettres minuscules non accentuées, des chiffres ou le caractère "souligné" (ce caractère se situe sur la touche 8 du clavier) pour jouer le rôle de séparateur de mots&nbsp;;
* débuter obligatoirement par une lettre minuscule.

Les noms suivants : `abs`, `ord`, `alti`, `peri1` et `aire_triangle` sont des exemples de noms de variables conformes.

L'utilisation de lettres majuscules pour les noms de variables n'est pas interdit, mais n'est pas recommandé. En particulier parce que la **casse** (En informatique, la casse est la distinction entre les caractères minuscules et majuscules) est bien prise en compte par les interpréteurs Python. Ainsi, `aire`, `Aire` et `AIRE` ne désignent pas tous la même variable, mais trois variables différentes. En fait, les lettres majuscules sont utilisées en Python pour les **constantes**, les noms de **classes** et les **exceptions**. Toutes ces notions ne font toutefois pas partie des bases et ne seront pas abordées dans ce chapitre.

Pour terminer, il faut préciser que le langage Python comprend un certain nombre de **mots réservés**, qui ont une signification bien précise et qui ne peuvent donc être utilisés comme des noms de variables. Le tableau ci-dessous contient la liste de tous ces mots réservés.

![Mots réservés du langage Python](ImagesNotebook/MotsReserves.PNG)

## Valeur d'une variable

### Affectation

L'instruction permettant de stocker un objet dans une variable (on parle aussi de donner une valeur à une variable) s'appelle l'**affectation** ou l'**assignation**. Elle se code de la manière suivante&nbsp;:


```python
nomvariable = unobjet
```

Le signe `=` n'a rien à voir ici avec le test d'égalité couramment utilisé en mathématiques. En langage courant, on pourrait dire que l'affectation ci-dessus permet de stocker l'objet `unobjet` dans la variable `nomvariable`. Après l'instruction d'affectation, la variable référence l'objet qui lui a été affecté. Voici ci-dessous quelques exemples d'affectations&nbsp;:


```python
coef = 5
message = "Hello world !"
valeurPi = 3.14159
```

Que se passe-t-il dans la mémoire de la machine lorsqu'une affectation d'une nouvelle variable est exécutée dans un programme ? On peut identifier quatre étapes&nbsp;:

1. Création d'un nouveau nom de variable dans l'**espace des noms** de la mémoire;
2. Création d'un nouvel objet dans une zone de la mémoire;
3. Attribution d'un type à la nouvelle variable (conforme au type de l'objet précédent);
4. Création d'un lien entre la nouvelle variable et la zone où l'objet est stocké.

Voici de manière très schématique l'état de la mémoire après les trois affectations précédentes&nbsp;:

![Schéma de la mémoire](ImagesNotebook/EtatMemoire.PNG)

### Affectation multiple

On peut affecter le même objet à plusieurs variables en une seule instruction. On parle alors d'**affectation multiple**. Voici ci-dessous un exemple d'affectation multiple&nbsp;:


```python
longueur = largeur = 6.5
```

![Exemple d'affectation multiple](ImagesNotebook/AffectationMultiple.PNG)

### Affectations parallèles

Il est possible également d'affecter des objets différents à plusieurs variables dans la même instruction. On parle alors d'**affectations parallèles**. Voici un exemple d'affectations parallèles&nbsp;:


```python
coefA, coefB, coefC = 5, 1, 2.4
```

![Exemple d'affectation multiple](ImagesNotebook/AffectationsParalleles.PNG)

## Les différents types d'objets

Il existe de nombreux types d'objets pouvant être manipulés dans des programmes Python. On ne parlera dans cette section que des types d'objets simples. D'autres types d'objets plus complexes, comme par exemple les listes ou les dictionnaires, seront abordés dans un chapitre ultérieur.

### Les types numériques

* **entier** (`int` en Python, par exemple : `5`)
* **réel** ou à « virgule flottante » (`float` en Python, par exemple : `6.41`)

### Les types alphanumériques (pour les données textuelles)

* **chaîne** (`str` en Python, par exemple : `"Bonjour"`)

Une chaîne est une suite de caractères quelconque entourée soit de guillemets ou doubles quotes (par exemple : `"Hello !"`), soit d'apostrophes ou simples quotes (par exemple : `'Python 3.10'`).

### Les booléens

* `bool`

Un booléen est un objet dont la valeur est soit **Vrai** (`True`), soit **Faux** (`False`). Les booléens sont particulièrement utilisés lors de la manipulations d'**expressions conditionnelles**. Nous y reviendrons dans un cours ultérieur.

## Le typage dynamique

En Python, le type d'une variable est déterminé lors de l'exécution du programme, en fonction de l'objet qu'elle référence. Dans les exemples précédents, `coef`, `coefA` et `coefB` sont des entiers, `valeurPi`, `longueur`, `largeur` et `coefC` sont des réels, `message` est une chaîne. De plus, ce typage est **dynamique**. Cela signifie que le type de l'objet référencé par une variable peut changer au cours du programme, et que le type de la variable s'adapte. Ainsi, une même variable pourra contenir un entier, puis un réel et enfin une chaîne sans que cela pose problème. La fonction `type()` permet de connaître le type d'une variable. Le programme ci-dessous illustre ce typage dynamique des variables&nbsp;:


```python
# Une variable maVar dont le type varie dans le programme.
# D'abord un entier

maVar = 18

# Vérification avec l'affichage de son type

print(type(maVar))

# Puis un réel

maVar = 5.21
print(type(maVar))

# Et enfin une chaîne

maVar = "Il est 17h56."
print(type(maVar))

```

    <class 'int'>
    <class 'float'>
    <class 'str'>
    

## Opérateurs et expressions

Les variables peuvent être utilisées dans des **expressions** de calcul contenant des **opérateurs**. 

### Évaluation d'une expression

Pour évaluer une expression, l'interpréteur remplace chaque variable par l'objet qu'elle référence. Considérons par exemple le programme suivant&nbsp;:


```python
pi = 3.14159
rayon = 6
airecercle = pi * (rayon ** 2)
print("La valeur de l'aire du cercle est : ", airecercle)
```

    La valeur de l'aire du cercle est :  113.09724
    

La variable `pi` est de type réel et sa valeur est `3.14159`. La variable `rayon` est de type entier et sa valeur est `6`. Pour déterminer la valeur de la variable `airecercle`, il faut évaluer l'expression `pi * (rayon ** 2)`. Pour évaluer cette expression, l'interpréteur remplace les variables par les objets qu'elles référencent. L'expression devient alors `3.14159 * (6 ** 2)` et son résultat est `113.09724` (`*` est l'opérateur de la multiplication et `**` celui de l'élévation à une puissance). La valeur de la variable `airecercle` est donc `113.09724` et son type est réel.

![Etat de la mémoire](ImagesNotebook/EtatMemoire2.PNG)

### Les principaux opérateurs arithmétiques

Voici comment sont codés les principaux opérateurs de l'arithmétique en langage Python&nbsp;:

* addition : `+`. Par exemple, `5 + 6` dont le résultat est `11`.
* soustraction : `-`. Par exemple, `5 - 6` dont le résultat est `-1`.
* multiplication : `*`. Par exemple, `5 * 6` dont le résultat est `30`.
* division : `/`. Par exemple, `5 / 6` dont le résultat est `0.8333333333...`.
* quotient de la division entière : `//`. Par exemple, `18 // 4` dont le résultat est `4`.
* reste de la division entière (ou modulo) : `%`. Par exemple, `18 % 4` dont le résultat est `2`.
* puissance : `**`. Par exemple, `2 ** 3` dont le résultat est `8`.

Les règles de priorité usuelles en arithmétique s'appliquent de la même façon dans un programme Python. Les expressions sont donc évaluées en respectant l'ordre suivant&nbsp;:

1. les expressions entre parenthèses (dans n'importe quel ordre)
2. les exposants (puissances)
3. les multiplications et divisions
4. les additions et soustractions

Lorsque deux opérateurs ont le même niveau de priorité, l'évaluation s'effectue de gauche à droite.

## Objets « muable » vs. objets « immuables »

Dans un programme Python, les données manipulées sont des objets. Certains objets sont modifiables. On parle alors d'objets **« muables »** (**« mutable »** en anglais). Les **listes**, **dictionnaires** et **ensembles** sont des exemples d'objets muables (ils feront l'objet d'un cours ultérieur et ne sont pas abordés pour le moment). À l'inverse, d'autres objets ne peuvent être modifiés. On parle alors d'objets **immuables** (**« immutable »** en anglais). C'est le cas notamment de tous les entiers, réels, chaînes et booléens. Pour modifier la valeur d'une variable référençant un objet immuable, il faut lui affecter un nouvel objet, faute de pouvoir modifier celui qu'elle référence. Le programme ci-dessous est un exemple de modification de la valeur d'une variable par une affectation&nbsp;:


```python
coef = 5
print("Valeur de coef après la première affectation : ", coef)
coef = 6
print("Valeur de coef après la seconde affectation : ", coef)
```

    Valeur de coef après la première affectation :  5
    Valeur de coef après la seconde affectation :  6
    

Une première affectation donne la valeur entière `5` à la variable `coef`. La variable `coef` est donc de type entier. Ce type entier étant immuable, le changement de valeur de `coef` s'effectue grâce à la seconde affectation, qui donne à `coef` la valeur `6`. Les deux affichages avec l'instruction `print()` permettent de confirmer ce changement de valeur. Que se passe-t-il dans la mémoire lors de ces deux affectations ? Cela peut être schématisé comme indiqué ci-dessous&nbsp;:

![Objet immuable](ImagesNotebook/ObjetImmuable.PNG)

La première affectation ajoute la variable `coef` en mémoire&nbsp;: ajout du nom `coef` dans l'espace des noms, ajout d'un nouvel objet entier `5` puis création d'un lien entre le nom `coef` et l'objet `5`. Lors de la seconde affectation, un nouvel objet entier `6` est ajouté, le lien précédent est supprimé et remplacé par un lien entre le nom `coef` et l'objet `6`. L'objet `5` n'est alors plus référencé par une variable (aucune variable ne lui est relié). Il est donc supprimé de la mémoire grâce à un mécanisme appelé **« ramasse-miettes »** (**« garbage collector »** en anglais).

On peut également comprendre ce qui se passe grâce au programme suivant&nbsp;: 


```python
coef = 5
print("Adresse de l'objet référencé par la variable coef : ", id(coef))
coef = 6
print("Adresse de l'objet référencé par la variable coef : ", id(coef))
```

    Adresse de l'objet référencé par la variable coef :  1620036708784
    Adresse de l'objet référencé par la variable coef :  1620036708816
    

Après chaque affectation, l'instruction `print("Adresse de l'objet référencé par la variable coef : ", id(coef))` permet d'afficher l'adresse en mémoire de l'objet référencé par la variable `coef`. Cette adresse est différente après la seconde affectation, ce qui montre que cette seconde affectation n'a pas modifié l'objet `5` (qui est un entier, donc immuable) mais a modifié l'objet référencé par `coef` qui est désormais `6`.

Le cas des objets muables est bien différent puisque ceux-ci sont modifiables. Comme il a été précisé plus haut, les objets muables tels que les listes et les dictionna ires feront l'objet d'un autre cours. Considérons néanmoins le programme suivant&nbsp;:


```python
maListe = [1, 2, 3, 4]
print("La valeur de la variable maListe est : ", maListe)
maListe.append(5)
print("La valeur de la variable maListe est : ", maListe)
```

    La valeur de la variable maListe est :  [1, 2, 3, 4]
    La valeur de la variable maListe est :  [1, 2, 3, 4, 5]
    

Ce qui se passe lors de l'exécution de ce programme peut se schématiser de la manière suivante&nbsp;:

![Objet muable](ImagesNotebook/ObjetMuable.PNG)

Une première affectation `maListe = [1, 2, 3, 4]` permet d'affecter à la variable `maListe` un **objet liste**, composé de plusieurs objets entiers `[1, 2, 3, 4]`. Puis l'instruction `maListe.append(5)` ajoute un nouvel élément `5` à l'objet liste référencé par `maListe` (ce qui est tout à fait possible puisq'un objet liste est muable). Les instructions d'affichage permettent de confirmer que la valeur de la variable `maListe` a bien été modifiée, puisque l'objet qu'elle référence a été modifié. Notons que cette modification n'a pas nécessité de seconde affectation. C'est l'objet référencé qui a été modifié directement. Aucun nouvel objet n'a été créé et le lien variable/objet n'a pas été modifié. Cette constatation peut se vérifier à l'aide du programme suivant&nbsp;:


```python
maListe = [1, 2, 3, 4]
print("Adresse de l'objet référencé par la variable maListe : ", id(maListe))
maListe.append(5)
print("Adresse de l'objet référencé par la variable maListe : ", id(maListe))
```

    Adresse de l'objet référencé par la variable maListe :  1994930698560
    Adresse de l'objet référencé par la variable maListe :  1994930698560
    

L'adresse de l'objet référencé par la variable `maListe` est la même après les deux instructions. La modification a donc impacté directement l'objet liste référencé par `maListe`.
Pour résumer la différence entre objet immuable et objet muable, on peut dire que&nbsp;:

* pour modifier la valeur d'une variable contenant un objet immuable, il faut impérativement lui affecter un nouvel objet;
* la valeur d'une variable contenant un objet muable se modifie en modifiant directement l'objet.

## Le « ramasse-miettes »

Le « ramasse-miettes », également appelé « récupérateur de mémoire » ou « glaneur de cellules » (« garbage collector » en anglais), est un processus visant à optimiser la mémoire de la machine lors de l'exécution d'un programme. Plus concrètement, au fil de l'exécution d'un programme, le ramasse-miettes détecte les objets de la mémoire non utilisés (c'est-à-dire, non référencés par des variables) et libère l'espace mémoire occupé par ces objets. De nombreux environnements de programmation possèdent un ramasse-miettes.

# La notion de fonction

Dans cette section, nous présentons brièvement la notion de fonction et nous présentons quelques fonctions usuelles du langage Python. Les fonctions feront l'objet d'un cours ultérieur plus détaillé.
Dans un programme, une **fonction** réalise une tâche particulière. Elle est définie une seule fois, mais exécutée autant de fois que nécessaire. Par exemple&nbsp;:

* `print()` affiche des informations à l'écran
* `input()` permet à l'utilisateur de saisir des données à l'aide du clavier
* `sqrt()` calcule la racine carrée d'un nombre
* `sin()` calcule le sinus d'un angle.

De manière générale, il existe trois catégories de fonctions dans les langages de programmation&nbsp;:

* les **fonctions natives**, qui sont intégrées au langage et donc toujours utilisables
* les fonctions définies dans des **modules** externes, qu'il faut importer pour pouvoir les utiliser
* les fonctions **propres au programmeur** que celui-ci définit dans ses programmes.

Le programme ci-dessous calcule la longueur de l'hypothénuse d'un triangle rectangle, à partir de celles des deux côtés de l'angle droit. Il contient des exemples de chaque catégorie de fonctions.


```python
from math import sqrt

# Définition d'une fonction calculant la longueur de l'hypothénuse d'un triangle rectangle
# à partir des longueurs des 2 côtés de l'angle droit
def calculer_long_hyp(longc1, longc2):
    return(sqrt(longc1**2 + longc2**2))

# Saisie des données au clavier (les longueurs des 2 côtés de l'angle droit)
print("Saisissez la longueur du premier côté de l'angle droit : ")
longc1 = float(input())
print("Saisissez la longueur du second côté de l'angle droit : ")
longc2 = float(input())

# Calcul de la longueur de l'hypothénuse
long_hyp = calculer_long_hyp(longc1, longc2)

# Affichage du résultat
print("La longueur de l'hypothénuse est : ",long_hyp)
```

    Saisissez la longueur du premier côté de l'angle droit : 
    

     5
    

    Saisissez la longueur du second côté de l'angle droit : 
    

     6
    

    La longueur de l'hypothénuse est :  7.810249675906654
    

Les fonctions `float()`, `print()` et `input()` sont des fonctions natives de Python. Elles sont exécutées plusieurs fois. Nous les aborderons plus en détails plus loin dans ce cours. La fonction `sqrt()` est définie dans le module `math` de Python. Elle est importée au début du programme avec l'instruction `from math import sqrt`. La fonction `calculer_long_hyp()` est définie par le programmeur au début du programme avec le mot-réservé `def`. Elle utilise dans sa définition la fonction importée `sqrt()`. Elle est ensuite exécutée dans l'instruction `long_hyp = calculer_long_hyp(longc1, longc2)`. 

Pour exécuter sa tâche, une fonction peut nécessiter (ou pas !) qu'on lui fournisse des données. Ces données qui sont fournies à une fonction sont appelées ses **paramètres** ou **arguments**. Il sont indiqués dans un jeu de parenthèses après le nom de la fonction et peuvent être&nbsp;:

* des objets
* des variables
* des expressions

Par exemple, dans l'instruction `print("Saisissez la longueur du premier côté de l'angle droit : ")`, l'objet chaîne `"Saisissez la longueur du premier côté de l'angle droit : "` est fournie en paramètre de la fonction `print()` dont la tâche consiste à l'afficher à l'écran. Dans l'instruction `sqrt(a*2)`, le résultat de l'expression `a*2` est évalué puis fourni en paramètre de ma fonction `sqrt()` afin qu'elle en calcule la racine carrée.

À partir des données qu'on lui fournit en paramètres, une fonction effectue sa tâche et retourne (ou pas !) un résultat (on parle aussi de **valeur de retour** d'une fonction). Pour être exploités ultérieurement dans un programme, les résultats retournés par les fonctions doivent être stockés dans des variables. La fonction `sqrt()` retourne la racine carrée d'un nombre fourni en paramètre. Dans l'instruction `racine = sqrt(nb)`, la valeur de la variable `nb` est fournie en paramètre. Puis le résultat retourné par la fonction est stocké dans la variable `racine`. Le résultat d'une fonction peut être utilisé dans une expression de calcul, comme par exemple dans l'instruction `b = sqrt(a)+sqrt(c)`. Il peut aussi être fourni comme paramètre d'une autre fonction. On parle alors de **composition de fonctions**. L'instruction `float(input())` est un exemple de composition de fonctions : le résultat de la fonction `input()` est donné en paramètre de la fonction `float()`.

## La fonction `print()` - Affichage d'informations à l'écran

La fonction `print()` affiche à l'écran les paramètres qu'on lui fournit (dans le jeu de parenthèses, séparés par des virgules). Un paramètre peut être&nbsp;: un objet, une variable, une expression ou une composition de fonctions. À l'écran, les valeurs des paramètres sont affichées dans le même ordre que celui où ils sont fournis, avec un espace de séparation entre chaque valeur. Par défaut, l'affichage se termine par un passage à la ligne suivante. Voici ci-dessous un exemple de programme Python affichant à l'écran la date du jour sous la forme « jj / mm / aa ».


```python
from datetime import *

aujourdhui = date.today()

print("Bonjour ! Aujourd'hui nous sommes le", aujourdhui.day, "/", aujourdhui.month, "/", aujourdhui.year, ".")
```

    Bonjour ! Aujourd'hui nous sommes le 13 / 10 / 2022 .
    

### Affichage formaté avec les **f-strings**

Depuis la version 3.6 de Python, la fonction `print()` peut être exécutée avec un seul paramètre de type `f-string`. `f-string` est l'abbréviation de « formatted string litteral », autrement dit « chaîne formatée ». Une `f-string`&nbsp;:

* se code comme une chaîne précédée du caractère « f » (sans espace), par exemple : `f"Ceci est une f-string."`
* peut contenir des variables, expressions ou exécutions de fonctions entre accolades. Dans ce cas, celles-ci seront remplacées par leurs valeurs respectives lors de l'affichage. Par exemple, `f"Ceci est une f-string contenant deux variables : {var1} et {var2}."`
* une variable, expression ou exécution de fonction contenue dans une `f-string` peut être accompagnée de son format d'affichage. Ceci est particulièrement utile pour l'affichage des données numériques. Par exemple, `f"Cette f-string affiche le nombre réel {mynb:.2f} avec 2 décimales seulement."` est une `f-string` où la valeur de `mynb` sera affichée avec deux chiffres décimaux seulement.
Voici une seconde version du programme de calcul de l'hypothénuse, où l'instruction `print()` finale s'effectue avec une `f-string` en paramètre afin d'afficher le résultat avec uniquement 3 chiffres décimaux.


```python
from math import sqrt

# Définition d'une fonction calculant la longueur de l'hypothénuse d'un triangle rectangle
# à partir des longueurs des 2 côtés de l'angle droit
def calculer_long_hyp(longc1, longc2):
    return(sqrt(longc1**2 + longc2**2))

# Saisie des données au clavier (les longueurs des 2 côtés de l'angle droit)
print("Saisissez la longueur du premier côté de l'angle droit : ")
longc1 = float(input())
print("Saisissez la longueur du second côté de l'angle droit : ")
longc2 = float(input())

# Calcul de la longueur de l'hypothénuse
long_hyp = calculer_long_hyp(longc1, longc2)

# Affichage du résultat
print(f"La longueur de l'hypothénuse est : {long_hyp:.3f}.")
```

    Saisissez la longueur du premier côté de l'angle droit : 
    

     9
    

    Saisissez la longueur du second côté de l'angle droit : 
    

     4
    

    La longueur de l'hypothénuse est : 9.849.
    

## La fonction `input()` - Saisie de données au clavier

L'exécution de la fonction `input()` provoque une interruption du programme, afin de permettre à l'utilisateur de saisir des données au clavier. Celui-ci saisit ses données, puis marque la fin de la saisie en appuyant sur la touche `ENTRÉE`. L'exécution du programme peut alors reprendre là où elle s'est interrompue. Le résultat de la fonction `input()` est une **chaîne** (`str`) contenant tous les caractères saisis au clavier par l'utilisateur. Il est possible de fournir une chaîne en paramètre de la fonction, par exemple : `input("Saisissez un nombre :")`. Dans ce cas, cette chaîne sera affichée à l'écran avant l'interruption pour la saisie au clavier.
Dans le programme suivant, la première instruction affiche la chaîne `"Saisissez des données au clavier :"`, saisit des données au clavier et les stocke dans une variable `ch`. La seconde instruction affiche le type de `ch` ainsi que sa valeur. Testez ce programme plusieurs fois avec des données différentes (mot, phrase, nombre entier, nombre réel). Quel est le type qui s'affiche, quelle que soit la donnée saisie ? Qu'en déduisez-vous sur le résultat retourné par `input()`.


```python
ch = input("Saisissez des données au clavier :")
print(f"Le type de la variable ch est {type(ch)} et sa valeur est {ch}.")
```

    Saisissez des données au clavier : 56
    

    Le type de la variable ch est <class 'str'> et sa valeur est 56.
    

Si vous avez testé le programme précédent, vous avez pu constater que le résultat de la fonction `input()` est toujours la **chaîne** contenant les caractères saisis. En effet, si vous saisissez les caractères `ABCDE`, la fonction retourne la chaîne `"ABCDE"`. De la même manière, si vous saisissez `987`, la fonction retourne la chaîne `"987"`. Comment faire pour que les données saisies soient utilisées dans le programme comme des nombres et non comme des chaînes ? Il faut utiliser les fonctions de conversion telles que `int()` et `float()`. Ces fonctions prennent en paramètre un objet, convertissent cet objet respectivement en un entier ou un réel, puis retournent le résultat (entier ou réel). Par exemple, `int("53")` retourne l'entier `53` et `float("3.14159")` retourne le réel `3.14159`. L'objet passé en paramètre doit bien sûr être compatible avec la conversion demandée, sous peine de provoquer une erreur à l'exécution. Ainsi, `int("Coucou")` et `int(3.62)` ne peuvent s'exécuter correctement puisque ni la chaîne `"Coucou"` ni le réel `3.62` ne peuvent être convertis en entiers. Le programme suivant utilise ces fonctions pour convertir les données saisies par l'utilisateur.


```python
lachaine = input("Saisissez une phrase au clavier.")
lentier = int(input("Saisissez un nombre entier au clavier."))
lereel = float(input("Saisissez un nombre réel au clavier."))

print(f"La valeur de la variable lachaine est {lachaine} et son type est {type(lachaine)}.")
print(f"La valeur de la variable lentier est {lentier} et son type est {type(lentier)}.")
print(f"La valeur de la variable lachaine est {lereel} et son type est {type(lereel)}.")
```

    Saisissez une phrase au clavier. Il pleut
    Saisissez un nombre entier au clavier. 84364
    Saisissez un nombre réel au clavier. 5.47
    

    La valeur de la variable lachaine est Il pleut et son type est <class 'str'>.
    La valeur de la variable lentier est 84364 et son type est <class 'int'>.
    La valeur de la variable lachaine est 5.47 et son type est <class 'float'>.
    

Pour terminer, notons qu'il existe d'autre fonctions telles que `str()` et `bool()` pour convertir des objets respectivement en chaînes et en booléens.

# Manipulation de chaînes

Pour terminer ce chapitre sur les notions de base du langage Python, voici quelques manipulations simples sur les chaînes de caractères.

## Notion de séquence et indiçage des caractères

En Python, une chaîne est considérée comme une **séquence**, c'est-à-dire une **suite ordonnée d'objets** (ordonnée au sens où chaque caractère occupe une place bien précise dans la chaîne). De ce fait, chaque caractère d'une chaîne est repéré par son **indice** dans la chaîne, l'indiçage s'effectuant à partir de 0 (en informatique, tout commence par le 0 !). Par exemple, la chaîne `"Programmation"` comporte 13 caractères. Le caractère d'indice `0` est `"P"`, celui d'indice `1` est `"r"`, celui d'indice `2` est `"o"`, etc. Le dernier caractère est `"n"` et il se trouve à l'indice `12`. De manière générale, une chaîne de longueur `n` (la longueur correspond au nombre de caractères de la chaîne) comporte des caractères indicés de `0` à `n-1`.

## Référencement d'un caractère

Pour référencer un caractère dans une chaîne, la notation consiste à indiquer le nom de la variable contenant la chaîne, suivie entre crochets de l'indice du caractère référencé. Par exemple, `maVarChaine[ind]` référence le caractère situé à l'indice `ind` dans la chaîne contenue dans la variable `maVarChaine`. `ind` doit obligatoirement être un entier ou une variable entière, et sa valeur ne doit pas dépasser celle de la longueur de la chaîne - 1. En effet, référencer un caractère situé à l'indice `10` dans une chaîne ne comportant que 5 caractères provoque une erreur. Le programme suivant illustre le référencement de caractères.


```python
maVarChaine = "Programmation"
print(f"Le caractère situé à l'indice 0 est : {maVarChaine[0]}")
print(f"Le caractère situé à l'indice 3 est : {maVarChaine[3]}")
print(f"Le caractère situé à l'indice 5 est : {maVarChaine[5]}")
print(f"Le caractère situé à l'indice 13 est : {maVarChaine[13]}")
```

    Le caractère situé à l'indice 0 est : P
    Le caractère situé à l'indice 3 est : g
    Le caractère situé à l'indice 5 est : a
    


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    Input In [2], in <cell line: 5>()
          3 print(f"Le caractère situé à l'indice 3 est : {maVarChaine[3]}")
          4 print(f"Le caractère situé à l'indice 5 est : {maVarChaine[5]}")
    ----> 5 print(f"Le caractère situé à l'indice 13 est : {maVarChaine[13]}")
    

    IndexError: string index out of range


Il est possible d'utiliser comme indice un nombre entier négatif. Dans ce cas, le référencement s'effectue à partir de la fin de la chaîne (et non pas du début comme ci-dessus). Le caractère d'indice `-1` est alors le dernier caractère de la chaîne, celui d'indice `-2` l'avant-dernier, et ainsi de suite. Voici des exemples d'utilisation d'indices négatifs. 


```python
maVarChaine = "Programmation"
print(f"Le caractère situé à l'indice -1 est : {maVarChaine[-1]}")
print(f"Le caractère situé à l'indice -3 est : {maVarChaine[-3]}")
print(f"Le caractère situé à l'indice -10 est : {maVarChaine[-10]}")
print(f"Le caractère situé à l'indice -13 est : {maVarChaine[-13]}")
print(f"Le caractère situé à l'indice -14 est : {maVarChaine[-14]}")
```

    Le caractère situé à l'indice -1 est : n
    Le caractère situé à l'indice -3 est : i
    Le caractère situé à l'indice -10 est : g
    Le caractère situé à l'indice -13 est : P
    


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    Input In [2], in <cell line: 6>()
          4 print(f"Le caractère situé à l'indice -10 est : {maVarChaine[-10]}")
          5 print(f"Le caractère situé à l'indice -13 est : {maVarChaine[-13]}")
    ----> 6 print(f"Le caractère situé à l'indice -14 est : {maVarChaine[-14]}")
    

    IndexError: string index out of range


## Référencement d'une sous-chaîne (« slicing »)

Une **sous-chaîne** est une partie spécifique d'une chaîne. Le **« slicing »** consiste à référencer une sous-chaîne et la forme générale de sa notation est `maVarChaine[prem:der]` où :

* `maVarChaine` est la variable contenant la chaîne
* `prem` est l'indice du premier caractère de la sous-chaîne
* `der` est l'indice du dernier caractère de la chaîne ne figurant pas dans la sous-chaîne

La notation `maVarChaine[prem:der]` référence donc la sous-chaine contenue dans `maVarChaine` qui débute au caractère d'indice `prem` et se termine au caractère d'indice `der-1`. Par exemple :


```python
print(f"Premier exemple de slicing : {maVarChaine[2:6]}")
print(f"Deuxième exemple de slicing : {maVarChaine[1:4]}")
```

    Premier exemple de slicing : ogra
    Deuxième exemple de slicing : rog
    

Lorsque les indices `prem` et `der` sont négatifs, le référencement débute à partir de la fin de la chaîne. Par exemple :


```python
print(f"Troisième exemple de slicing : {maVarChaine[-5:-2]}")
```

    Troisième exemple de slicing : ati
    

L'indice `prem` peut être omis. Dans ce cas, le référencement s'effectue à partir du premier caractère de la chaîne jusqu'au caractère d'indice `der-1`. Par exemple :


```python
print(f"Quatrième exemple de slicing : {maVarChaine[:3]}")
```

    Troisième exemple de slicing : Pro
    

De la même façon, l'indice `der` peut être omis. Dans ce cas, le référencement s'effectue à partir du caractère d'indice `prem` jusqu'au dernier caractère de la chaîne. Par exemple :


```python
print(f"Cinquième exemple de slicing : {maVarChaine[3:]}")
```

    Quatrième exemple de slicing : grammation
    

## Opérateurs et fonctions usuelles sur les chaînes

Il existe deux opérateurs usuels sur les chaînes : la **concaténation** et la **répétition**.

### La concaténation

La concaténation permet de construire une chaîne en mettant bout à bout deux ou plusieurs chaînes existantes. Elle est une sorte d'addition de chaînes. Elle se note d'ailleurs avec le signe `+`. Par exemple :


```python
ch1 = " en Python"
ch2 = " à Rennes 2."
chConc = maVarChaine + ch1 + ch2
print(f"Chaîne obtenue par concaténation : {chConc}")
```

    Chaîne obtenue par concaténation : Programmation en Python à Rennes 2.
    

### La répétition

La répétition permet de construire une chaîne en répétant plusieurs fois une chaîne existante. Elle est une sorte de multiplication de chaînes. Elle se note d'ailleurs avec le signe `*`. Par exemple :


```python
chMult = maVarChaine * 5
print(f"Chaîne obtenue par multiplication : {chMult}")
```

    Chaîne obtenue par multiplication : ProgrammationProgrammationProgrammationProgrammationProgrammation
    

### Longueur d'une chaîne

La fonction `len` prend en paramètre une chaîne et retourne sa longueur, c'est-à-dire son nombre de caractères. Par exemple :


```python
print(f"La chaîne {chMult} contient {len(chMult)} caractères.")
print(f"La chaîne 'L1 MIASHS' contient {len('L1MIASHS')} caractères.")
```

    La chaîne ProgrammationProgrammationProgrammationProgrammationProgrammation contient 65 caractères.
    La chaîne 'L1 MIASHS' contient 8 caractères.
    

### Indice d'un caractère dans une chaîne

Les chaînes sont des objets sur lesquels il est possible d'appliquer des **méthodes** qui vont retourner des résultats. Syntaxiquement, l'application d'une méthode à un objet s'effectue avec l'instruction `Obj.NomMeth(listepara)` où :

* `Obj` est l'objet ou le nom de la variable référençant l'objet
* `NomMeth` est le nom de la méthode à appliquer sur l'objet
* `listepara` est la liste des paramètres fournis à la méthode (séparés par des virgules).

La notion de méthode est proche de celle de fonction, et sera vue plus en détails en licence 2. En Python, il existe de nombreuses méthodes prédéfinies pour les différents types d'objets. Parmi les méthodes qui s'appliquent aux chaînes, la méthode `index` prend en paramètre un caractère et retourne l'indice de la première occurrence de ce caractère dans la chaîne. Par exemple :


```python
uneChaine = "Ce matin, je me suis levée de bonne heure."
print(f"Le premier caractère 'a' est situé à l'indice {uneChaine.index('a')} dans la chaîne.")
print(f"Le premier caractère 'u' est situé à l'indice {uneChaine.index('u')} dans la chaîne.")
```

    Le premier caractère 'a' est situé à l'indice 4 dans la chaîne.
    Le premier caractère 'u' est situé à l'indice 17 dans la chaîne.
    

Lorsque le caractère fourni en paramètre ne figure pas dans la chaîne, une erreur se produit :


```python
print(f"Le premier caractère 'w' est situé à l'indice {uneChaine.index('w')} dans la chaîne.")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Input In [16], in <cell line: 1>()
    ----> 1 print(f"Le premier caractère 'w' est situé à l'indice {uneChaine.index('w')} dans la chaîne.")
    

    ValueError: substring not found


## Test d'appartenance d'un caractère à une chaîne

En Python, il existe une structure conditionnelle `if` permettant de tester si un caractère appartient ou pas à une chaîne. Un bloc d'instructions différent est ensuite exécuté en fonction de l'appartenance ou non du caractère à la chaîne. Sa syntaxe est la suivante :
if car in ch:
    bloc 1
else:
    bloc 2
où :
* `car` est un caractère ou une variable référençant un caractère
* `ch` est une chaîne ou une variable référençant une chaîne
Par exemple :


```python
voyelles = "aeiouyAEIOUY"
MyCar = input("Saisissez un caractère :")
if MyCar in voyelles:
    print(f"Le caractère {MyCar} est une voyelle.")
else:
    print(f"Le caractère {MyCar} n'est pas une voyelle.")
```

    Saisissez un caractère : k
    

    Le caractère k n'est pas une voyelle.
    
