import datetime

LOG_FILE = "rogue_ap_log.txt"

def log_rogue_ap(rogue_aps):
    """ Rogue AP'leri log dosyasına yazar. """
    with open(LOG_FILE, "a") as file:
        for ap in rogue_aps:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{timestamp}] SSID: {ap['SSID']} | BSSID: {ap['BSSID']} | Kanal: {ap['Channel']} | Güç: {ap['Signal']}\n"
            file.write(log_entry)

        print(f"[LOG] {len(rogue_aps)} adet Rogue AP tespit edildi ve kaydedildi.")
