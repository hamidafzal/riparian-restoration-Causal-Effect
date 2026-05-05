
# ============================================================
# 02_estimate_pscore.py
# Estimate propensity scores
# ============================================================

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

DATA_PATH = "data/df_sample.csv"

df = pd.read_csv(DATA_PATH)

# Example confounders (subset for sample)
CONFOUNDERS = [
    'topo',
    'distance_mainChannel',
    'vhi_regional_lag1'
]

df = df.dropna(subset=CONFOUNDERS + ['is_restored'])

X = df[CONFOUNDERS].astype(float)
y = df['is_restored'].values

scaler = StandardScaler()
X_s = scaler.fit_transform(X)

ps_model = LogisticRegression(max_iter=2000)
ps_model.fit(X_s, y)

df['ps'] = ps_model.predict_proba(X_s)[:, 1]

print("✓ Propensity scores estimated")
print(df['ps'].describe())
