import re
from collections import defaultdict

def analyze_server_logs(file_path, alert_threshold=3):
    
    failed_attempts = defaultdict(int)

    print("Analyzing 16-bit server logs for brute-force attacks...\n")

    try:
        
        with open(file_path, 'r') as log_file:
            for line in log_file:
               
                if "Failed password" in line:
                   
                    ip_search = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                    
                    if ip_search:
                        attacker_ip = ip_search.group(1)
                        
                    
                        failed_attempts[attacker_ip] += 1

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return

    # Generate the final security report
    print("--- AUTOMATED SECURITY ALERT REPORT ---")
    for ip, count in failed_attempts.items():
        if count >= alert_threshold:
            print(f"[CRITICAL ALERT] IP {ip} flagged! {count} failed attempts. Possible Brute-Force.")
        else:
            print(f"[LOG] IP {ip} had {count} failed attempt(s). Normal user error.")


analyze_server_logs('arcade_auth.log')