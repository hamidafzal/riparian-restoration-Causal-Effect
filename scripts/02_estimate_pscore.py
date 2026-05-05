# ============================================================
# 02_estimate_pscore.py
# Propensity score and IPTW
# ============================================================

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

DATA_PATH = "data/df_sample.csv"

df = pd.read_csv(DATA_PATH)

# Confounders (subset for public sample)
CONFOUNDERS = [
    'topo',
    'distance_mainChannel',
    'vhi_regional_lag1'
]

df = df.dropna(subset=CONFOUNDERS + ['is_restored'])

# Propensity score
X = df[CONFOUNDERS].astype(float)
y = df['is_restored'].values

X = StandardScaler().fit_transform(X)

ps_model = LogisticRegression(max_iter=2000)
ps_model.fit(X, y)

df['ps'] = ps_model.predict_proba(X)[:, 1]

# IPTW (stabilized)
p_treated = df['is_restored'].mean()

df['iptw'] = np.where(
    df['is_restored'] == 1,
    p_treated / df['ps'],
    (1 - p_treated) / (1 - df['ps'])
)

# Trimming (optional, safe default)
df['iptw'] = df['iptw'].clip(upper=df['iptw'].quantile(0.99))

df.to_csv(DATA_PATH, index=False)
print("✓ Propensity scores and IPTW computed")
