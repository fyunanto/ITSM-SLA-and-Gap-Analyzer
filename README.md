# 📊 ITSM SLA & Gap Analyzer

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Domain](https://img.shields.io/badge/ITSM-ISO%2020000-orange)

An automated Python analytics pipeline for ServiceNow incident logs. This tool computes core operational metrics (**MTTA** & **MTTR**) and maps the perception gap between **Technical Audit Compliance** (ISO/IEC 20000-1) and **End-User Satisfaction**.

---

## 🎯 Key Features

- **Automated Metric Calculation**: Converts raw ServiceNow timestamps into precise MTTA (*Mean Time to Acknowledge*) and MTTR (*Mean Time to Resolve*) metrics in hours.
- **Score Normalization**: Scales 5-point CSAT survey scores to a 0-100% scale for direct correlation with technical audit scores.
- **Perception Gap Mapping**: Identifies operational disconnects where high audit compliance does not align with user satisfaction.
- **Multi-Chart Dashboard**: Automatically generates publication-ready visualizations via Matplotlib & Seaborn.
- **Privacy-First Design**: Includes synthetic data generators to enable testing without exposing sensitive internal ticket details.

---

## 📁 Repository Structure

```text
├── config/             # SLA targets & column mapping
├── data/               # Raw & sample incident datasets
├── docs/               # Methodology & ISO 20000 framework guides
├── output/             # Exported charts & metric summaries
├── scripts/            # Core processing modules
├── main.py             # Main pipeline orchestrator
└── requirements.txt    # Python dependencies
