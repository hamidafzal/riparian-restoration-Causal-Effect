# riparian-restoration-Causal-Effect
Event-study analysis of riparian forest restoration effects on Vegetation Health Index (VHI) using satellite data
# Riparian Forest Restoration — Event‑Study with IPTW

This repository contains the analysis code for an event‑study evaluation of
riparian forest restoration effects on vegetation health using satellite data.

The analysis implements an **inverse probability of treatment weighting (IPTW)**
difference‑in‑differences design to estimate time‑varying **Average Treatment
Effects on the Treated (ATTs)**.

---

## 🔬 Study Overview

- **Outcome**
  - Vegetation Health Index (VHI)

- **Design**
  - Event‑study difference‑in‑differences

- **Estimand**
  - Average Treatment Effect on the Treated (ATT)

- **Key features**
  - Propensity score weighting (IPTW)
  - Reach fixed effects
  - Placebo test (pre‑trend diagnostic)
  - Sensitivity analysis (E‑values)
  - Spatial diagnostics (Moran’s I)
  - Spatial cluster‑robust standard errors

---
---

## 📊 Data availability

The full analytical dataset used in the manuscript cannot be shared due to
data volume and licensing constraints.

This repository includes a **reduced sample dataset**
(`data/df_sample_for_github.csv`) containing **100 randomly selected pixels per reach**.

The sample data:
- preserves the structure of the full dataset,
- allows execution of the complete analysis workflow,
- **does not reproduce the manuscript’s quantitative results**.

Results obtained using the sample data are illustrative only.

---

## ▶️ How to run the analysis

### 1. Install dependencies


pip install -r requirements.txt

---
---
### 1. Install dependencies
python scripts/01_prepare_data.py
python scripts/02_estimate_pscore.py
python scripts/03_estimate_att.py
python scripts/04_placebo_test.py
python scripts/05_spatial_diagnostics.py
python scripts/06_plots.py


``
