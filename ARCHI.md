### Architecture du projet 

Utilisation de quatre docker distincts:\
`DNS` (`10.0.0.2`): Un résolveur DNS fragile et "attaquable"\
`Victim` (`10.0.0.3`): Une victime sur laquelle effectuer l'attaque\
`Attacker` (`10.0.0.4`): L'attaquant qui va lancer l'attaque\
`Upstream DNS` (`10.0.0.5`): Joue le rôle du serveur DNS montant

### Cache serveur DNS (`10.0.0.2`)

Ce serveur DNS est un simple résolveur DNS développé pour examiner entièrement le processus d'attaque. 

Il regarde d'abord le cache stocké et renvoie le cache s'il y en a un. Sinon, il transférera la requête au serveur DNS montant, en attendant les réponses.

Le but de ce projet est uniquement d'examiner le processus d'attaque. 
Le QID pour la requête est toujours défini pour être compris entre 10000 et 10050, et le port source est fixé à 22222 pour éviter de lancer une attaque de "birthday", qui n'est pas le but de ce projet.

Le serveur DNS est un simple résolveur DNS développé pour examiner entièrement le processus d'attaque.

### Serveur DNS (`10.0.0.5`)

Un serveur DNS local est mis en place pour prendre la place des serveurs DNS montants pour toujours répondre aux requêtes DNS avec l'IP `1.2.3.4`.

### Attacker (`10.0.0.4`)

L'adversaire envoie d'abord une requête DNS au serveur DNS cache (`10.0.0.2`), de sorte que le serveur enverra une requête DNS au serveur DNS montant et commencera à accepter les réponses. Ensuite, il envoie des réponses DNS en essayant toutes les QID possibles à partir de l'impersonation du serveur DNS montant (`10.0.0.5`) au serveur DNS cache (`10.0.0.2`).

Un script d'attaque (`/attacker/attack.py`) est donc créé.