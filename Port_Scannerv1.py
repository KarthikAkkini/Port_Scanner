import sys
import socket
from datetime import datetime

# Validate the target and print banner
if len(sys.argv) != 2:
    print("Syntax: python3 scanner.py <ip>")
    sys.exit(1)

try:
    target = socket.gethostbyname(sys.argv[1])
    print("-" * 80)
    print("Scanning target:", target)
    print("Time Started:", datetime.now())
    print("-" * 80)
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit(1)

# Scan ports
try:
    for port in range(1024):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
                s.close()
except KeyboardInterrupt:
    print("\nExiting Program.")
    sys.exit(1)
except Exception as e:
    print("Error:", e)
    sys.exit(1)
