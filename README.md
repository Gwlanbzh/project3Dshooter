
# Créer et Activer l'environnement virtuel python

Pour toutes les étapes suivante on considéreras que vous êtes dans le dossier du projet.

## Création

Pour créer l'environnement virtuel, entrez la commande suivante :
`python3 -m venv .venv`

## Activation 

`source .venv/bin/activate`

## Installation des prérequis

Une fois l'environnement activé, vous pouvez installer les différents package nécessaire au fonctionnement du jeu :
Pour cela, lancez la commande : 

`python3 -m pip install -r requirements.txt`

# Lancer le jeu

`py src/main.py`

# Création de maps

Pour créer une map, il faut choisir une *skybox*, une couleur de sol, un *set* de textures, et dessiner une carte.

## Carte

Les maps sont créées avec des fichiers textes. Un fichier de m lignes et n colonnes créera une map de taille m×n.
Les espaces correspondent à des vides, les chiffres à des murs, et les lettres à des entités (la case est importante).

Les différents chiffres donneront différentes textures (pour savoir laquelle, regarder dans src/assets/visual/textures/, dans le dossier correspondant au *set* choisi).
À chaque chiffre est attribué nombre à virgule flottante dans le fichier `textures.py`, qui correspond à la hauteur du mur qui sera généré par ce chiffre. Ceci est utile pour créer des tours, caisses...
Il est important de noter que le chiffre 9 renvoie vers la texture 1, à ceci près qu'il génèrera une case que le joueur peut traverser, et sert donc à placer des **secrets** dans la carte.

    1 à 4: murs standard.
    5: caisse.
    6: tour.
    7: porte de sortie du niveau
    8: non attribué
    9: secret (texture et hauteur n°1)

Les entités sont de plusieurs types: props, *pickables*, mobs et joueur. Pour qu'une map soit jouable, il est nécessaire de placer un joueur dans le niveau, avec la lettre `P`. La case où il est placé correspond à la position où le joueur apparaîtra en début de partie.
Les props sont de simples objets inanimés, qui n'entrent pas en collision avec le joueur et les mobs (comme toutes les autres entités) et servent d'éléments de décor.
Les mobs sont de trois types: Grunt (ennemis de base), Heavy et Boss.
Les *pickables* sont un type d'entité particulier, dont le comportement peut être programmé pour réagir lorsqu'un joueur se trouve à proximité. Ils sont de trois types: les munitions et les kits de santé. Pour les deux premiers types, il existe un petit et un grand modèle, qui donnent plus ou moins de santé/munitions. Le troisième ajoute une arme à l'inventaire du joueur et donne un certain nombre de munitions en fonction de l'arme.
Enfin, la lettre E correspond non pas à une entité, mais à une sortie, c'est-à-dire que la partie s'arrêtera lorsque que le joueur sera dans une de ces cases, il aura agné.

    P: joueur.
    G: Grunt.
    V: Heavy.
    B: Boss.

    h: santé (petit kit)
    H: santé (grand kit)
    a: munitions (petit kit)
    A: munitions (grand kit)

    S: Shotgun.
    R: Rifle.
    M: Superweapon.

    l: lampadaire.
    T: arbre (grand, à utiliser avec parcimonie)
    t: arbre mort
    b: barril

    E: sortie

## Compilation

La compilation se fait à l'aide du script `compile.py`, dans le dossier `src`.

__Syntaxe:__
```bash
./compile.py SOURCE DEST [--skybox=<filename>] [--floor=<R>,<G>,<B>] [--texture-set=<name>]
```
Où `filename` est le nom de l'image choisi comme skybox, `R`, `G` et `B` des entiers inférieurs à 256, `name` le nom d'un set (les sets disponibles sont dans `src/assets/visual/textures/`.)
Les trois options sont facultatives, elles ont unee valeur par défaut (`"sky.png"`, `70,70,70` et `"default"`).

Par convention, les fichiers textes pour les maps sont de simple `.txt`, alors que les maps compilées devront avoir un nom en `.bin`.

## Comment jouer :

Pour se déplacer : 
    - Z : avancer
    - Q : aller à gauche
    - D : aller à droite
    - S : reculer 

Changer d'arme :
    - 1 (&) : utiliser le point
    - 2 (é) : utiliser le pistolet
    - 3 (") : si dans l'inventaire, utiliser Shotgun
    - 4 (') : si dans l'inventaire, utiliser Rifle
    - 5 (() : si dans l'inventaire, utiliser SuperWeapon

tirer : 
    - clic gauche

menu : 
    - escape