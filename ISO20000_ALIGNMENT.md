# 🛡️ ISO/IEC 20000-1:2018 Alignment Guide

## 1. Executive Context
ISO/IEC 20000-1:2018 is the international standard for IT Service Management Systems (SMS). This document details how the **ITSM SLA & Gap Analyzer** maps ServiceNow operational log metrics directly to key clauses of the standard.

---

## 2. Clause Mapping Matrix

| ISO/IEC 20000-1 Clause | Requirement Description | Analytical Metric / Tool Feature |
| :--- | :--- | :--- |
| **Clause 8.2.2** | Service Level Management (SLA Tracking) | Automated MTTR & MTTA calculation vs target thresholds defined in `config.json`. |
| **Clause 8.6.1** | Incident Management | Log tracking of lifecycle state transitions (`created` $\rightarrow$ `acknowledged` $\rightarrow$ `resolved`). |
| **Clause 8.6.2** | Service Request Management | Ticket categorization, response duration, and fulfillment SLA tracking. |
| **Clause 9.1.1** | Monitoring, Measurement, Analysis & Evaluation | Dashboard analytics mapping Technical Audit Compliance against Target KPIs. |
| **Clause 9.1.2** | Customer Satisfaction Evaluation | CSAT normalization and Perception Gap trend analysis. |
| **Clause 10.1** | Continual Improvement | Identification of high-MTTR categories and correlation anomaly detection for root-cause optimization. |

---

## 3. Operational Alignment Details

### 3.1 Clause 8.2.2: Service Level Management
- **Objective**: Ensure IT service delivery meets agreed-upon performance targets (SLAs).
- **Tool Mapping**: The pipeline compares calculated MTTA and MTTR values against pre-configured thresholds (`mtta_target_hours: 0.5` and `mttr_target_hours: 8.0`). Incidents breaching SLAs are flagged for operational audit.

### 3.2 Clause 9.1.2: Customer Satisfaction Evaluation
- **Objective**: Assess whether delivered IT services meet business and end-user expectations.
- **Tool Mapping**: By converting CSAT survey ratings to normalized percentages and plotting them against audit compliance, organizations can systematically satisfy ISO audit requirements for user feedback evaluation.

### 3.3 Clause 10.1: Continual Improvement (PDCA Cycle)
- **Plan**: Define SLA targets in `config/config.json`.
- **Do**: Log daily incident lifecycle timestamps in ServiceNow.
- **Check**: Run `main.py` to calculate MTTR, MTTA, and Perception Gaps.
- **Act**: Target categories exhibiting significant perception gaps ($>15\%$) for user communication improvements or technical retraining.