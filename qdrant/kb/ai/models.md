# Modèles locaux & matériel AI — Benchmarks et choix

> **Source** : sessions Claude 2025-2026 + canirun.ai + doc Hermes
> **Dernière mise à jour** : 2026-06-10

---

## Parc machines AI

| Machine | RAM | Rôle |
|---------|-----|------|
| Mac mini M1 (192.168.0.37) | 16GB | Prod AI : Hermes, Ollama, Qdrant, Open WebUI. ~150GB disque libre (contrainte modèles) |
| MacBook Pro M5 Pro | 24GB | Banc de test MLX + Hermes |
| Mac mini M4 (192.168.0.93) | — | Workstation, Claude Desktop/Hermes Desktop |
| Mac mini M5 128GB/1TB | 128GB | Prévu ~sept. 2026, future prod AI (risque dispo mémoire, délais 14 semaines observés) |

---

## Modèles Ollama installés sur le M1

qwen2.5:7b, qwen2.5:3b, qwen2.5-7b-64k (custom num_ctx 64000), qwen2.5-3b-64k, nomic-embed-text. Upgrade planifiée : qwen3.5:9b.

---

## Qwen3.5 9B : quantizations (données canirun.ai)

| Quant | VRAM | Qualité | M1 16GB |
|-------|------|---------|---------|
| Q4_K_M | 5.1 GB | bonne | ✅ confortable |
| Q6_K | 7.4 GB | excellente | ✅ recommandé |
| Q8_0 | 9.7 GB | excellente | ⚠️ limite avec les services |

Modèle multimodal (chat + vision), contexte 32K, Apache 2.0, recommandé par la doc Hermes comme modèle de départ Apple Silicon.

---

## Bande passante mémoire : le facteur déterminant des tokens/sec

La vitesse d'inférence dépend d'abord de la bande passante mémoire, pas de la RAM totale :

| Puce | Bande passante | Estimation Qwen3.5 9B Q6 |
|------|---------------|--------------------------|
| M1 | ~68 GB/s | ~8-12 tok/s |
| M1 Pro | ~200 GB/s | ~25-30 tok/s |
| M4 Max | 546 GB/s | — |
| M3 Ultra | 800 GB/s | — |

Conséquence : pour la cible Gemma 27B sur la future machine, un M3 Ultra 96GB serait supérieur à un M4 Max 64GB (800 vs 546 GB/s). Attention : canirun.ai ne référence pas le M1 standard (seulement M1 Pro) — diviser ses estimations de vitesse par ~2.5.

---

## MLX vs Ollama vs LM Studio

- **Ollama et LM Studio** partagent le backend llama.cpp : perfs quasi identiques (Ollama légèrement devant grâce à son empreinte ~100MB vs ~500MB).
- **MLX** (framework Apple) : ~37% plus rapide que llama.cpp en génération sur Apple Silicon. Serveur API via `mlx_lm.server` (compatible OpenAI). Sur M1 standard le gain est plus faible ; il devient significatif sur M5 Pro et au-delà.
- **mlx_lm** = texte uniquement ; **mlx_vlm** = modèles vision (Gemma 4 n'existe en MLX que sous mlx_vlm car nativement multimodal).
- Décision : Ollama reste sur le M1 (prod, fallback Hermes) ; MLX testé sur MacBook M5 Pro ; arbitrage final pour le Mac mini M5.

---

## Gemma 4 (sorti avril 2026, Apache 2.0)

Tailles : E2B, E4B, 26B A4B (MoE), 31B. Le 26B A4B en 4-bit (~14GB) est le meilleur candidat pour un Mac 24GB+. Contexte 256K. Nécessite mlx_vlm. Cible d'inférence pour le futur Mac mini M5.

---

## RAG : Qdrant (prod) vs LEANN (à tester)

- **Qdrant** v1.18.2 : choix prod confirmé — Rust, API REST, quantization native, léger, déjà intégré.
- **LEANN** : index vectoriel ultra-compact (~97% de stockage en moins, recomputation à la volée des embeddings, graphe HNSW/DiskANN). Python only, pas d'API REST, pas de support Anthropic confirmé pour LeannChat. Dans notre architecture seul LeannSearcher serait utilisé (Hermes reste l'orchestrateur, LLM-agnostique). À tester sur le MacBook M5 Pro.
- Embeddings : nomic-embed-text (Ollama, local).
