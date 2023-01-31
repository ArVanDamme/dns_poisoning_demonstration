TP - DNS Spoofing Demonstration
===============================

Ce TP a pour but de reproduire une attack sur DNS (DNS Poisoning / Sppofing) sur un réseau fermé via des dockers. 
Dans ce TP plusieurs docker seront lancés dans le but de reproduire un résolveur DNS, un serveur DNS Upstream (de redirection), un Attaquant et une victime.

On utilisera dans cette démonstration l'adresse google.com pour la rediriger vers 1.2.3.4 (adresse de l'attaquant).
 

## Quickstart

### Prérequis

On aura besoin dans ce TP de Docker Compose et de Docker.

### Build

```bash
docker-compose build
docker-compose up
```
Une fois lancé, le résolveur DNS et le sevreur DNS seront sur un mode d'écoute sur le port 53.

### L'attaque

#### 1. Commencons par lancer le container d'attaque en mode console :

```bash
docker exec -it attacker bash
```

#### 2. Une fois dedans on peut lancer une attaque via le script python attack.py

On utilise ici google.com comme cible et 1.2.3.4 comme redirection

```bash
python attack.py google.com 1.2.3.4
```

#### 3. Dans le console principale on peut voir une réponse du DNS : 


En sortie du conteneur `dns`, un "fake" DNS Record à bien été inséré en cache. On peut également le vérifier en se rendant dans le contenur de la victime.

### La victime

#### Commencons par lancer le container de la vicitme en mode console


```bash
docker exec -it victim bash
```

#### 2. Une fois dedans on peut lancer la commande "dig" dans le but d'observer la redirection

```bash
dig google.com
```

Cela devrait normalement afficher une réponse du serveyr google.com avec l'ip 1.2.3.4
Et voila ! Vous avez correctement contourné l'adresse google.com d'une victime vers votre adresse 1.2.3.4

