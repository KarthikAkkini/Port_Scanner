
---

### **3. README.md for `improved_port_scanner` Folder**  

**Path:** `/improved_port_scanner/README.md`

```markdown
# Improved Port Scanner

## Description
This is an enhanced version of the basic port scanner. It allows users to specify a custom port range and uses multithreading to speed up the scanning process.

---

## Features:
- Customizable port range for scanning.
- Multithreading for faster scans.
- Displays open ports in real-time.
- Improved error handling.

---

## Prerequisites:
- Python 3.x installed on your machine.
- A basic understanding of networking and ports.
- Knowledge of multithreading concepts (optional).

---

## Installation

1. Clone the repository and navigate to the folder:
    ```bash
    git clone https://github.com/yourusername/Port_Scanner.git
    cd Port_Scanner/improved_port_scanner
    ```

2. Run the script:
    ```bash
    python3 Port_Scanner.py <target_ip> <start_port> <end_port>
    ```

---

## Usage Example

Example command to scan ports 80 to 100 on the target IP `192.168.1.1`:
```bash
python3 Port_Scanner.py 192.168.1.1 80 100
