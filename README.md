# 🛡️ Cybersecurity Lab Automation

> *Autonomous AI agents, security analytics scripts, and MCP bridge integration for automated log monitoring, network reconnaissance, and security analysis.*

---

## 🎯 Overview

This repository contains security automation tooling for the sovereign lab, running on the **Kali-Master** node. It includes:

- **Autonomous agents** for continuous security monitoring
- **Python scripts** for log parsing, network scanning, and access control
- **MCP Bridge** for direct AI agent integration with security tools

---

## 🏗️ Repository Structure

```
cybersecurity-lab-automation/
├── README.md                          (this file)
├── agents/
│   ├── security-ops-agent.py         Log monitoring & incident response
│   ├── net-analyzer-agent.py         Hourly network reconnaissance
│   └── rd-agent.py                   Research & development experiments
├── analytics/
│   ├── log-parser.py                 Parse security logs
│   ├── network-scanner.py            Network reconnaissance
│   ├── access-control.py             User access analysis
│   └── threat-detection.py           Anomaly & threat detection
├── mcp-bridge/
│   ├── security-tools-bridge.py      Integration layer for security tools
│   └── docs/
│       └── MCP_SECURITY_FIX.md       Security hardening documentation
├── suite/
│   ├── scanner.py                    Multi-vector vulnerability scanner
│   ├── test_ssti.py                  SSTI (Server-Side Template Injection) testing
│   └── README.md                     Security suite documentation
└── config/
    └── agent-config.yml              Agent configuration & scheduling
```

---

## 🤖 Autonomous Agents

### Security-Ops Agent
Monitors security logs and triggers incident response workflows.

**Features:**
- Real-time log analysis
- Anomaly detection
- Alert generation
- Incident response coordination

**Runs on:** Kali-Master  
**Frequency:** Continuous

### Net-Analyzer Agent
Performs hourly network reconnaissance and threat hunting.

**Features:**
- Network topology mapping
- Port scanning
- Service enumeration
- Threat intelligence correlation

**Runs on:** Kali-Master  
**Frequency:** Hourly

---

## 🛠️ Security Analytics Scripts

### Log Parsing
- `failed_login.py` — Parse failed authentication attempts
- `access_logs.py` — Analyze system access patterns
- `auth_events.py` — Track authorization events

### Network Scanning
- `analyse_paquets.py` — Packet analysis & inspection
- `port_scan.py` — Network service discovery
- `network_mapper.py` — LAN topology mapping

### Access Control
- `filtrage_utilisateurs.py` — User access filtering
- `permission_audit.py` — Permission compliance checking
- `access_control.py` — ACL enforcement validation

---

## 🔌 MCP Bridge

The MCP Bridge provides secure integration between AI agents (Gemini CLI, Ollama) and security tools.

**Architecture:**
```
[AI Agent] → [MCP Bridge] → [Security Tools]
                   │
          [Log Analytics]
          [Network Scanners]
          [Threat Detection]
```

**Features:**
- Secure command execution
- Tool context injection
- Response parsing & aggregation
- Audit logging

**Security Fixes:** See `mcp-bridge/docs/MCP_SECURITY_FIX.md`

---

## 🧪 Security Suite

Custom security testing tools:

- **scanner.py** — Evolving vulnerability scanner (multi-vector)
- **scanner1.py, scanner2.py, scanner3.py** — Specialized scanners
- **test_ssti.py** — Server-Side Template Injection (SSTI) testing

**Usage:**
```bash
python3 test_ssti.py --url http://target-app.local
python3 scanner.py --target 192.168.1.0/24
```

**Disclaimer:** For authorized penetration testing in controlled environments only.

---

## 🚀 Deployment

### Prerequisites
- Kali Linux running on Kali-Master node
- Python 3.8+
- Standard security tools (nmap, metasploit, etc.)

### Quick Start
```bash
# Clone repository
git clone https://github.com/Dinaverse/cybersecurity-lab-automation
cd cybersecurity-lab-automation

# Install dependencies (if needed)
pip install -r requirements.txt

# Start agents
python agents/security-ops-agent.py &
python agents/net-analyzer-agent.py &
```

### Monitoring Agents
```bash
# Check agent status
ps aux | grep agent

# View agent logs
tail -f logs/agents.log
```

---

## 🔗 Integration with Lab

| Integration | Details |
|-------------|---------|
| **Ollama LLM** | Agents powered by local Qwen 3.5:27B model |
| **Prometheus** | Metrics exported to monitoring stack |
| **Grafana** | Security dashboards & alerts |
| **n8n Workflows** | Incident response automation |
| **Morpheus Pipeline** | NVIDIA AI-driven threat detection |

---

## 🔗 Related Repositories

| Repository | Purpose |
|------------|---------|
| [`sovereign-ai-infrastructure`](https://github.com/Dinaverse/sovereign-ai-infrastructure) | Main architecture documentation |
| [`sovereign-ai-skills`](https://github.com/Dinaverse/sovereign-ai-skills) | Custom AI skills for security operations |
| [`local-ai-sovereign-stack`](https://github.com/Dinaverse/local-ai-sovereign-stack) | Ollama & monitoring stack |
| [`sovereign-ai-security`](https://github.com/Dinaverse/sovereign-ai-security) | NVIDIA Morpheus integration |

---

## 📖 Documentation

- [MCP Security Bridge](mcp-bridge/docs/MCP_SECURITY_FIX.md) — Security hardening & best practices
- [Security Suite](suite/README.md) — Vulnerability scanning tools
- [Agent Operations](docs/AGENT_OPERATIONS.md) — Agent deployment & management (planned)

---

*Autonomous security operations — agents monitoring, analyzing, and defending locally.*
