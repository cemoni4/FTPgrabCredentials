# FTPgrabCredentials
This Python script captures HTTP packets, decompresses GZIP-encoded responses, and extracts form data (such as usernames and passwords) from POST requests. It uses Scapy for packet parsing and NetfilterQueue for real-time traffic monitoring.
# Packet Sniffer for GZIP Decompression and Form Data Extraction 🐍🔍

This Python script captures HTTP packets, decompresses GZIP-encoded responses, and extracts form data (such as usernames and passwords) from POST requests. It uses **Scapy** for packet parsing and **NetfilterQueue** for real-time traffic monitoring.

## Features ✨
- **GZIP Decompression**: Decompresses GZIP-encoded HTTP responses.
- **Form Data Extraction**: Extracts **username** and **password** from POST requests.
- **Real-Time Monitoring**: Uses **NetfilterQueue** for live packet monitoring.

## Requirements ⚙️

Before running the script, ensure you have the following Python packages installed:

- `scapy`
- `netfilterqueue`
- `zlib`
- `urllib.parse`

To install the required packages, run the following command:

```bash
pip install scapy netfilterqueue
⚠️ Note: The script requires root privileges to capture network traffic.

Usage 🚀
Run the script with root privileges to start monitoring HTTP traffic:

bash
Copia
Modifica
sudo python3 packet_sniffer.py
The script will display:

GZIP-encoded data in HTTP responses.
Form data (e.g., username and password) from HTTP POST requests.
Stop the script by pressing Ctrl+C.

Example Output 📊
GZIP Detected: The script will print a message when it detects GZIP-encoded data.

bash
Copia
Modifica
GZIP data detected in the response.
Form Data Extracted: If form data is successfully extracted, it will display the username and password.

bash
Copia
Modifica
Form found: Username: ['user123'] Password: ['password456']
License 📜
This project is licensed under the MIT License.
