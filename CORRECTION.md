TP - DNS Spoofing Demonstration CORRECTION
==========================================

Rappel sujet : 

Ce TP a pour but de reproduire une attack sur DNS (DNS Poisoning / Sppofing) sur un réseau fermé via des dockers. 
Dans ce TP plusieurs docker seront lancés dans le but de reproduire un résolveur DNS, un serveur DNS Upstream (de redirection), un Attaquant et une victime.

On utilisera dans cette démonstration l'adresse google.com pour la rediriger vers 1.2.3.4 (adresse de l'attaquant).


### Build

A) Script attaker.py : 

```py
if len(sys.argv) < 3:
    print("Utilisation: attack.py [target (domaine)] [IP de redirection]")
    sys.exit()

hostname = sys.argv[1]

fake_ip = sys.argv[2]
```

B) Lancement docker compose : 

```bash
docker-compose up --build
```

C) Ce code est un serveur DNS qui utilise un cache pour stocker des enregistrements DNS. Il est utilisé pour tester une attaque de contamination du cache. Lorsqu'une demande DNS est reçue, le code vérifie si l'enregistrement est déjà présent dans le cache. Si oui, il renvoie l'enregistrement enregistré. Sinon, le code envoie une demande à un serveur DNS principal (qui est spécifié par la variable "ns") pour obtenir les informations requises, les enregistrements reçus sont stockés dans le cache et sont ensuite renvoyés au demandeur. Le code utilise la bibliothèque dnslib pour gérer les protocoles DNS et la bibliothèque gevent pour gérer les sockets réseau de manière asynchrone.


### L'attaque

D) Utilisation docker attacker :

```bash
docker exec -it attacker bash
```

E) Exemple lancement d'attaque :

```bash
python attack.py google.com 1.2.3.4
```


### La victime

F) 

```bash
docker exe -it victim bash
```

G) Commande dig :

```bash
dig google.com
```
