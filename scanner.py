import subprocess
import platform
import re

def get_wifi_networks():
    """ Çevredeki Wi-Fi ağlarını tarar ve SSID, BSSID, Sinyal Gücü bilgilerini döndürür. """
    system = platform.system()
    networks = []

    try:
        if system == "Windows":
            output = subprocess.check_output(["netsh", "wlan", "show", "networks", "mode=Bssid"], encoding="utf-8", errors="ignore")
            networks = parse_windows_output(output)
        elif system == "Linux":
            output = subprocess.check_output(["nmcli", "-t", "-f", "SSID,BSSID,SIGNAL", "dev", "wifi"], encoding="utf-8", errors="ignore")
            networks = parse_linux_output(output)
        else:
            print("Bu işletim sistemi desteklenmiyor.")
            return []
    except subprocess.CalledProcessError as e:
        print("Komut çalıştırma hatası:", e)
        return []

    return networks

def parse_windows_output(output):
    """ Windows çıktısını analiz eder ve temiz bir formatta döndürür. """
    networks = []
    ssid = None

    for line in output.split("\n"):
        ssid_match = re.search(r"SSID \d+ : (.+)", line)
        bssid_match = re.search(r"BSSID \d+ : (.+)", line)
        signal_match = re.search(r"Signal\s+: (\d+)%", line)

        if ssid_match:
            ssid = ssid_match.group(1)
        elif bssid_match and ssid:
            networks.append({
                "SSID": ssid,
                "BSSID": bssid_match.group(1),
                "Signal": signal_match.group(1) if signal_match else "N/A"
            })

    return networks

def parse_linux_output(output):
    """ Linux çıktısını analiz eder ve temiz bir formatta döndürür. """
    networks = []
    for line in output.strip().split("\n"):
        parts = line.split(":")
        if len(parts) == 3:
            ssid, bssid, signal = parts
            networks.append({
                "SSID": ssid,
                "BSSID": bssid,
                "Signal": signal
            })
    return networks

if __name__ == "__main__":
    wifi_networks = get_wifi_networks()
    for net in wifi_networks:
        print(net)
