# FTPgrabCredentials
This Python script is designed to monitor and analyze FTP traffic, specifically focusing on capturing FTP credentials (username and password) sent in clear text. The script uses NetfilterQueue to capture network packets and Scapy for packet parsing. It detects FTP commands and responses, then extracts sensitive information, such as the username and password, when applicable.
# FTP Sniffer for Username and Password Extraction 🐍🔍

This Python script captures and analyzes FTP packets, extracting **username** and **password** information from FTP login attempts. It uses **NetfilterQueue** to monitor network traffic and **Scapy** for packet parsing.

## Features ✨
- **FTP Traffic Analysis**: Captures FTP packets and analyzes commands like `USER` and `PASS`.
- **Credential Extraction**: Prints the username and password when a successful login (`230` response) is detected.
- **Real-Time Monitoring**: Uses **NetfilterQueue** to capture and analyze network traffic in real time.

## Requirements ⚙️

Before running the script, ensure you have the following Python packages installed:

- `scapy`
- `netfilterqueue`

To install the required packages, run the following command:

```bash
pip install scapy netfilterqueue
⚠️ Note: The script requires root privileges to capture network traffic.

Usage 🚀
Run the script with root privileges to start monitoring FTP traffic:

bash
Copia
Modifica
sudo python3 ftp_sniffer.py
The script will capture FTP packets and display the following:

Username and password when a successful login is detected (230 response).
Stop the script by pressing Ctrl+C.

Example Output 📊
Captured FTP Credentials: When a successful login is detected, the script will print the username and password:

bash
Copia
Modifica
USER : user123
PASS : password456
License 📜
This project is licensed under the MIT License.
Modifica
Form found: Username: ['user123'] Password: ['password456']
License 📜
This project is licensed under the MIT License.
