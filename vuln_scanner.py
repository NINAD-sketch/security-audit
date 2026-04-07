import datetime

def scan_retro_server_software():
    print("=" * 60)
    print("🔴 RETRO BOY SECURE VULNERABILITY SCANNER 🔴")
    print(f"Scan Initiated: {datetime.datetime.now()}")
    print("=" * 60)

    
    installed_software = {
        "Apache Web Server": "2.4.49",
        "MySQL Database": "8.0.26",
        "OpenSSH": "7.2p2",
        "Leaderboard API": "1.0.0"
    }

    
    cve_database = {
        "Apache Web Server": {
            "vulnerable_version": "2.4.49", 
            "cve": "CVE-2021-41773", 
            "severity": "CRITICAL",
            "fix": "Update to version 2.4.51"
        },
        "OpenSSH": {
            "vulnerable_version": "7.2p2", 
            "cve": "CVE-2016-6210", 
            "severity": "HIGH",
            "fix": "Update to version 7.3 or higher"
        }
    }

    vulnerabilities_found = 0

    print("\n[*] Scanning installed packages against threat database...\n")
    
    
    for software, version in installed_software.items():
        print(f"    Checking {software} v{version}...")
        
        if software in cve_database:
            if version == cve_database[software]["vulnerable_version"]:
                print(f"    [!] ALERT: Match found in vulnerability database!")
                vulnerabilities_found += 1

    
    print("\n" + "-" * 60)
    print("SCAN COMPLETE: REMEDIATION REPORT")
    print("-" * 60)

    if vulnerabilities_found > 0:
        print(f"WARNING: {vulnerabilities_found} vulnerability(ies) detected on the server.")
        for software, data in cve_database.items():
            if installed_software.get(software) == data["vulnerable_version"]:
                print(f"\nSoftware: {software}")
                print(f"Severity: {data['severity']}")
                print(f"CVE ID:   {data['cve']}")
                print(f"Action:   {data['fix']}")
    else:
        print("System secure. No known vulnerabilities detected.")
        
    print("=" * 60)


scan_retro_server_software()