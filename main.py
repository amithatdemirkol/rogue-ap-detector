import argparse
from monitor import monitor_rogue_aps
from scanner import get_wifi_networks
from analyzer import detect_rogue_aps
from reporter import print_alerts, save_as_txt, save_as_csv, save_as_json

def main():
    parser = argparse.ArgumentParser(description="Rogue AP Tespit Aracı")
    parser.add_argument("--monitor", action="store_true", help="Gerçek zamanlı izlemeyi başlat")
    args = parser.parse_args()

    if args.monitor:
        monitor_rogue_aps()
    else:
        print("\n🔍 Rogue AP Tespit Aracı Çalışıyor...\n")
        networks = get_wifi_networks()
        rogue_aps = detect_rogue_aps(networks)

        print_alerts(rogue_aps)
        save_as_txt(rogue_aps)
        save_as_csv(rogue_aps)
        save_as_json(rogue_aps)

if __name__ == "__main__":
    main()
