# Docker Swarm — Déploiement & opérations (cluster docker-manager-01/02/03)

> **Source** : sessions Claude 2025-2026, validées en production
> **Contexte** : 3 VMs managers — docker-manager-01/Tom (192.168.50.61), 02/Zakh (192.168.50.62), 03/Ilan (192.168.50.63). VIP Keepalived 192.168.50.36. Stacks sur CephFS : /mnt/cephfs/docker-cluster/Docker-Swarm/
> **Dernière mise à jour** : 2026-06-10

---

## Les fichiers .env ne sont PAS chargés automatiquement par docker stack deploy

Contrairement à docker-compose, `docker stack deploy` ignore les fichiers `.env`. Avant tout déploiement d'une stack utilisant des variables d'environnement :

```bash
set -a && source <stack>/.env && set +a
docker stack deploy -c docker-compose.yml <NOM_STACK>
```

**Symptôme si oublié** : variables vides dans les services, comportements silencieusement cassés (URLs vides, mots de passe absents).

---

## docker ps ne montre que les conteneurs du nœud local

`docker ps` n'affiche que les conteneurs tournant sur le nœud où la commande est exécutée. Pour localiser un service dans le Swarm, toujours commencer par :

```bash
docker service ps <nom_service>
```

Cette commande identifie le nœud qui héberge réellement la tâche. Ensuite seulement, se connecter à ce nœud pour inspecter le conteneur.

---

## Mise à jour d'image : --image + --force pour re-pull sur le bon nœud

Pour forcer un service à re-télécharger son image (exemple vécu : Homebridge) :

```bash
docker service update --image <image>:<tag> --force <service>
```

`--force` seul réutilise l'image en cache local — il ne re-pull pas. La combinaison `--image` + `--force` force le re-pull sur le nœud cible réel de la tâche.

---

## Tâche bloquée en "Preparing" : docker service update --force

Après un événement transitoire d'élection de leader Swarm, une tâche peut rester bloquée en état "Preparing". L'action de déblocage correcte est :

```bash
docker service update --force <nom_service>
```

Cela force une re-planification de la tâche sans toucher à la configuration.

---

## stop-first : fenêtre de vulnérabilité quorum

L'ordre de mise à jour `stop-first` (utilisé quand un port hôte doit être libéré, ex. Homebridge en réseau host) crée une fenêtre où l'ancien conteneur est arrêté avant que le nouveau démarre. Pendant les transitions sur les services critiques, le Swarm est vulnérable à une perte de quorum si un autre incident survient simultanément. À réserver aux services qui l'exigent (ports host), préférer `start-first` ailleurs.

---

## Convention : version pinning explicite des images

Toujours pinner les versions exactes des images Docker (ex. `technitium/dns-server:15.2.0`, jamais `latest` en production). Vérifier le format exact du tag sur les releases GitHub du projet — exemple : Technitium utilise un semver 3 chiffres (`15.2.0`, pas `15.2`).

---

## Accès SSH depuis le M1

Le M1 (192.168.0.37) a un accès SSH sans mot de passe vers les 3 managers (192.168.50.61/62/63), utilisé par Hermes via l'outil MCP `exec_command` du serveur Proxmox.

**Particularité exec_command** : l'outil n'exécute pas via un shell. Les redirections, pipes et variables nécessitent un wrapper :

```bash
bash -c 'commande | pipe > fichier'
```

Le M1 n'a pas de route directe vers le réseau 192.168.50.x pour certains services (ex. API Technitium) — passer par SSH via docker-manager-01.
