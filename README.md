# ☁️ Cloud Resource Monitor

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Cloud](https://img.shields.io/badge/Cloud-AWS-orange?style=for-the-badge&logo=amazon-aws)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![3SVK](https://img.shields.io/badge/3SVK-Season%203-purple?style=for-the-badge)

> **National Research & Innovation Challenge — Season 3 by 3SVK**  
> Team: `mr-robot` | Author: `Pankaj Kumar` | Domain: `Cloud Engineering`

---

## 🚀 Overview

**Cloud Resource Monitor** is a Python-based intelligent cloud infrastructure analysis tool that simulates real-world **AWS resource tracking, cost optimization, and security auditing**.

Built for the 3SVK National Research & Innovation Challenge Season 3, this project addresses one of the most critical problems in modern cloud computing — **cloud waste**, which costs organizations billions annually.

---

## 🎯 Problem Statement

> Organizations waste **30–35% of their cloud budget** on idle, underutilized, or forgotten resources. Manual monitoring is error-prone and slow.

**Our Solution:** An automated Python engine that continuously monitors EC2 instances and S3 buckets, detects waste, flags security risks, and generates actionable recommendations — in seconds.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 💰 **Cost Analysis** | Real-time breakdown of EC2 + S3 monthly spend |
| 📉 **Waste Detection** | Identifies idle, stopped & underutilized instances |
| 🔒 **Security Audit** | Flags publicly exposed S3 buckets automatically |
| 💡 **Smart Recommendations** | Actionable steps to reduce spend immediately |
| 📊 **JSON Reports** | Machine-readable output for pipeline integration |

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Cloud Focus:** AWS EC2, AWS S3
- **Output Format:** Terminal + JSON
- **Dependencies:** Standard Library only (zero pip installs!)

---

## ⚡ Quick Start

```bash
# Clone the repository
git clone https://github.com/hack2ai/cloud-resource-monitor.git
cd cloud-resource-monitor

# Run the monitor
python src/cloud_monitor.py

# Run tests
python tests/test_monitor.py
```

---

## 📊 Sample Output

╔══════════════════════════════════════════════════════╗
║ CLOUD RESOURCE MONITOR - HEALTH REPORT ║
╚══════════════════════════════════════════════════════╝
Generated: 2026-10-11 | Author: Pankaj Kumar

📊 COST ANALYSIS
─────────────────────────────────────────
EC2 Instances Cost : $480.85/month
S3 Storage Cost : $31.87/month
Total Monthly Cost : $512.72/month
Estimated Waste : $239.10/month
Savings Potential : 46.6% 🔥

🔒 SECURITY AUDIT
─────────────────────────────────────────
⚠️ Bucket ‘backup-storage’ has PUBLIC access!

💡 RECOMMENDATIONS
─────────────────────────────────────────
📉 Instance i-04521abc CPU at 6% — downsize to save cost
⏸️ Instance i-07823def is IDLE — schedule auto-shutdown
💡 Instance i-03785abc STOPPED — terminate to save $27/month


---

## 📁 Project Structure

cloud-resource-monitor/
├── 📂 src/
│ └── cloud_monitor.py # Core monitoring engine
├── 📂 tests/
│ └── test_monitor.py # Unit test suite
├── 📂 docs/
│ └── research_notes.md # Research documentation
├── requirements.txt # Dependencies
└── README.md # You are here


---

## 🔬 Research Contributions

1. **Cost Optimization Model** — Quantifies monthly savings potential with instance-level granularity
2. **Security Posture Scoring** — Automated detection of publicly exposed cloud storage
3. **Resource Health Classification** — Categorizes instances into actionable priority tiers

---

## 📜 License

MIT License — Open for research, education, and innovation.

---

<div align="center">
  <b>Built with ❤️ for 3SVK National Research & Innovation Challenge Season 3</b><br>
  <i>Team mr-robot | Pankaj Kumar | JNTU Hyderabad</i>
</div>
