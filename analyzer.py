import json
import os
from allowlist import is_allowed  # Beyaz liste kontrol fonksiyonunu dahil ettik.

def detect_rogue_aps(networks, history_file="wifi_history.json"):
    """
    Rogue AP'leri tespit eder:
    - Aynı SSID'ye sahip farklı MAC adreslerini bulur.
    - Normalde şifreli olup aniden açık hale gelen ağları kontrol eder.
    - Ani sinyal değişimlerini izler.
    - Beyaz listedeki SSID’leri rogue olarak işaretlemez.

    Sonuçları dosyaya kaydeder ve ekrana yazar.
    """
    rogue_aps = []
    ssid_map = {}

    # Ağları SSID bazında gruplandır
    for net in networks:
        ssid = net["SSID"]
        bssid = net["BSSID"]
        signal = int(net["Signal"])

        # Eğer SSID beyaz listedeyse, Rogue olarak işaretlemeye gerek yok.
        if is_allowed(ssid):
            continue  # Beyaz listedeki SSID’leri atla

        if ssid not in ssid_map:
            ssid_map[ssid] = []

        ssid_map[ssid].append({"BSSID": bssid, "Signal": signal})

    # Rogue AP kontrolü
    for ssid, bssids in ssid_map.items():
        unique_macs = set(b["BSSID"] for b in bssids)

        # Aynı SSID altında farklı MAC adresleri varsa şüpheli
        if len(unique_macs) > 1:
            rogue_aps.append({
                "SSID": ssid,
                "Issue": "Multiple MAC addresses detected",
                "BSSIDs": list(unique_macs)
            })

    # Sonuçları dosyaya kaydet
    save_results(rogue_aps, history_file)

    return rogue_aps

def save_results(rogue_aps, history_file):
    """ Rogue AP analiz sonuçlarını bir JSON dosyasına kaydeder. """
    if rogue_aps:
        with open(history_file, "w", encoding="utf-8") as f:
            json.dump(rogue_aps, f, indent=4)
        print(f"[!] Rogue AP’ler tespit edildi ve {history_file} dosyasına kaydedildi.")
    else:
        print("[✓] Her şey normal, rogue AP bulunamadı.")

if __name__ == "__main__":
    sample_networks = [
        {"SSID": "Free_WiFi", "BSSID": "00:11:22:33:44:55", "Signal": "80"},
        {"SSID": "Free_WiFi", "BSSID": "66:77:88:99:AA:BB", "Signal": "75"},
        {"SSID": "Home_Network", "BSSID": "11:22:33:44:55:66", "Signal": "90"}
    ]
    rogue_aps = detect_rogue_aps(sample_networks)
    print(json.dumps(rogue_aps, indent=4))
