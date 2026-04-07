# 🕹️ Retro Boy Arcade: Security Audit & Defensive Tools

## 📝 Overview
This repository contains a suite of custom Python scripts developed as an educational internship project. The objective was to design, build, and deploy entry-level corporate security tools for a simulated environment: the backend infrastructure of a classic 16-bit high-score database.

This project demonstrates practical knowledge in three core pillars of cybersecurity:
1. **Infrastructure Security:** Automated vulnerability identification.
2. **Defensive Monitoring:** Log parsing and brute-force detection.
3. **Application Security:** Cryptographic password hashing and salting.

---

## 🛠️ The Arsenal (Projects Included)

### 1. Vulnerability Scanner (`vuln_scanner.py`)
A simulated infrastructure auditing tool. It cross-references the server's installed software packages against a threat intelligence database of known vulnerabilities (CVEs).
* **Key Skills:** Dictionary data structures, conditional logic, automated remediation reporting.
* **Outcome:** Successfully flags outdated versions of Apache (CVE-2021-41773) and OpenSSH (CVE-2016-6210) and generates an actionable patch report for system administrators.

### 2. Automated Log Analyzer (`log_analyzer.py`)
A defensive monitoring script designed to parse server authentication logs and identify potential brute-force attacks in real-time.
* **Key Skills:** File I/O, Regular Expressions (Regex), IP extraction, threshold alerting.
* **Outcome:** Reads `arcade_auth.log`, tracks failed login attempts by IP address, and triggers a `[CRITICAL ALERT]` if an IP exceeds the predefined failure threshold, distinguishing between normal user error and malicious intent.

### 3. Cryptographic Password Hasher (`password_crypto.py`)
A secure authentication module that enforces password complexity and protects user credentials from data breaches and Rainbow Table attacks.
* **Key Skills:** Cryptography (`hashlib`), randomized salting (`secrets`), password complexity validation.
* **Outcome:** Rejects weak passwords, generates a 16-byte randomized hex salt, and outputs a highly secure SHA-256 hash for safe database storage.

---

## 🚀 How to Run the Tools

These scripts are written in standard Python 3 and require no external dependencies. 

To run any of the scripts, clone the repository and execute them via the terminal:

**Run the Vulnerability Scanner:**
python vulnerability-scanning/vuln_scanner.py


**Run the Log Analyzer:**

python log-analysis/log_analyzer.py

**Run the Cryptography Module:**
python cryptography/password_crypto.py
