
# ============================================================
# 03_estimate_att.py
# Event-study ATT estimation WITH IPTW
# ============================================================

import pandas as pd
import numpy as np
import statsmodels.api as sm

DATA_PATH = "data/df_sample.csv"
df = pd.read_csv(DATA_PATH)

# Event-time bins
bins   = [-np.inf, -1, 0, 2, 5, 10, np.inf]
labels = ['Pre', 'Year0', 'yr1_2', 'yr3_5', 'yr6_10', 'gt10']

df['time_group'] = pd.cut(df['relative_year'], bins=bins, labels=labels)

# Period dummies
period_dums = pd.get_dummies(df['time_group'], prefix='period')
df = pd.concat([df, period_dums], axis=1)

# ATT interactions
PERIODS = ['Year0','yr1_2','yr3_5','yr6_10','gt10']
ATT_VARS = []

for p in PERIODS:
    v = f'att_{p}'
    df[v] = df['is_restored'] * df[f'period_{p}']
    ATT_VARS.append(v)

# Reach fixed effects
reach_dums = pd.get_dummies(df['reach_numb'], prefix='reach', drop_first=False)
REACH_FE = [c for c in reach_dums.columns if c != 'reach_3']
df = pd.concat([df, reach_dums[REACH_FE]], axis=1)

# Weighted regression
X = sm.add_constant(df[ATT_VARS + REACH_FE])
y = df['vhi_regional']

model = sm.WLS(
    y,
    X,
    weights=df['iptw']
).fit()

print(model.summary())
