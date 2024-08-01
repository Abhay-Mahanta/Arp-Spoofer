# ARP Spoofing Tool

This Python script performs ARP spoofing (also known as ARP poisoning) to intercept network traffic between two IP addresses. The tool is designed for educational purposes and should only be used in controlled environments where you have explicit permission to perform network tests. The script uses Scapy, a powerful Python library for network packet manipulation, to send ARP spoofing packets and manipulate ARP tables.

## Features

- **ARP Spoofing**: Continuously sends ARP spoofing packets to redirect traffic between the target IP and gateway IP.
- **Restore Function**: Restores the ARP tables to their original state when the script is interrupted.
- **Count Display**: Displays the number of spoofed packets sent in real-time.

## Requirements

- Python 3.x
- Scapy (install via `pip install scapy`)

## Usage

1. **Install Scapy**:
   ```bash
   pip install scapy

2. **Run the Script**:
   ```bash
   python your_script.py --target 192.168.92.134 --gateway 192.168.92.2




## Notes
- Legal Disclaimer: This tool should only be used for educational purposes and in environments where you have permission to perform network tests. Unauthorized use of this tool is illegal and unethical.
- Dependencies: Ensure that Scapy is properly installed and that you have the necessary permissions to send ARP packets on your network.
Feel free to customize the script and use it to learn more about network security and ARP spoofing.
