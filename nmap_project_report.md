Nmap Vulnerability Scanning Project

Target: 192.168.95.132 (My Kali Linux Machine)
1️⃣ Basic Scan

Command:

sudo nmap 192.168.95.132 -oN basic_scan.txt

Result:

    Host is up.

    All 1000 scanned ports are closed.

Key Output:

All 1000 scanned ports on 192.168.95.132 are in ignored states.
Not shown: 1000 closed tcp ports (reset)

2️⃣ Network Discovery (Ping Scan)

Command:

sudo nmap -sn 192.168.95.0/24 -oN network_discovery.txt

Result:

    4 devices detected on the network:

IP Address	MAC Address	Vendor (if available)
192.168.95.20	06:53:2B:9C:E7:A9	Unknown
192.168.95.92	F6:FF:15:CB:CE:B9	Unknown
192.168.95.116	CC:2F:71:C8:FB:45	Intel Corporate
192.168.95.132	This machine (Kali)	-
3️⃣ SYN Port Scan

Command:

sudo nmap -sS 192.168.95.132 -oN syn_scan.txt

Result:

    Host is up.

    All 1000 scanned TCP ports are closed.

Key Output:

All 1000 scanned ports on 192.168.95.132 are in ignored states.
Not shown: 1000 closed tcp ports (reset)

4️⃣ Vulnerability Script Scan

Command:

sudo nmap --script vuln 192.168.95.132 -oN vuln_scan.txt

Result:

    Host is up.

    No open ports were found, so no vulnerabilities detected.

Key Output:

All 1000 scanned ports on 192.168.95.132 are in ignored states.
Not shown: 1000 closed tcp ports (reset)

🔎 Summary of Findings

    ✅ The Kali machine is online but has no open ports exposed on the standard 1000 TCP ports.

    ✅ The local network has 4 active devices.

    🚫 No vulnerabilities were detected because no ports were open.

📈 Reflection

The scan results show that my system is secure by default with no services exposed to the network. This is a good baseline security posture. Future tests can involve intentionally opening ports (e.g., running a web server or SSH) to practice scanning real services.
