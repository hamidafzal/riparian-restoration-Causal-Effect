
# ============================================================
# 04_placebo_test.py
# Placebo ATT with shifted restoration year
# ============================================================

import pandas as pd
import numpy as np
import statsmodels.api as sm

DATA_PATH = "data/df_sample.csv"
SHIFT = 5

df = pd.read_csv(DATA_PATH)

df['restoration_placebo'] = df['restoration_year'].apply(
    lambda y: y - SHIFT if y < 9999 else y
)

df['is_restored_pl'] = (df['year'] >= df['restoration_placebo']).astype(int)
df.loc[df['restoration_placebo'] >= 9999, 'is_restored_pl'] = 0

df['rel_year_pl'] = df['year'] - df['restoration_placebo']

bins   = [-np.inf,-1,0,2,5,10,np.inf]
labels = ['Pre','Year0','yr1_2','yr3_5','yr6_10','gt10']

df['time_group'] = pd.cut(df['rel_year_pl'], bins=bins, labels=labels)
dums = pd.get_dummies(df['time_group'], prefix='period')
df = pd.concat([df, dums], axis=1)

ATT_VARS = []
for p in ['Year0','yr1_2','yr3_5','yr6_10','gt10']:
    v = f'att_{p}'
    df[v] = df['is_restored_pl'] * df[f'period_{p}']
    ATT_VARS.append(v)

X = sm.add_constant(df[ATT_VARS])
y = df['vhi_regional']

model = sm.WLS(y, X, weights=df['iptw']).fit()
print(model.summary())
