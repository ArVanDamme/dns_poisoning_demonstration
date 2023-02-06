TP - DNS Spoofing Demonstration
===============================

Ce TP a pour but de reproduire une attack sur DNS (DNS Poisoning / Sppofing) sur un réseau fermé via des dockers. 
Dans ce TP plusieurs docker seront lancés dans le but de reproduire un résolveur DNS, un serveur DNS Upstream (de redirection), un Attaquant et une victime.

On utilisera dans cette démonstration l'adresse google.com pour la rediriger vers 1.2.3.4 (adresse de l'attaquant).
 

## Quickstart

### Prérequis

On aura besoin dans ce TP de Docker Compose et de Docker.

### Build

A) Commencons par corrigé le script attacker.py, toutes les indications se trouvent à l'intérieur !

B) Une fois correctement corrigé, construire et lancer le docker-compose !

Une fois lancé, le résolveur DNS et le sevreur DNS seront sur un mode d'écoute sur le port 53.

C) Ouvrez maintenant le fichier server.py, essayer de comprendre son fonctionnement et de l'expliquer brièvement.


### L'attaque

#### 1. Commencons par lancer le container d'attaque en mode console :

D) Rentré dans le docker de l'attaquant en mode intéractif via la console.

#### 2. Une fois dedans on peut lancer une attaque via le script python attack.py

E) Lancer une attaque sur un site internet quelconque (ex: google.com) et ajouter une IP de redirection (qui en théorie serait malveillante mais dans ce TP aucunement besoin de cela nous souhaitons simplement rediriger)

#### 3. Dans le console principale on peut voir une réponse du DNS : 

En sortie du conteneur `dns`, un "fake" DNS Record à bien été inséré en cache. On peut également le vérifier en se rendant dans le contenur de la victime.

### La victime

#### Commencons par lancer le container de la vicitme en mode console

F) Rentré dans le docker de la victime en mode intéractif via la console.

#### 2. Une fois dedans on peut lancer la commande "dig" dans le but d'observer la redirection

G) Utiliser la commande dig pour observer la redirection que vous venez de mettre en place

Cela devrait normalement afficher une réponse du serveur avec le domaine voulu mais avec l'IP de redirection de l'attaquant.
Et voila ! Vous avez correctement contourné un domaine d'une victime vers votre adresse IP choisie.

