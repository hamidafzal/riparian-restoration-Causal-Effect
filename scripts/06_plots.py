
# ============================================================
# 06_plots.py
# Event-study plot (sample only)
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "data/df_sample.csv"
df = pd.read_csv(DATA_PATH)

means = df.groupby('time_group')['vhi_regional'].mean()

plt.figure(figsize=(6,4))
means.plot(marker='o')
plt.axhline(df['vhi_regional'].mean(), linestyle='--')
plt.ylabel("Mean VHI")
plt.xlabel("Event-time bin")
plt.title("Illustrative event-study trajectory (sample data)")
plt.tight_layout()
plt.show()
