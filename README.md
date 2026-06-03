# riparian-restoration-Causal-Effect

Event-study analysis of riparian forest restoration effects on Vegetation Health Index (VHI) using satellite data

Try the Pipeline on Google Colab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hamidafzal/riparian-restoration-Causal-Effect/blob/main/Danube_Causal_Pipeline.ipynb)



# Riparian Forest Restoration — Event‑Study with IPTW


-This repository contains the analysis code for an event‑study evaluation of
riparian forest restoration effects on vegetation health using satellite data.

The analysis implements an **inverse probability of treatment weighting (IPTW)**
difference‑in‑differences (DiD) design to estimate time‑varying **Average Treatment
Effects on the Treated (ATTs)**.

---

## 🔬 Study Overview

- **Outcome**
  - The average treatment effect of hydrological restoration on the Vegetation Health Index
  -  $$VHI = \alpha \cdot VCI + (1 - \alpha) TCI$$
  
- **Framework**
  - Potential outcomes · marginal structural model

- **Estimand**
  - Average Treatment Effect on the Treated (ATT)

- **Key features**
  - Propensity score weighting (IPTW)
  - Reach fixed effects
  - Sensitivity analysis (E‑values)
  - Spatial diagnostics (Moran’s I)
  - Spatial cluster‑robust standard errors

---
---

## 📊 Data availability


The complete analytical dataset used in the manuscript is available from the authors upon  request.

This repository includes a **reduced sample dataset**
(`data/sample.csv`) containing **100 randomly selected pixels per reach**.

The sample data:
- preserves the structure of the full dataset,
- allows execution of the complete analysis workflow,
- **does not reproduce the ORIGINAL quantitative results**.

Results obtained using the sample data are illustrative only.

---

