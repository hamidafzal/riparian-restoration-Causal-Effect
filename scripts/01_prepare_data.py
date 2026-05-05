# ============================================================
# 01_prepare_data.py
# Load sample data and define treatment timing
# ============================================================

import pandas as pd
import numpy as np

DATA_PATH = "data/df_sample.csv"

# Load
df = pd.read_csv(DATA_PATH)

# Basic checks
required = ['id', 'reach_numb', 'year']
for c in required:
    if c not in df.columns:
        raise ValueError(f"Missing required column: {c}")

# Restoration map (example — must match paper logic)
RESTORE_MAP = {
    1: 2012,
    2: 2019,
    3: 9999,  # never restored
    4: 2014
}

df['restoration_year'] = df['reach_numb'].map(RESTORE_MAP)

# Treatment indicator and event time
df['is_restored'] = (df['year'] >= df['restoration_year']).astype(int)
df.loc[df['restoration_year'] >= 9999, 'is_restored'] = 0

df['relative_year'] = df['year'] - df['restoration_year']

print("✓ Data loaded and treatment variables created")
print(df[['reach_numb', 'restoration_year', 'is_restored']].drop_duplicates())
