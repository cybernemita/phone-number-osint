# 📞 Phone Number OSINT Tool
### by CyberNemita

Free & legal Phone Number Information (OSINT) tool for Termux and Linux.
This tool extracts **basic public information** related to a phone number.

---

## 🔍 What Information This Tool Provides
- ✅ Phone number validation
- 🌍 Country / Region information
- 📡 Original Carrier (SIM provider at time of number allocation)
- 📱 National & International number format
- ⏰ Timezone (Advanced mode)

---

## ⚠️ Important Note About SIM / Carrier Information

This tool uses Google's **libphonenumber** database.

🔴 **Carrier shown is NOT always the current SIM provider.**

### Why?
- Mobile numbers can be **ported** between operators
- Public OSINT databases store **original allocation data**
- Live SIM data is **private telecom information**

📌 Example:
- Number originally bought from **Airtel**
- Later ported to **Jio**
- Tool will still show **Airtel**

✅ This is a **technical limitation**, not a bug.

---

## 🛠 Requirements
- Termux (F-Droid version recommended)
- Python 3
- Internet connection

---

## 🚀 One-Time Setup (Auto Install)

```bash
pkg update && pkg upgrade -y
pkg install git python -y
git clone https://github.com/cybernemita/phone-number-osint
cd phone-number-osint
pip install -r requirements.txt
chmod +x phone-osint.sh

Run Tool (Single Command)
Copy code
Bash
./phone-osint.sh


⚖️ Legal Disclaimer
This tool is developed for educational and legal OSINT purposes only.
❌ Do NOT use for:
Harassment
Stalking
Illegal surveillance
Privacy violation
The author CyberNemita is not responsible for misuse.
⭐ Support
If you find this project useful:
Give it a ⭐ on GitHub
Share with students & learners
