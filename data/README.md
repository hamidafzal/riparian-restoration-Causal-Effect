# Danube Riparian Forest Restoration — Causal Inference Pipeline

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

Reproducible code for the causal inference analysis reported in:

> [Authors]. *Climate variability and forest management as drivers of vegetation health in the riparian zone of the Danube.* Environmental Research Letters, 2025.

---

## Overview

This repository provides the full Python pipeline to estimate the **Average Treatment Effect on the Treated (ATT)** of hydrological reconnection on riparian forest vegetation health (VHI) across the Slovak Danube floodplain (1985–2024).

The pipeline uses **Inverse Probability of Treatment Weighting (IPTW)** within a marginal structural model, with spatial cluster-robust standard errors and a full placebo re-estimation for validation.

---

## Repository structure

```
danube-restoration-causal/
├── Danube_Causal_Pipeline.ipynb   ← full analysis notebook (15 steps)
├── data/
│   └── sample.csv                 ← 50-pixel anonymised sample
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Quick start

```bash
# 1. Clone
git clone https://github.com/YOUR_USERNAME/danube-restoration-causal
cd danube-restoration-causal

# 2. Install dependencies
pip install -r requirements.txt

# 3. Optional — Moran's I spatial test
pip install libpysal esda

# 4. Run
jupyter notebook Danube_Causal_Pipeline.ipynb
```

Set `DATA_PATH` in **Cell 1** to your data file. The sample (`data/sample.csv`) runs the full pipeline on 50 anonymised pixels.

---

## Data

The full pixel-level dataset (2,187 pixels × 40 years) is archived on Zenodo:  
→ [https://doi.org/10.5281/zenodo.XXXXXXX](https://doi.org/10.5281/zenodo.XXXXXXX)

### Column reference

| Column | Description |
|---|---|
| `id` | Unique pixel identifier |
| `X`, `Y` | Pixel centroid coordinates (metres, EPSG:32633) |
| `reach_numb` | Reach (1–4). Reach 3 = control |
| `restoration_year` | Year of hydrological reconnection (9999 = never) |
| `vhi_regional_YYYY` | Sub-regional VHI — **primary outcome** (bounded 0–1) |
| `vhi_YYYY` | Z-scored AR1 residuals from trend analysis (not used in causal model) |
| `msi_YYYY` | Moisture Stress Index |
| `tem_YYYY` | Growing-season mean temperature (°C) |
| `pre_YYYY` | Growing-season precipitation (mm) |
| `discharge_YYYY` | Annual mean discharge (m³/s) |
| `forest_type` | 101 = managed plantation \| 102 = unmanaged natural forest |
| `forest_F` | Fraction of 40 years classified as forest |
| `topo` | LiDAR-derived elevation (m) |
| `landcover` | Forest cover probability z-score |
| `distance_mainChannel` | Distance to Danube main channel (m) |

---

## Reach reference

| Reach | Restoration | Forest type | Role |
|---|---|---|---|
| 1 | 2012 | Mixed (101+102) | Treated |
| 2 | 2019 | Mixed (101+102) | Treated |
| **3** | **Never** | **Managed (101)** | **Reference control** |
| 4 | 2015 | Unmanaged (102) | Treated |

---

## Pipeline steps

| Step | Description |
|---|---|
| 1 | Load and reshape (wide → long, X/Y included) |
| 2 | Validate `vhi_regional` |
| 3 | Define modular functions (PS, weights, ATT, placebo-reusable) |
| 4 | Estimate propensity scores (cross-sectional, pre-treatment means) |
| 5 | VIF check |
| 6 | Covariate balance (SMD before/after IPTW) |
| 7 | Build panel and ATT specification |
| 8 | ATT models (A: standard, B: reach-balanced ★ PRIMARY) + reach-specific |
| 9 | Pre-treatment parallel trends check |
| 10 | **Placebo test** (full re-estimation under fake restoration dates) |
| 11 | **Moran's I** (spatial autocorrelation in residuals) |
| 12 | **Spatial cluster-robust SEs** (30m grid) |
| 13 | E-value sensitivity analysis |
| 14 | Event study plot (Figure 7) |
| 15 | Forest type comparison (managed 101 vs unmanaged 102) |

---

## Key methodological decisions

| Decision | Choice | Reason |
|---|---|---|
| PS estimation unit | Pre-treatment rows per pixel | Treatment is one-time — panel rows contaminate |
| PS covariates | 5-yr pre-treatment means | Lags near treatment year are endogenous |
| Groundwater | **NOT** a confounder | Mediator: T→GW→VHI — overadjustment bias |
| `vhi` column | **NOT** used as outcome | Z-scored AR1 residuals — wrong scale |
| Pooled estimate | Reach-balanced weights | Prevents Reach 2 (largest) dominating |
| Standard errors | Spatial cluster-robust (30m grid) | Landsat pixels are spatially correlated |
| Placebo | Full re-estimation | Reusing real weights is not a valid test |

---

## Dependencies

```
pandas>=1.5
numpy>=1.23
statsmodels>=0.14
scikit-learn>=1.2
matplotlib>=3.6
```

Optional (Moran's I):
```
libpysal>=4.7
esda>=2.4
```

---

## Citation

If you use this code, please cite:

```bibtex
@article{authors2025danube,
  title   = {Climate variability and forest management as drivers of
             vegetation health in the riparian zone of the Danube},
  author  = {[Authors]},
  journal = {Environmental Research Letters},
  year    = {2025},
  doi     = {10.1088/XXXX}
}
```

---

## License

MIT — see [LICENSE](LICENSE).
