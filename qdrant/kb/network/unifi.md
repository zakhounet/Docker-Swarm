# UniFi — Réseau, WiFi, ZBF (UDM-SE + NVR Protect)

> **Source** : sessions Claude 2025-2026
> **Matériel** : UDM-SE (192.168.0.1), NVR Protect (192.168.30.100) — deux hôtes distincts, deux MCP distincts (unifi-network-mcp / unifi-protect-mcp). WireGuard VPN : 192.168.200.0/24
> **Version Network** : 10.4.x
> **Dernière mise à jour** : 2026-06-10

---

## Réglementation France : pas de UNII-1 en extérieur

Les canaux UNII-1 (36–48) sont illégaux ETSI pour les points d'accès extérieurs en France. Les APs outdoor doivent utiliser UNII-3 et au-delà (canal 100+). Vérifier ce point avant tout changement de canal 5 GHz sur un AP extérieur.

---

## API radio MCP : paramètres exacts

- `unifi_get_device_radio` exige le paramètre `mac_address` (PAS `mac`)
- `unifi_update_device_radio` exige `radio` valant `'ng'` (2.4 GHz) ou `'na'` (5 GHz), plus `confirm: True`
- **Piège** : une erreur `api.err.InvalidChannel` renvoyée sur une bande DIFFÉRENTE de celle modifiée signifie qu'une config invalide pré-existante sur l'autre bande bloque la sauvegarde globale. Corriger d'abord la bande en erreur.

---

## UI Network 10.4.x : chemins déplacés

- Les groupes firewall sont sous **Networks → Network Lists** (plus sous CyberSecure → Groups)
- Le chemin "Radio Management" des anciennes versions n'existe plus

Ne pas suivre les tutoriels antérieurs à Network 10.x sans vérifier les chemins.

---

## ZBF (Zone-Based Firewall, Network 9.x+) : caméras en zone Untrusted

Le VLAN NVR/caméras est placé en zone Untrusted. Pour l'accès depuis le VPN (WireGuard), créer une policy Allow ciblée depuis la zone VPN, scopée sur IP/port spécifiques (NVR 192.168.30.100), plutôt que d'ouvrir largement la zone. Principe : ouvertures chirurgicales, jamais zone-à-zone complète vers Untrusted.

---

## Gestion de bande 2.4 GHz : min_rssi

Recommandation validée : min_rssi à -75 dBm sur les APs Bureau et Etage (2.4 GHz) pour forcer les clients distants à basculer sur un AP plus proche. Action encore ouverte.

---

## Suivi ouvert : STP Edge ports

Configuration des ports STP Edge sur le USW-Ultra et les Flex 2.5G à finaliser (follow-up planifié).
 
