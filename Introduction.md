<div align="center">
    <font size="13" color="red">Structures de données en Python I</font>
    <br>
    <font size="13">Introduction</font>
</div>

# Objectifs

Ce cours est la continuité du cours de **« Culture Numérique et Programmation »** du semestre 1. La réflexion algorithmique en reste l'un des objectifs, mais nous y ajoutons en plus l'apprentissage de la syntaxe et des concepts de base de la programmation en langage Python. Tous les documents nécessaires (PDF des cours et des sujets de travaux dirigés, corrigés des programmes demandés) sont téléchargeables à partir de l'**espace-cours Cursus « Structures de données en Python I »** : https://cursus.univ-rennes2.fr/course/view.php?id=5679.

# Modalités pédagogiques

Le cours est composé essentiellement de séances de Travaux Dirigés, à raison de deux heures par semaine. Quatre intervenants assureront les TDs :

* Haïscam ABDALLAH
* Xavier ANDRÉ
* Emmanuelle MARTIENNE
* Fabienne MOREAU

L'évaluation du cours s'effectue à l'aide de deux contrôles continus (deux épreuves individuelles sur machine d'une durée d'une heure), comptant chacun pour 50% de la note finale.

# Bibliographie - Webographie

* **Apprendre à programmer avec Python 3** - G. Swinnen - _Éditions Eyrolles_ (version PDF disponible dans l'espace-cours Cursus mentionné plus haut). 
* **Page Wikipédia sur Python** - https://fr.wikipedia.org/wiki/Python_(langage)
* **Page Wikipédia sur la programmation informatique** - https://fr.wikipedia.org/wiki/Programmation_informatique

# Qu'est-ce que la programmation ?

## Définition

On peut définir la programmation comme une activité destinée à faire réaliser par un ordinateur une tâche qu'il n'était pas en mesure d'accomplir auparavant. Plus concrètement, elle consiste à **coder des programmes** que l'ordinateur sera capable d'exécuter, à l'aide d'un **langage de programmation**. La programmation occupe une part très importante dans tout le processus de développement des logiciels informatiques.

## Exemple de tâche simple

On considère par exemple une tâche assez qu'il est possible d'effectuer avec juste un crayon, une feuille de papier... et le souvenir de ses leçons de mathématiques du lycée : le calcul des racines réelles d'une équation du second degré à une inconnue de la forme : $ax^2+bx+c=0$. Pour automatiser cette tâche à l'aide d'un ordinateur et d'un programme, quatre étapes sont nécessaires&nbsp;:

* la conception ;
* le codage ;
* la compilation ou l'interprétation du programme source ;
* le test du programme source.

# Les étapes de la mise au point d'un programme

## La conception

La conception est une analyse préalable, sur papier, du programme que l'on souhaite écrire. Cela suppose de se poser, et aussi de répondre, à un certain nombre de questions de manière non ambigüe. Voici pêle-mêle quelques exemples de ces questions (la liste n'est pas exhaustive !).


À l'origine d'un programme, il y généralement les données qu'il va traiter, qui sont souvent appelées les **entrées**. Quelles sont ces entrées ? Dans quel format se présentent-elles ? Comment sont-elles fournies au programme (saisie au clavier, lecture dans un ou plusieurs fichiers) ?


Un programme traite des données pour produire des résultats, aussi appelés **sorties**. Quelles sont ces sorties ? Dans quel format se présentent-elles ? Comment sont-elles fournies à l'utilisateur (affichage à l'écran ou création de fichier) ?


Une fois les entrées et sorties clairement formalisées, vient la question centrale : comment le programme va-t-il produire les sorties à partir des entrées ? Répondre à cette question consiste à écrire un **algorithme**, c'est-à-dire une suite d'actions, que l'ordinateur doit réaliser séquentiellement pour obtenir les sorties à partir des entrées. À titre de comparaison avec la vie quotidienne, un algorithme en informatique est équivalent à une recette de cuisine. Les entrées sont les ingrédients, les sorties sont le plat à confectionner, et la recette (l'algorithme) vous indique pas à pas comment mélanger les ingrédients (les entrées) pour obtenir le plat (les sorties).

Voici ci-dessous un document qui pourrait tout à fait être le résultat de la phase de conception de notre programme de calcul des racines d'une équation.


