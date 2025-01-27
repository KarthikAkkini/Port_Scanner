import sys
import socket
import threading
from datetime import datetime

# Validate the number of arguments
if len(sys.argv) != 4:
    print("Usage: python3 scanner.py <ip> <start_port> <end_port>")
    sys.exit(1)

# Extract the arguments
target = sys.argv[1]

try:
    start_port = int(sys.argv[2])  # Convert to integer
    end_port = int(sys.argv[3])  # Convert to integer
except ValueError:
    print("Error: Ports must be integers.")
    sys.exit(1)

# Print banner information
try:
    target = socket.gethostbyname(target)
    print("-" * 80)
    print(f"Scanning Target: {target}")
    print(f"Time Started: {datetime.now()}")
    print("-" * 80)
except socket.gaierror:
    print("Error: Hostname could not be resolved.")
    sys.exit(1)

# Function to scan a single port
def scan_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
    except Exception as e:
        pass  # Ignore other exceptions (e.g., connection errors)

# Function to handle multi-threading
def scan_ports_in_range():
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(port,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

# Start scanning
scan_ports_in_range()
