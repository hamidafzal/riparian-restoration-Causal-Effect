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

## 📂 Repository structure

``
