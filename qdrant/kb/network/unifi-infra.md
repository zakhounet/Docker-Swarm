# UniFi — Infrastructure Réseau Complète

> Généré automatiquement depuis l'API UniFi — UDM-SE (192.168.0.1)
> Dernière mise à jour : juin 2026

---

## 🌐 Réseaux / VLANs

| Nom | Subnet | VLAN | Type | DHCP |
|---|---|---|---|---|
| Main | 192.168.0.1/24 | — | Corporate | ✅ |
| IoT | 192.168.20.1/24 | 20 | Corporate | ✅ |
| Camera | 192.168.30.1/24 | 30 | Corporate | ✅ |
| Guest | 192.168.40.1/24 | 40 | Guest | ✅ |
| Liaison 10 GBs | 192.168.50.1/24 | 50 | Corporate | ✅ |
| WireGuard Server | 192.168.200.1/24 | — | VPN | — |
| OpenVPN Server | 192.168.1.1/24 | — | VPN | — |
| WG-UDMSE | 10.100.0.1/16 | — | VPN | — |
| Primary LEOX | — | — | WAN1 (Orange) | — |
| 5G iPhone Franck | — | — | WAN2 (failover) | — |

---

## 📡 WiFi — SSIDs

| SSID | Sécurité | VLAN | Caché | Notes |
|---|---|---|---|---|
| Main | WPA-PSK | — | Non | Réseau principal |
| IoT | WPA-PSK | — | Non | Appareils IoT |
| Guest | WPA-PSK | — | Non | Réseau invités |
| Camera | WPA-PSK | — | **Oui** | Caméras (masqué) |
| UID | WPA-EAP | — | Non | Entreprise (802.1X) |
| UID_IoT | WPA-PSK | — | Non | IoT entreprise |

---

## 🖥️ Équipements UniFi (21 devices)

### Gateway
| Nom | Modèle | IP | MAC |
|---|---|---|---|
| UDMSE | UDM Pro SE | 81.250.179.22 (WAN) | 70:a7:41:64:87:a9 |

### Switches
| Nom | Modèle | IP | MAC |
|---|---|---|---|
| USW-Aggregation | USL8A | 192.168.0.4 | 78:45:58:6d:92:f2 |
| USW Aggregation 2 | USL8A | 192.168.0.20 | 1c:6a:1b:98:37:26 |
| USW-Enterprise-8-PoE | US68P | 192.168.0.3 | 70:a7:41:6b:6c:c6 |
| USW Pro HD 24 PoE | USWED72 | 192.168.0.2 | 94:2a:6f:4c:63:f9 |
| USW Ultra | USM8P | 192.168.0.61 | 58:d6:1f:8f:f6:65 |
| USW-Ultra Salon | USM8P | 192.168.0.9 | f4:e2:c6:ad:3a:97 |
| USW Flex 2.5G 8 PoE (MS-01) | USWED37 | 192.168.0.19 | 84:78:48:fc:43:3d |
| USW Flex 2.5G 8 PoE | USWED37 | 192.168.0.18 | 94:2a:6f:fe:28:a7 |
| USW Flex XG | USFXG | 192.168.0.5 | 78:45:58:6f:a6:10 |
| USW-Flex Jardin | USF5P | 192.168.0.6 | 60:22:32:56:b6:c1 |
| Flex-Mini Bureau 1 | USMINI | 192.168.0.8 | 60:22:32:35:e7:0c |
| Flex-Mini Bureau 2 | USMINI | 192.168.0.7 | 60:22:32:35:e7:1b |
| UPS Tower | USWDA24 | 192.168.0.21 | 1c:0b:8b:3c:1a:28 |

### Points d'accès WiFi
| Nom | Modèle | IP | MAC |
|---|---|---|---|
| U7 In-Wall Appartement | UAPA6A5 | 192.168.0.10 | 84:78:48:02:1c:e2 |
| U7 Pro Outdoor Piscine | UAPA6B0 | 192.168.0.11 | 94:2a:6f:ea:65:bb |
| U7 Pro Outdoor Abri | UAPA6B0 | 192.168.0.12 | 1c:0b:8b:0a:d3:a7 |
| U6-Mesh | U6M | 192.168.0.13 | d0:21:f9:f5:22:5c |
| U7 Pro Outdoor entrée maison | UAPA6B0 | 192.168.0.14 | 1c:0b:8b:0a:e2:9e |
| U7 Pro Max Bureau | U7PROMAX | 192.168.0.15 | 94:2a:6f:de:e3:49 |
| U7 Pro Max Etage | U7PROMAX | 192.168.0.16 | 94:2a:6f:de:f9:15 |

---

## 🔒 Firewall — Groupes

### Groupes d'adresses
| Nom | Membres |
|---|---|
| RFC1918 | 192.168.0.0/16, 172.16.0.0/12, 10.0.0.0/8 |
| Trusted | 192.168.0.0/24, 192.168.50.0/24 |
| Untrusted | 192.168.20.0/24, 192.168.30.0/24 |
| MANAGEMENT_SERVERS | 192.168.0.45, 192.168.0.54, 192.168.0.52 (nœuds Proxmox) |
| AP IP | 192.168.0.12, 0.13, 0.14, 0.15, 0.16 (APs WiFi) |
| Block Acces to UDMSE | 192.168.0.1, 192.168.20.1, 192.168.30.1 (gateways) |
| Block Camera to Gateways | 192.168.0.1, 192.168.20.1, 192.168.40.1 |
| Block Guest to Gateways | 192.168.0.1, 192.168.20.1, 192.168.30.1 |
| IoT Gateway | 192.168.20.1 |
| all local DNS server | 192.168.0.36, 192.168.0.104, 1.1.1.1 |
| Homes Assistants + Homebridge + Docker + Apple TV | 192.168.0.67, 192.168.0.25, 192.168.0.36 |
| Cloudflare IP server | 103.21.244.0/22, 103.22.200.0/22, 103.31.4.0/22, ... |

### Groupes de ports
| Nom | Ports |
|---|---|
| http, https, ssh | 80, 443, 22 |
| DNS server port | 53 |
| HTTPS Only | 443 |

---

## 🔀 Port Forwards

| Nom | Proto | Port WAN | Destination | Port Interne | Actif |
|---|---|---|---|---|---|
| Plex | TCP+UDP | 32497 | 192.168.0.125 | 32400 | ✅ |
| Plex 2 | TCP+UDP | 32400 | 192.168.50.55 | 32400 | ✅ |
| qbittorrent | TCP+UDP | 8085 | 192.168.50.97 | 8085 | ✅ |

---

## 🔑 VPN

- **WireGuard** : 192.168.200.0/24 (full-tunnel)
- **OpenVPN** : 192.168.1.0/24
- **WG-UDMSE** : 10.100.0.0/16

---

## 📋 Zone-Based Firewall (ZBF) — Règles clés

Architecture UDM-SE Network 9.x — ZBF actif :
- **VLAN 30 Camera** → zone `Untrusted` — accès sortant bloqué par défaut
- **VLAN 20 IoT** → zone `Untrusted`
- **Exception** : NVR 192.168.30.100 → ports 443 + ICMP autorisés depuis WireGuard VPN
- **Groupes Trusted** : Main (192.168.0.0/24) + Swarm (192.168.50.0/24)
- **Groupes Untrusted** : IoT (192.168.20.0/24) + Camera (192.168.30.0/24)
