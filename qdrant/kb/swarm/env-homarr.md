# Homarr — Variables d'environnement

Stack : `homarr/docker-compose.yml`
Fichier : `homarr/.env` (gitignored)

## Variables

| Variable | Rôle |
|---|---|
| `AUTH_SECRET` | Secret JWT pour l'authentification des sessions utilisateur |
| `SECRET_ENCRYPTION_KEY` | Clé de chiffrement des données sensibles (intégrations, credentials) |
| `DB_PASSWORD` | Mot de passe de la base de données PostgreSQL interne |
