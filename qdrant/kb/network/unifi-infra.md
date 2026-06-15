# UniFi Network — Snapshot infra

> Généré automatiquement le 2026-06-15 03:04 via API UDM-SE (192.168.0.1)
> Source : cron `unifi-kb-refresh` — ne pas éditer manuellement

## Réseaux / VLANs

| Nom | VLAN ID | Subnet | Purpose / DHCP |
|---|---|---|---|
| Primary LEOX (WAN1) | untagged | — | wan / static |
| 5G Iphone Franck | untagged | — | wan / static |
| Main | untagged | 192.168.0.1/24 | corporate / DHCP (192.168.0.2–192.168.0.254) |
| WireGuard Server | untagged | 192.168.200.1/24 | remote-user-vpn / static (192.168.200.2–192.168.200.254) |
| OpenVPN Server  | untagged | 192.168.1.1/24 | remote-user-vpn / static (192.168.1.6–192.168.1.254) |
| WG-UDMSE | untagged | 10.100.0.1/16 | remote-user-vpn / static |
| IoT | 20 | 192.168.20.1/24 | corporate / DHCP (192.168.20.6–192.168.20.254) |
| Camera | 30 | 192.168.30.1/24 | corporate / DHCP (192.168.30.6–192.168.30.254) |
| Guest | 40 | 192.168.40.1/24 | guest / DHCP (192.168.40.6–192.168.40.254) |
| Liaison 10 GBs | 50 | 192.168.50.1/24 | corporate / DHCP (192.168.50.101–192.168.50.200) |

## SSIDs WiFi

| SSID | Bande | VLAN | Sécurité | Activé |
|---|---|---|---|---|
| Camera | both | — | wpapsk | ✓ |
| Guest | both | — | wpapsk | ✓ |
| IoT | both | — | wpapsk | ✓ |
| Main | both | — | wpapsk | ✓ |
| UID | both | — | wpaeap | ✓ |
| UID_IoT | both | — | wpapsk | ✓ |

## Équipements UniFi

| Nom | Type | Modèle | IP | MAC | État | Version FW |
|---|---|---|---|---|---|---|
| Flex-Mini Bureau 1 | usw | USMINI | 192.168.0.8 | 60:22:32:35:e7:0c | 🟢 connected | 2.1.6.762 |
| Flex-Mini Bureau 2 | usw | USMINI | 192.168.0.7 | 60:22:32:35:e7:1b | 🟢 connected | 2.1.6.762 |
| U6-Mesh | uap | U6M | 192.168.0.13 | d0:21:f9:f5:22:5c | 🟢 connected | 6.8.2.15592 |
| U7 In-Wall Appartement | uap | UAPA6A5 | 192.168.0.10 | 84:78:48:02:1c:e2 | 🟢 connected | 8.6.11.18870 |
| U7 Pro Max Bureau | uap | U7PROMAX | 192.168.0.15 | 94:2a:6f:de:e3:49 | 🟢 connected | 8.6.11.18870 |
| U7 Pro Max Etage | uap | U7PROMAX | 192.168.0.16 | 94:2a:6f:de:f9:15 | 🟢 connected | 8.6.11.18870 |
| U7 Pro Outdoor Abri | uap | UAPA6B0 | 192.168.0.12 | 1c:0b:8b:0a:d3:a7 | 🟢 connected | 8.6.11.18870 |
| U7 Pro Outdoor Piscine | uap | UAPA6B0 | 192.168.0.11 | 94:2a:6f:ea:65:bb | 🟢 connected | 8.6.11.18870 |
| U7 Pro Outdoor entrée maison | uap | UAPA6B0 | 192.168.0.14 | 1c:0b:8b:0a:e2:9e | 🟢 connected | 8.6.11.18870 |
| UDMSE | udm | UDMPROSE | 81.250.179.22 | 70:a7:41:64:87:a9 | 🟢 connected | 5.1.15.33416 |
| UPS Tower | usw | USWDA24 | 192.168.0.21 | 1c:0b:8b:3c:1a:28 | 🟢 connected | 1.5.0.378 |
| USW Aggregation 2 | usw | USL8A | 192.168.0.20 | 1c:6a:1b:98:37:26 | 🟢 connected | 7.4.1.16850 |
| USW Flex 2.5G 8 PoE | usw | USWED37 | 192.168.0.18 | 94:2a:6f:fe:28:a7 | 🟢 connected | 2.1.8.971 |
| USW Flex 2.5G 8 PoE MS-01 | usw | USWED37 | 192.168.0.19 | 84:78:48:fc:43:3d | 🟢 connected | 2.1.8.971 |
| USW Flex XG | usw | USFXG | 192.168.0.5 | 78:45:58:6f:a6:10 | 🟢 connected | 7.4.1.16850 |
| USW Pro HD 24 PoE | usw | USWED72 | 192.168.0.2 | 94:2a:6f:4c:63:f9 | 🟢 connected | 7.4.1.16850 |
| USW Ultra | usw | USM8P | 192.168.0.61 | 58:d6:1f:8f:f6:65 | 🟢 connected | 2.1.8.971 |
| USW-Aggregation | usw | USL8A | 192.168.0.4 | 78:45:58:6d:92:f2 | 🟢 connected | 7.4.1.16850 |
| USW-Enterprise-8-PoE | usw | US68P | 192.168.0.3 | 70:a7:41:6b:6c:c6 | 🟢 connected | 7.4.1.16850 |
| USW-Flex Jardin | usw | USF5P | 192.168.0.6 | 60:22:32:56:b6:c1 | 🟢 connected | 7.4.1.16850 |
| USW-Ultra Salon | usw | USM8P | 192.168.0.9 | f4:e2:c6:ad:3a:97 | 🟢 connected | 2.1.8.971 |

