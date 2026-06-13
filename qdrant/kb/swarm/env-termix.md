# Termix — Variables d'environnement

Stack : `termix/docker-compose.yml`
Fichier : `termix/data/.env` (gitignored)

## Variables

| Variable | Rôle |
|---|---|
| `JWT_SECRET` | Secret JWT pour l'authentification des sessions (auto-généré) |
| `DATABASE_KEY` | Clé de chiffrement de la base de données (auto-générée) |
| `ENCRYPTION_KEY` | Clé de chiffrement générale (auto-générée) |
| `INTERNAL_AUTH_TOKEN` | Token d'authentification interne entre services (auto-généré) |
| `CREDENTIAL_SHARING_KEY` | Clé pour le partage de credentials entre utilisateurs (auto-générée) |
