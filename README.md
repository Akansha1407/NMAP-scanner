# NMAP-scanner using Python Programming
The primary objective of this project is to build a network scanning tool using Python and Nmap that can:
•	Automating Network Scanning: Build a Python application that automates the process of scanning a target network to identify live hosts, open ports, and running services, providing similar functionality to Nmap but with a custom implementation.
•	Port and Service Detection: Implement the ability to scan a range of ports and identify services running on those ports (e.g., HTTP, FTP, SSH). The tool should also be able to determine the versions of those services to help assess security risks.
•	Operating System Detection: Implement basic OS fingerprinting techniques to detect the operating system of the target devices based on their network behavior and responses to scan probes.
•	Basic Vulnerability Assessment: Integrate basic vulnerability scanning features, such as identifying open ports that are commonly targeted by attackers or detecting outdated services that may have known security vulnerabilities.
•	Concurrency for Speed: Utilize multi-threading or asynchronous programming in Python to perform network scans concurrently. This will speed up the scanning process, especially when dealing with large networks or multiple target hosts.
•	User-Friendly Command-Line Interface (CLI): Create a simple and intuitive command-line interface (CLI) for users to easily input scan parameters such as target IP addresses, port ranges, scan types, and other settings.

# NMAP
Nmap is one of the most widely used network scanning tools in cybersecurity. According to the research by Fyodor, the creator of Nmap, the tool provides highly customizable scanning techniques, including service version detection, OS detection, and scripting engine capabilities. 
Nmap, originally developed by Gordon Lyon in 1997, has become the de facto standard for network scanning. It is used for tasks like:
•	Host discovery: Identifying live systems in a network.
•	Port scanning: Checking which ports are open or closed on a target machine.
•	Service and version detection: Identifying the services running on open ports and determining their version.
•	Operating system fingerprinting: Determining the target machine's operating system based on TCP/IP stack behaviour.
•	Vulnerability scanning: Detecting weak points in services running on open ports.

# System Requirement 
•	Hardware Requirements:
•	A system (Windows, Linux, or macOS) with at least 2 GB of RAM and a multi-core processor.
•	Stable network connection for running scans over a local network or remote targets.
•	Software Requirements:
•	Operating System: Windows 10/11, Linux (Ubuntu/Debian), or macOS.
•	Python: Version 3.7 or higher.
•	Nmap: Latest version of Nmap installed (available from nmap.org).
•	Libraries: python-nmap, subprocess (for handling Nmap execution), os, json, threading (for multi-threading support).

# references:-
Hackersploit NMAP tutorials
David bombal subnetting tutorials
NMAP official documentation

