import csv
import json
import os
from datetime import datetime
from colorama import Fore, Style

def save_as_txt(rogue_aps, filename="rogue_aps.txt"):
    """ Rogue AP bilgilerini TXT dosyasına kaydeder. """
    if not rogue_aps:
        return
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=== Rogue AP Tespit Raporu ===\n")
        f.write(f"Tarih: {datetime.now()}\n\n")

        for ap in rogue_aps:
            f.write(f"SSID: {ap['SSID']}\n")
            f.write(f"Durum: {ap['Issue']}\n")
            f.write(f"BSSID'ler: {', '.join(ap['BSSIDs'])}\n")
            f.write("-" * 40 + "\n")

    print(f"{Fore.GREEN}[✓] Rogue AP raporu '{filename}' dosyasına kaydedildi.{Style.RESET_ALL}")

def save_as_csv(rogue_aps, filename="rogue_aps.csv"):
    """ Rogue AP bilgilerini CSV dosyasına kaydeder. """
    if not rogue_aps:
        return

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["SSID", "Durum", "BSSID'ler"])

        for ap in rogue_aps:
            writer.writerow([ap["SSID"], ap["Issue"], ", ".join(ap["BSSIDs"])])

    print(f"{Fore.GREEN}[✓] Rogue AP raporu '{filename}' dosyasına kaydedildi.{Style.RESET_ALL}")

def save_as_json(rogue_aps, filename="rogue_aps.json"):
    """ Rogue AP bilgilerini JSON formatında kaydeder. """
    if not rogue_aps:
        return
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(rogue_aps, f, indent=4)

    print(f"{Fore.GREEN}[✓] Rogue AP raporu '{filename}' dosyasına kaydedildi.{Style.RESET_ALL}")

def print_alerts(rogue_aps):
    """ Terminalde renkli uyarılar gösterir. """
    if not rogue_aps:
        print(f"{Fore.CYAN}[✓] Her şey normal, rogue AP bulunamadı.{Style.RESET_ALL}")
        return

    print(f"{Fore.RED}[!] Dikkat! Rogue AP tespit edildi!{Style.RESET_ALL}\n")
    for ap in rogue_aps:
        print(f"{Fore.YELLOW}SSID: {ap['SSID']}{Style.RESET_ALL}")
        print(f"{Fore.RED}Durum: {ap['Issue']}{Style.RESET_ALL}")
        print(f"BSSID'ler: {', '.join(ap['BSSIDs'])}\n")
        print("-" * 40)

if __name__ == "__main__":
    # Test için örnek rogue AP listesi
    sample_rogue_aps = [
        {"SSID": "Free_WiFi", "Issue": "Multiple MAC addresses detected", "BSSIDs": ["00:11:22:33:44:55", "66:77:88:99:AA:BB"]}
    ]

    print_alerts(sample_rogue_aps)
    save_as_txt(sample_rogue_aps)
    save_as_csv(sample_rogue_aps)
    save_as_json(sample_rogue_aps)
