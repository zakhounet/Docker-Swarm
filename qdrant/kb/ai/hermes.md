# Hermes Agent — Configuration & lessons learned

> **Source** : sessions de mise en place (Noos Research, framework sorti février 2026)
> **Déploiement** : backend sur M1 (192.168.0.37), dashboard http://192.168.0.37:9119, lancé via launchd. Hermes Desktop sur M4. Gateway Telegram @hermes_nessim_bot (user ID 2088447676)
> **Dernière mise à jour** : 2026-06-10

---

## Stack LLM

- **Principal** : Anthropic API claude-sonnet (Tier 2, 450K ITPM)
- **Fallback** : Ollama local (Qwen3.5:9b) — déclenché sur ERREUR uniquement (rate limit, panne, auth), jamais sur complexité de tâche. Le fallback est scoped au tour : chaque nouveau message repart sur le principal.
- **Auxiliaire** : Haiku pour la compression de contexte
- **Contrainte** : Hermes exige un contexte de 64K tokens minimum sur le modèle principal
- Hermes supporte les endpoints locaux MLX/llama.cpp (détection automatique localhost/LAN, timeouts adaptés). MLX ~37% plus rapide que llama.cpp en génération.

---

## MCP servers configurés

ha-mcp (770 entités HA), mcp-portainer (filtré à 23 outils, ~38.8K tokens), mcp-proxmox (3 nœuds, 7 VMs), unifi-network-mcp (lazy loading, 172 outils), unifi-protect-mcp (10 caméras, 53 outils).

**Bug connu** : le Dashboard Hermes ne recharge PAS les outils MCP après un restart — il faut cliquer Settings → MCP Servers → Reload MCP dans Hermes Desktop avant d'ouvrir une nouvelle session.

---

## Pièges de configuration

- `hermes config set` stocke les listes YAML comme des chaînes littérales, pas du vrai YAML — corrections manuelles au `sed` nécessaires après coup.
- L'affichage `[object Object]` pour `fallback_providers` dans Hermes Desktop est un bug cosmétique confirmé (#9726) — la config sous-jacente est correcte.
- L'outil MCP `exec_command` (Proxmox) ne passe pas par un shell : envelopper les redirections/pipes dans `bash -c '...'`.

---

## Mémoire & RAG

- Mémoire Hermes : MEMORY.md / USER.md via l'outil `memory`
- MemPalace : store ~/.mempalace/ via mempalace-rs v0.4.2 — le serveur MCP Python MemPalace est définitivement cassé sur Apple Silicon (issue ChromaDB/gRPC #649), utiliser exclusivement mempalace-rs
- Qdrant v1.18.2 sur M1 (Docker Compose, ports 6333/6334), embedding nomic-embed-text via Ollama
- Web : SearXNG sur le Swarm derrière Traefik (searxng.test.teamfnb.com, format JSON activé), Firecrawl comme backend d'extraction

---

## Vision / multimodal : limitation actuelle

Hermes route TOUTES les analyses d'images vers le modèle auxiliaire de vision configuré (qwen3-vl ou autre), même si le modèle principal est nativement multimodal. Le passage direct d'images au modèle principal (`native_vision`) fait l'objet d'une issue GitHub ouverte (problèmes dans le pipeline core, paramètre `detail` absent des blocs image_url). Ne pas compter sur le multimodal natif tant que ce n'est pas mergé.

---

## Notion

CLI ntn v0.16.0 validé. Les DEUX variables `NOTION_API_KEY` et `NOTION_API_TOKEN` doivent être définies. Documentation homelab complète créée dans Notion.

---

## Abandons documentés

- **Recall self-hosted** : abandonné définitivement (image absente de ghcr.io, pas de support Ollama en mode HTTP, OAuth incompatible Claude Desktop).
