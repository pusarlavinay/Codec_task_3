# 🛠️ Pentesting Toolkit

A **Python-based penetration testing toolkit** designed with modularity and simplicity in mind.  
This toolkit includes multiple modules such as a **Port Scanner**, **HTTP Info Grabber**, and **Password Auditor**, making it a lightweight but powerful utility for basic security assessments.  

⚠️ **Disclaimer:** This toolkit is for **educational purposes only**. Use it **only on systems you are authorized to test**.

---

## ✨ Features
- 🔍 **Port Scanner** – Scans open ports on a given host.  
- 🌐 **HTTP Info Grabber** – Fetches server headers and HTTP response details.  
- 🔑 **Password Auditor** – Tests password strength against common rules.  
- 🧩 **Modular Design** – Easy to extend with new modules.  

---

## 📂 Project Structure
pentoolkit/
│── core.py # Main menu runner
│── http_info.py # HTTP info script
│── port_scanner.py # Standalone port scanner
│── passwd_audit.py # Password auditor
│── requirements.txt # Dependencies
│
├── modules/
│ └── port_scanner.py # Scanner logic (modular)
│
├── reports/ # Optional: Generated reports
├── utils/ # Helper functions
└── venv/ # Virtual environment (ignored in Git)


---

## ⚡ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pentoolkit.git
   cd pentoolkit


Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows


Install dependencies:

pip install -r requirements.txt

🚀 Usage

Run the toolkit with:

python3 core.py


=== Penetration Testing Toolkit ===
1. Port Scanner
2. HTTP Info
3. Password Audit
4. Exit



📦 Requirements

Python 3.8+

Packages (already in requirements.txt):

requests
colorama



🤝 Contribution

Want to add more modules (like a brute-forcer or directory scanner)? Fork this repo and submit a pull request!

Author:
Pusarla Vinay
