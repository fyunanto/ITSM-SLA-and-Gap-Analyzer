# 📐 Gap Analysis Methodology

## 1. Overview
This document outlines the analytical methodology used in the **ITSM SLA & Gap Analyzer** pipeline. The framework evaluates the relationship and divergence between objective **Technical Audit Compliance** (procedural adherence, SLA thresholds, workflow completeness) and subjective **End-User Perception** (CSAT surveys, user satisfaction scores).

---

## 2. Core Metrics & Mathematical Formulations

### 2.1 Mean Time to Acknowledge (MTTA)
MTTA measures the speed at which the IT support team acknowledges and assigns an incident from the time of creation.

$$\text{MTTA (Hours)} = \frac{\sum_{i=1}^{N} (T_{\text{acknowledged}, i} - T_{\text{created}, i})}{N \times 3600}$$

Where:
- $T_{\text{created}}$ = Timestamp of incident registration (`sys_created_on`).
- $T_{\text{acknowledged}}$ = Timestamp of first response/assignment (`sys_acknowledged_on`).
- $N$ = Total number of incidents processed.

### 2.2 Mean Time to Resolve (MTTR)
MTTR measures the total elapsed time from incident creation until successful resolution and service restoration.

$$\text{MTTR (Hours)} = \frac{\sum_{i=1}^{N} (T_{\text{resolved}, i} - T_{\text{created}, i})}{N \times 3600}$$

Where:
- $T_{\text{resolved}}$ = Timestamp of incident closure/resolution (`resolved_at`).

---

## 3. Perception vs. Audit Gap Analysis

### 3.1 Score Normalization
To enable direct comparative analysis between technical compliance scores and user satisfaction ratings, 5-point CSAT survey metrics are normalized onto a 100% percentage scale:

$$\text{User Perception (\%)} = \left( \frac{\text{CSAT Rating}}{5.0} \right) \times 100$$

### 3.2 Perception Gap Formula
The Perception Gap measures the percentage point divergence between internal audit scores and external user satisfaction:

$$\text{Perception Gap} = \text{Technical Audit Score (\%)} - \text{User Perception (\%)}$$

#### Interpretation Matrix:
| Gap Value | Classification | Operational Meaning |
| :---: | :--- | :--- |
| **$> +15\%$** | **High Over-Confidence / User Dissatisfaction** | IT team achieves high procedural compliance, but end users remain dissatisfied (e.g., poor communication, workaround friction). |
| **$-5\%$ to $+10\%$** | **Optimal Operational Alignment** | Technical SLA compliance closely reflects user satisfaction and expectations. |
| **$< -10\%$** | **User Lenience / Undocumented Support** | High end-user satisfaction despite low procedural audit scores (e.g., informal resolution off-the-record). |

---

## 4. Statistical Correlation
The pipeline evaluates statistical association between technical compliance ($X$) and user perception ($Y$) using **Pearson’s Correlation Coefficient ($r$)**:

$$r = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum (X_i - \bar{X})^2 \sum (Y_i - \bar{Y})^2}}$$

- **$r \ge 0.80$**: Strong positive alignment between technical execution and user satisfaction.
- **$r < 0.50$**: Disconnect in service delivery, triggering process review and refinement.