```python
## Entrées : trois variables réelles correspondant aux coefficients
#            de l'équation. 
#            Les valeurs de ces variables sont saisies au clavier.
#            - coeff_a est la valeur du coefficient a
#            - coeff_b est la valeur du coefficient b
#            - coeff_c est la valeur du coefficient c
#            Aucun contrôle de validité n'est effectué sur les valeurs
#            saisies au clavier.
## Sorties : deux (une) variable(s) réelle(s) correspondant aux racines 
#            (à la racine unique) de l'équation si elle(s) existe(nt).
#            Les valeurs de ces variables sont affichées à l'écran.
#            - racine1 est la valeur de la première racine
#              (ou de la racine unique selon le cas
#            - racine2 est la valeur de la seconde racine
#            si l'équation n'admet aucune racine réelle, un message
#            l'indiquant est affiché à l'écran.
# Autres données calculées dans le programme :
#            - variable réelle delta contenant la valeur du discriminant
#              de l'équation.

# Algorithme (séquence d'instructions à réaliser)

    Afficher à l'écran le message : 
    " Saisissez au clavier les valeurs des 3 coefficients de l'équation : "
    Saisir au clavier la valeur de coeff_a
    Saisir au clavier la valeur de coeff_b
    Saisir au clavier la valeur de coeff_c
    Calculer la valeur du discriminant delta
    Si (delta <= 0)
        alors Si (delta > 0)
                    alors calculer les valeurs des 2 racines racine1 et racine2
                          afficher à l'écran les valeurs de racine1 et racine2
                    sinon calculer la valeur de la racine unique racine1
                          afficher la valeur de racine1
        sinon afficher à l'écran un message indiquant qu'il n'y a aucune racine
```

## Le codage

L'étape de codage consiste à traduire l'algorithme résultant de la phase de conception en un **programme source**, codé dans un langage de programmation. Voici ci-dessous le programme source obtenu en traduisant l'algorithme précédent en langage Python.

