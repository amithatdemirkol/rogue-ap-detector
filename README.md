# Rogue AP Detector  
🛡 **Advanced Wireless Security Tool for Detecting Rogue Access Points**  

---

## 🚀 Project Description  
This project is an **advanced security tool that scans wireless networks and detects rogue access points (Rogue APs).**  
- Works on **Windows and Linux**  
- **Performs dynamic analysis** to identify unauthorized APs  
- **Real-time monitoring mode** continuously scans for Rogue APs  
- **Allowlist System** excludes trusted networks
- Generates reports in **CSV, TXT, and JSON formats**  

---

## 📌 Features  
✅ **Detects Wireless Networks** – Scans available Wi-Fi networks  
✅ **Identifies Rogue APs** – Detects multiple MAC addresses under the same SSID  
✅ **Allowlist Support** – Excludes trusted SSIDs from detection  
✅ **Real-Time Monitoring** – Runs scans every 30 seconds automatically  
✅ **Reports Findings** – Saves detected Rogue APs in **TXT, CSV, and JSON** formats  
✅ **Cross-Platform Compatibility** – Works on **Windows and Linux**   

---

## ⚙ Installation and Usage  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/amithatdemirkol/rogue-ap-detector.git
cd rogue-ap-detector
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run Rogue AP Detection
```sh
python main.py
```
#### 📌 One-time Rogue AP scan:
```sh
python main.py
```

#### 📌 Real-time monitoring (scans every 30 seconds):
```sh
python main.py --monitor
```

## 📊 Output and Reports  
####  📄 rogue_aps.txt – List of detected Rogue APs
####  📊 rogue_aps.csv – Detailed log compatible with Excel
####  📜 rogue_aps.json – JSON formatted report

## ⚠  Allowlist Usage

#### 📌 Add a new SSID to the allowlist:
```sh
echo "My_Home_WiFi" >> allowlist.txt
```

#### 📌 View the current allowlist:
```sh
cat allowlist.txt
```

#### 📌 Remove an SSID from the allowlist:
```sh
sed -i '/My_Home_WiFi/d' allowlist.txt
```
