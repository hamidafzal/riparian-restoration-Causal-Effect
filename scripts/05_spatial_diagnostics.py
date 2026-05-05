
# ============================================================
# 05_spatial_diagnostics.py
# Moran’s I on residuals (illustrative)
# ============================================================

import pandas as pd

try:
    from libpysal.weights import KNN
    from esda.moran import Moran
    SPATIAL = True
except ImportError:
    SPATIAL = False

DATA_PATH = "data/df_sample.csv"
df = pd.read_csv(DATA_PATH)

if not SPATIAL:
    print("⚠ Spatial libraries not installed")
elif not {'X','Y'}.issubset(df.columns):
    print("⚠ Coordinates removed in public sample")
else:
    coords = df[['X','Y']].values
    w = KNN.from_array(coords, k=8)
    w.transform = 'R'
    mi = Moran(df['vhi_regional'], w)
    print(f"Moran’s I = {mi.I:.3f}, p = {mi.p_sim:.3f}")
