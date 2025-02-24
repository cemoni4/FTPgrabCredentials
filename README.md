# FTP Credential Sniffer Tool 🛡️

## Description 📘
This project is a Python script that uses `netfilterqueue` and `scapy` to capture and analyze FTP traffic. It extracts and prints FTP credentials (username and password) when users attempt to log in.

## Features ⚡
- **FTP Packet Interception**: Captures FTP traffic using a Netfilter queue.
- **Credential Logging**: Extracts and prints usernames and passwords sent over FTP.
- **Real-Time Monitoring**: Continuously monitors packets and displays results live.

## Requirements 🛠️
- Python 3
- Libraries:
  - `netfilterqueue`
  - `scapy`

Install the required libraries with:
```bash
pip install netfilterqueue scapy
```

## Firewall Configuration 🔥
To make the script work, you need to set up an iptables rule to forward traffic to the Netfilter queue:
```bash
iptables -I FORWARD -j NFQUEUE --queue-num 1
```

For local testing:
```bash
iptables -I OUTPUT -j NFQUEUE --queue-num 1
iptables -I INPUT -j NFQUEUE --queue-num 1
```

After running the script, you can reset the rules with:
```bash
iptables --flush
```

## Execution ▶️
Run the script with:
```bash
sudo python3 FTP.py
```

## Warning ⚠️
Running this script requires superuser privileges and modifies firewall rules. FTP transmits credentials in plaintext, so this tool demonstrates how attackers can intercept sensitive data. Use responsibly and only in controlled environments for educational or testing purposes!

## License 📄
Distributed under the MIT License.

---