## Groupes Firewall

| Nom | Type | Membres |
|---|---|---|
| AP IP  | address-group | 192.168.0.12, 192.168.0.13, 192.168.0.14, 192.168.0.15, 192.168.0.16 (+2) |
| Block Acces to UDMSE  | address-group | 192.168.0.1, 192.168.20.1, 192.168.30.1, 192.168.40.1, 192.168.50.1 |
| Block Camera to Gateways | address-group | 192.168.0.1, 192.168.20.1, 192.168.40.1, 192.168.50.1 |
| Block Guest to Gateways | address-group | 192.168.0.1, 192.168.20.1, 192.168.30.1, 192.168.50.1 |
| Cloudflare IP server | address-group | 103.21.244.0/22, 103.22.200.0/22, 103.31.4.0/22, 104.16.0.0/13, 104.24.0.0/14 (+10) |
| DNS server port | port-group | 53 |
| HTTPS Only | port-group | 443 |
| Homes Assistants + Homebridge + Docker + Apple TV | address-group | 192.168.0.67, 192.168.0.25, 192.168.0.36, 192.168.50.97, 192.168.0.20 |
| IoT Gateway | address-group | 192.168.20.1 |
| MANAGEMENT_SERVERS | address-group | 192.168.0.45, 192.168.0.54, 192.168.0.52 |
| RFC1918 | address-group | 192.168.0.0/16, 172.16.0.0/12, 10.0.0.0/8 |
| Trusted | address-group | 192.168.0.0/24, 192.168.50.0/24 |
| Untrusted | address-group | 192.168.20.0/24, 192.168.30.0/24 |
| all local DNS server | address-group | 192.168.0.36, 1.1.1.1, 192.168.0.104, 192.168.50.36, 192.168.50.104 |
| http, https, ssh | port-group | 80, 443, 22 |

## NAT / Port Forwards

| Nom | Proto | Port ext. | IP dest | Port dest | Activé |
|---|---|---|---|---|---|
| Plex | tcp_udp | 32497 | 192.168.0.125 | 32400 | ✓ |
| plex 2 | tcp_udp | 32400 | 192.168.50.55 | 32400 | ✓ |
| qbittorrent | tcp_udp | 8085 | 192.168.50.97 | 8085 | ✓ |

## Résumé

- **Réseaux/VLANs :** 10
- **SSIDs WiFi :** 6
- **Équipements :** 21
- **Groupes firewall :** 15
- **Règles firewall :** 0
- **Port forwards :** 3
- **Routes statiques :** 0
- **VPN clients :** 0