![Programme source en langage Python calculant les racines réelles d'une équation du second degré à une seule inconnue](ImagesNotebook/equation.PNG)

Même si le langage de programmation est généralement de haut niveau et donc non compréhensible directement par un ordinateur, cette étape est un pas de plus vers l'exécution de l'algorithme par la machine. 

## La transformation du programme source

La transformation du programme source consiste à rendre ce dernier exécutable par l'ordinateur. Pour ce faire, il existe deux techniques&nbsp;:

* la compilation
* l'interprétation.

### La compilation

Le principe de la compilation est d'utiliser un programme spécifique, appelé **compilateur**, pour transformer un programme source&nbsp;:

* soit en un programme directement compréhensible et exécutable par la machine (les fichiers portant l'extension .exe sont des programmes exécutables directement par la machine)
* soit en un **bytecode** directement compréhensible et exécutable par une **machine virtuelle** (les fichiers portant l'extension .class sont des bytecodes). Dans ce second cas, cette machine virtuelle doit être installée sur l'ordinateur pour qu'il puisse exécuter le bytecode.

Parmi les langages de programmation pouvant être compilés, on peut citer par exemple&nbsp;:

* Pascal, C et C++ où le résultat de la compilation est un programme exécutable
* Java et Python où le résultat de la compilation est un bytecode.

### L'interprétation

Le principe de l'interprétation est d'utiliser un programme spécifique, appelé **interpréteur**, qui va lire le programme source séquentiellement, instruction par instruction. Il traduit chaque instruction en **langage machine** avant de la transmettre à l'ordinateur pour que celui-ci l'exécute. Parmi les langages de programmation pouvant être interprétés, on peut citer par exemple&nbsp;:

* Perl
* PHP
* Python (il est à noter que les programmes Python peuvent aussi être compilés).

Voici ci-dessous le programme source Python (on utilise généralement le terme de **script Python**) prêt à être interprété (avec un exemple d'exécution).


```python
from math import sqrt

# Saisie des données au clavier

print("Saisissez les valeurs des 3 coefficients a, b et c dans cet ordre : ")
# Saisie et mémorisation des coefficients (conversion des chaînes saisies en nombres réels)
coeff_a = float(input())
coeff_b = float(input())
coeff_c = float(input())

# Calcul et mémorisation du discriminant de l'équation

delta = (coeff_b**2)-(4 * coeff_a * coeff_c)

# Calcul des racines réelles (ou pas) en fonction de la valeur du discriminant

if (delta >= 0):
    if (delta > 0):
        racine1 = ((-1 * coeff_b) - sqrt(delta))/(2 * coeff_a)
        racine2 = ((-1 * coeff_b) + sqrt(delta))/(2 * coeff_a)
        print(f"L'équation admet deux racines réelles égales à {racine1} et {racine2}.")
    else:
        racine1 = (-1 * coeff_b)/(2 * coeff_a)
        print(f"L'équation admet une racine réelle double égale à : {racine1}.")
else:
    print("Cette équation n'admet pas de racine réelle.")
```

    Saisissez les valeurs des 3 coefficients a, b et c dans cet ordre : 
    

     4
     4
     1
    

    L'équation admet une racine réelle double égale à : -0.5.
    

## Le test du programme

Cette dernière étape de la conception d'un programme consiste à vérifier que celui-ci fonctionne correctement, et qu'il est conforme à ce qui a été défini lors de la phase de conception. Pour ce faire, il est nécessaire de constituer des **jeux d'essai**, c'est-à-dire des exemples d'entrées possibles avec les sorties attendues du programme. Ces jeux d'essai doivent être exhaustifs, dans le sens où ils doivent permettre de tester le comportement du programme dans tous les cas de figures possibles. Le programme est ensuite exécuté sur ces jeux d'essai. Si toutes les exécutions se déroulent normalement (une exécution normale est une exécution du début à la fin sans plantage du programme) et que les sorties produites sont conformes à celles attendues, on peut alors considérer que le programme est terminé. Si des erreurs sont constatées, il sera nécessaire de revoir le travail en amont afin de corriger le programme. La correction se fera à une étape différente (généralement au niveau de la conception ou du codage) en fonction du type d'erreur constaté.
Si on considère le programme précédent, en fonction des coefficients de l'équation (les valeurs des variables **coeff_a**, **coeff_b** et **coeff_c**), il existe trois cas de figure possibles&nbsp;:

* l'équation admet deux racines réelles
* l'équation admet une seule racine réelle
* l'équation n'admet pas de racine réelle.

Pour tester complètement ce programme, il faut donc trouver au minimum trois jeux d'essai (un jeu d'essai pas cas). Voici des propositions de jeux d'essai que vous pouvez tester en interprétant le programme ci-dessus&nbsp;:

* $x^2+3x+2=0$ soit les valeurs respectives de 1, 3 et 2 pour les variables saisies **coeff_a**, **coeff_b** et **coeff_c**. Le programme doit afficher les valeurs des deux racines réelles : -2 et -1.
* $4x^2+4x+1=0$ soit les valeurs respectives de 4, 4 et 1 pour les variables saisies **coeff_a**, **coeff_b** et **coeff_c**. Le programme doit afficher la valeur de l'unique racine réelle : -1/2.
* $x^2+x+1=0$ soit les valeurs respectives de 1, 1 et 1 pour les variables saisies **coeff_a**, **coeff_b** et **coeff_c**. Le programme doit afficher un message indiquant qu'il n'existe pas de racine réelle.

## Les différents types d'erreurs

### Erreur de syntaxe

Comme tout langage, un langage de programmation se base sur des règles précises qui doivent être respectées. Une erreur de syntaxe dans un programme source correspond à un non respect des règles de syntaxe et de structure du langage choisi. C'est en quelque sorte une faute d'orthographe dans le programme. On ne peut pas énumérer toutes les erreurs de syntaxe possibles, mais en voici quelques-unes assez courantes&nbsp;:

* erreur sur un mot réservé du langage, par exemple **imput** à la place de **input**
* oubli d'une parenthèse (ouvrante ou fermante) dans une expression de calcul
* erreur dans l'écriture d'un nom de variable
* oubli d'un guillemet ou d'une apostrophe autout d'une chaîne de caractères
* etc.

Une erreur de syntaxe est toujours signalée lors de la phase de compilation ou d'interprétation du programme. Pour la corriger, il faut retourner à l'étape de codage. Vous trouverez ci-dessous deux exemples de scripts Python (toujours notre programme de l'équation !) dont l'interprétation indique des erreurs de syntaxe. Quelles sont ces erreurs&nbsp;? Notez bien que le message d'erreur fourni par l'interpréteur, ainsi que parfois la ligne où est censée se trouver l'erreur, ne sont pas toujours exacts. Avant d'exécuter les scripts, n'oubliez pas de réinitialiser la mémoire de l'interpréteur en cliquant sur la flèche circulaire "Restart the kernel".


```python
from math import sqrt

# Saisie des données au clavier

print("Saisissez les valeurs des 3 coefficients a, b et c dans cet ordre : ")
# Saisie et mémorisation des coefficients (conversion des chaînes saisies en nombres réels)
coeff_a = float(input())
coeff_b = float(input())
coeff_c = float(input())

# Calcul et mémorisation du discriminant de l'équation

delta = (coeff_b**2)-(4 * coeff_a * coeff_c)

# Calcul des racines réelles (ou pas) en fonction de la valeur du discriminant

if (delta >= 0):
    if (delta > 0):
        racine1 == ((-1 * coeff_b) - sqrt(delta))/(2 * coeff_a)
        racine2 = ((-1 * coeff_b) + sqrt(delta))/(2 * coeff_a)
        print(f"L'équation admet deux racines réelles égales à {racine1} et {racine2}.")
    else:
        racine1 = (-1 * coeff_b)/(2 * coeff_a)
        print(f"L'équation admet une racine réelle double égale à : {racine1}.")
else:
    print("Cette équation n'admet pas de racine réelle.")
```

    Saisissez les valeurs des 3 coefficients a, b et c dans cet ordre : 
    

     5
     6
     1
    


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Input In [2], in <cell line: 17>()
         17 if (delta >= 0):
         18     if (delta > 0):
    ---> 19         racine1 == ((-1 * coeff_b) - sqrt(delta))/(2 * coeff_a)
         20         racine2 = ((-1 * coeff_b) + sqrt(delta))/(2 * coeff_a)
         21         print(f"L'équation admet deux racines réelles égales à {racine1} et {racine2}.")
    

    NameError: name 'racine1' is not defined



```python
from math import sqrt

# Saisie des données au clavier

print("Saisissez les valeurs des 3 coefficients a, b et c dans cet ordre : ")
# Saisie et mémorisation des coefficients (conversion des chaînes saisies en nombres réels)
coeff_a = float(input())
coeff_b = float(input())
coeff_c = float(input())

# Calcul et mémorisation du discriminant de l'équation

delta = (coeff_b**2)-(4 * coeff_a * coeff_c)

# Calcul des racines réelles (ou pas) en fonction de la valeur du discriminant

if (delta >= 0):
    if (delta > 0):
        racine1 == ((-1 * coeff_b) - sqrt(delta))/(2 * coeff_a)
        racine2 = ((-1 * coeff_b) + sqrt(delta))/(2 * coeff_a)
        print(f"L'équation admet deux racines réelles égales à {racine1} et {racine2}.")
    else:
        racine1 = (-1 * coeff_b)/(2 * coeff_a)
        print(f"L'équation admet une racine réelle double égale à : {racine1.")
else:
    print("Cette équation n'admet pas de racine réelle.")
```


      Input In [1]
        print(f"L'équation admet une racine réelle double égale à : {racine1.")
                                                                              ^
    SyntaxError: f-string: expecting '}'
    


### Erreur sémantique

Un programme contient une erreur de sémantique lorsqu'il ne produit pas le(s) résultat(s) attendu(s). Une telle erreur se détecte lors de la phase de test et nécessite de retourner à la phase de conception pour corriger l'algorithme, puis le programme source. Il faudra ensuite refaire les étapes d'interprétation (ou de compilation) puis de test.

### Erreur à l'exécution ou à l'interprétation

Une erreur à l'exécution ou à l'interprétation se produit lors de situations exceptionnelles (on parle aussi d'**exception**)&nbsp;:

* mémoire vive de la machine insuffisante
* accès à des données dans un fichier qui n'existe pas
* mauvaise saisie de l'utilisateur (par exemple, une chaîne de caractères alors qu'un nombre est attendu)
* problème matériel sur la machine
