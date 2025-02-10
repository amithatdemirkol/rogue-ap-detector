def load_allowlist():
    """ Beyaz listeyi (Allowlist) yükler ve bir set olarak döndürür. """
    try:
        with open("allowlist.txt", "r") as file:
            return set(line.strip() for line in file if line.strip())
    except FileNotFoundError:
        print("[INFO] allowlist.txt bulunamadı, beyaz liste boş.")
        return set()

def is_allowed(ssid):
    """ Belirtilen SSID'nin beyaz listede olup olmadığını kontrol eder. """
    allowlist = load_allowlist()
    return ssid in allowlist
