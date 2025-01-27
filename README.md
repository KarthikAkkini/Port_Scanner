# Port Scanner Repository

This repository contains two Python-based port scanner projects designed for network security testing. The goal of these scripts is to help users identify open ports on target machines, making them useful for network administrators and cybersecurity professionals.

## Repository Structure:

- **basic_port_scanner**: Contains the basic version of the port scanner.
- **improved_port_scanner**: Contains the improved version of the port scanner with additional features.

---

## Project Overviews

### 1. **Basic Port Scanner**  
- Scans the first 1024 TCP ports of a target machine.  
- Simple implementation using basic TCP connections.  
- Great for beginners or quick network testing.  

### 2. **Improved Port Scanner**  
- Adds functionality to scan a custom range of ports.  
- Implements multithreading for faster scanning.  
- Enhanced error handling and usability.  

---

## How to Use

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/Port_Scanner.git
    ```

2. Navigate to the desired project folder:
    ```bash
    cd Port_Scanner/basic_port_scanner
    ```

3. Run the script with Python:
    ```bash
    python3 Port_Scanner_v1.py <target_ip>
    ```

4. For the improved version, navigate to its folder:
    ```bash
    cd Port_Scanner/improved_port_scanner
    ```
    And run:
    ```bash
    python3 Port_Scanner.py <target_ip> <start_port> <end_port>
    ```

---

## Contribution Guidelines

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a branch for your feature (`git checkout -b feature-name`).
3. Commit your changes and push them to your fork.
4. Create a pull request for review.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
