import time
from scanner import get_wifi_networks
from analyzer import detect_rogue_aps
from reporter import print_alerts, save_as_txt, save_as_csv, save_as_json
from colorama import Fore, Style

DETECTION_INTERVAL = 30  # 30 saniyede bir tarama yapacak

def monitor_rogue_aps():
    """ Gerçek zamanlı olarak Rogue AP tespiti yapar. """
    print(f"{Fore.CYAN}[INFO] Gerçek zamanlı Rogue AP izleme başlatıldı...{Style.RESET_ALL}")

    previous_rogue_aps = set()  # Önceki tespitleri takip etmek için set kullanıyoruz.

    while True:
        networks = get_wifi_networks()
        rogue_aps = detect_rogue_aps(networks)

        if rogue_aps:
            # Yeni tespitleri eski kayıtlarla karşılaştır
            new_rogue_aps = {ap["SSID"] for ap in rogue_aps} - previous_rogue_aps

            if new_rogue_aps:
                print(f"{Fore.RED}[ALERT] Yeni Rogue AP Tespit Edildi!{Style.RESET_ALL}")
                print_alerts(rogue_aps)

                save_as_txt(rogue_aps)
                save_as_csv(rogue_aps)
                save_as_json(rogue_aps)

            previous_rogue_aps = {ap["SSID"] for ap in rogue_aps}  # Güncelle
        else:
            print(f"{Fore.GREEN}[✓] Şu an için herhangi bir Rogue AP tespit edilmedi.{Style.RESET_ALL}")

        time.sleep(DETECTION_INTERVAL)  # Belirlenen süre kadar bekle

if __name__ == "__main__":
    monitor_rogue_aps()
