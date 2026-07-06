# 📊 Analytics & Security Scripts

## Description

A comprehensive collection of Python scripts for security analytics, log analysis, and system data processing. This module provides automated tools for parsing security logs, detecting anomalies, and tracking authorization events.

## Content

- **Log Analysis:** Parse failed login attempts, track access patterns, analyze authorization events
- **Network Reconnaissance:** Packet analysis, port scanning, network topology mapping
- **Access Control:** User filtering, permission auditing, ACL validation
- **Threat Detection:** Anomaly detection, threat scoring, correlation analysis

## Scripts

### Log Analysis

- `failed_login.py` — Extract and analyze failed authentication attempts
- `access_logs.py` — Parse system access patterns and identify anomalies
- `auth_events.py` — Track and correlate authorization events

### Network Analysis

- `analyse_paquets.py` — Packet capture analysis and traffic inspection
- `port_scan.py` — Network service discovery and port enumeration
- `network_mapper.py` — Discover and map network topology

### Access Control

- `filtrage_utilisateurs.py` — Filter and validate user access
- `permission_audit.py` — Audit file and directory permissions
- `access_control.py` — Validate ACL enforcement and compliance

### Threat Detection

- `threat_detection.py` — Analyze security events and score threats
- `anomaly_detection.py` — Identify deviations from baseline behavior

## Technical Documentation

For detailed integration and security considerations, see:
- [Main README](../README.md)
- [MCP Security Fix](../docs/MCP_SECURITY_FIX.md)

## Cross-References

- **Infrastructure Hub:** [sovereign-ai-infrastructure](https://github.com/Dinaverse/sovereign-ai-infrastructure)
- **Security Agents:** [cybersecurity-lab-automation](https://github.com/Dinaverse/cybersecurity-lab-automation)
- **Related Scripts:** [python-security-analytics](https://github.com/Dinaverse/python-security-analytics)

## Usage

All scripts are designed to run as standalone tools or integrated into security workflows:

```bash
# Analyze failed logins
python3 failed_login.py --log /var/log/auth.log

# Scan network
python3 network_mapper.py --subnet 192.168.1.0/24

# Audit permissions
python3 permission_audit.py --path /home --recursive
```

---

*Automating security analysis. Defending through intelligence.*
