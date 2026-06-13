# Traefik — Variables d'environnement

Stack : `traefik/docker-compose.yml`
Fichier : `traefik/.env` (gitignored)

## Variables

| Variable | Rôle |
|---|---|
| `CF_DNS_API_TOKEN` | Token API Cloudflare pour le DNS challenge Let's Encrypt (certificats wildcard `*.test.teamfnb.com`) |
| `TECHNITIUM_API_URL` | URL de l'instance Technitium DNS primary (`http://192.168.50.104:5380`) |
| `TECHNITIUM_API_TOKEN` | Token API Technitium pour la gestion des enregistrements DNS |
| `ACME_EMAIL` | Email de contact pour Let's Encrypt (`fnb2@orange.fr`) |
