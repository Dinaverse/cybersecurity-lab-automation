# 🛡️ Cybersecurity Lab Automation — Analytics Suite

> *Python security analytics and autonomous agents for real-time log monitoring, network reconnaissance, and threat analysis on the Kali-Master node.*

---

## 🎯 Overview

This directory contains the **security analytics suite** — Python scripts and tools for automated log parsing, network scanning, access control analysis, and threat detection.

**Status:** ✅ Active — 40+ scripts operational

---

## 📦 Content Organization

### Security Analysis Scripts
- **/security** — Log analysis, network reconnaissance, access control
- **/math_and_data** — Mathematical computations and data analysis (NumPy)
- **/programming_exercises** — Data structure manipulation and algorithm practice

---

## 🛠️ Core Analytics Tools

### Log Analysis
- `failed_login.py` — Parse and analyze failed authentication attempts
- `access_logs.py` — Analyze system access patterns and anomalies
- `auth_events.py` — Track authorization events and permission changes

### Network Reconnaissance
- `analyse_paquets.py` — Packet capture and analysis
- `port_scan.py` — Network service discovery and enumeration
- `network_mapper.py` — LAN topology mapping and asset discovery

### Access Control
- `filtrage_utilisateurs.py` — User access filtering and validation
- `permission_audit.py` — Permission compliance checking
- `access_control.py` — ACL enforcement verification

### Threat Detection
- `threat_detection.py` — Anomaly detection and threat correlation
- Pattern matching for known attack signatures
- Behavioral analysis for zero-day detection

---

## 💻 Usage

All scripts are standalone Python 3 tools with minimal external dependencies (NumPy for data analysis modules only).

```bash
# Log analysis example
python3 failed_login.py --logfile /var/log/auth.log --threshold 5

# Network scanning
python3 network_mapper.py --interface eth0 --subnet 192.168.1.0/24

# Access control audit
python3 permission_audit.py --path /home --recursive
```

---

## 🔗 Integration

These analytics scripts integrate with:
- **Security-Ops Agent** — Autonomous log monitoring and incident response
- **Net-Analyzer Agent** — Hourly network reconnaissance
- **MCP Bridge** — Direct AI agent integration via Model Context Protocol
- **NVIDIA Morpheus** — AI-powered security data processing pipeline

---

## 📚 Related Documentation

- **Main Repository:** [cybersecurity-lab-automation](../README.md)
- **Infrastructure Hub:** [sovereign-ai-infrastructure](https://github.com/Dinaverse/sovereign-ai-infrastructure)
- **AI Integration:** [python-security-analytics](https://github.com/Dinaverse/python-security-analytics)
- **MCP Security Fix:** [MCP_SECURITY_FIX.md](../docs/MCP_SECURITY_FIX.md)

---

*Security through automation. Defense through analytics.*