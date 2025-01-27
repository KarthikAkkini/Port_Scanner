# Basic Port Scanner

## Description
This is a simple Python script that scans the first 1024 TCP ports of a target machine to check for open ports. It is a beginner-friendly tool for basic network testing.

---

## Features:
- Scans ports from 1 to 1024.
- Basic TCP connection to check if ports are open.
- Displays open ports in real-time.

---

## Prerequisites:
- Python 3.x installed on your machine.
- A basic understanding of networking and ports.

---

## Installation

1. Clone the repository and navigate to the folder:
    ```bash
    git clone https://github.com/yourusername/Port_Scanner.git
    cd Port_Scanner/basic_port_scanner
    ```

2. Run the script:
    ```bash
    python3 Port_Scanner_v1.py <target_ip>
    ```

---

## Usage Example

Example command to scan the target IP `192.168.1.1`:
```bash
python3 Port_Scanner_v1.py 192.168.1.1
