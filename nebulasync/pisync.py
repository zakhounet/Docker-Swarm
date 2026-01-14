import requests
import time
import sys

# Configuration de la chaîne HA - IP Validées par la Memory
PRIMARY_URL = "http://192.168.50.36" # VIP du Pi4 Master
REPLICAS = [
    "http://192.168.50.62:8080",     # Replica sur Zakh (docker-manager-02)
    "http://192.168.50.61:8080"      # Replica sur Tom (docker-manager-01)
]
PASSWORD = "password"

def get_sid(url):
    try:
        r = requests.post(f"{url}/api/auth", json={"password": PASSWORD}, timeout=5)
        data = r.json()
        if r.status_code == 200 and data.get("session", {}).get("valid"):
            return data["session"]["sid"]
    except: return None

def logout(url, sid):
    try: requests.delete(f"{url}/api/auth", headers={"sid": sid}, timeout=2)
    except: pass

def sync_to_target(sid_p, target_url):
    sid_r = get_sid(target_url)
    if not sid_r:
        print(f" ERROR: Impossible de joindre le Replica {target_url}")
        return

    try:
        # 1. SYNCHRO DNS (Hosts + CNAMEs)
        cfg_p = requests.get(f"{PRIMARY_URL}/api/config", headers={"sid": sid_p}, timeout=5).json()
        dns_p = cfg_p["config"]["dns"]
        
        payload_dns = {
            "config": {
                "dns": {
                    "hosts": dns_p.get("hosts", []),
                    "cnameRecords": dns_p.get("cnameRecords", [])
                }
            }
        }
        requests.patch(f"{target_url}/api/config", headers={"sid": sid_r}, json=payload_dns, timeout=5)

        # 2. SYNCHRO AD-LISTS
        lists_p = requests.get(f"{PRIMARY_URL}/api/adlists", headers={"sid": sid_p}).json().get("adlists", [])
        lists_r = requests.get(f"{target_url}/api/adlists", headers={"sid": sid_r}).json().get("adlists", [])
        urls_r = [l['address'] for l in lists_r]
        
        added = 0
        for l in lists_p:
            if l['address'] not in urls_r:
                requests.post(f"{target_url}/api/adlists", headers={"sid": sid_r}, json={
                    "address": l['address'], 
                    "comment": "Sync from Pi4 Master", 
                    "enabled": l.get('enabled', True)
                })
                added += 1
        
        print(f" SUCCESS [{target_url}]: DNS synchronisé. {added} Ad-lists ajoutées.")
        
        if added > 0:
            print(f" INFO [{target_url}]: Mise à jour Gravity en cours...")
            requests.post(f"{target_url}/api/gravity", headers={"sid": sid_r})

    except Exception as e:
        print(f" ERROR sur {target_url}: {e}")
    finally:
        logout(target_url, sid_r)

def main():
    print(f"--- PiSync-V6 Triple-HA (DNS + Ad-lists) Started ---")
    while True:
        sid_p = get_sid(PRIMARY_URL)
        if sid_p:
            for target in REPLICAS:
                sync_to_target(sid_p, target)
            logout(PRIMARY_URL, sid_p)
        else:
            print(f" CRITICAL: Master Pi4 (VIP {PRIMARY_URL}) injoignable.")
        
        sys.stdout.flush()
        time.sleep(1500)

if __name__ == "__main__":
    main()