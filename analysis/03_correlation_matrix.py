"""
03_correlation_matrix.py
------------------------
Cramér's V correlation matrix between observed variables used in SEM latent
variable construction.

Cramér's V measures association between categorical variables (range 0–1),
analogous to Pearson's r for continuous data.

Produces:
    - results/cramers_v_matrix.csv
    - figures/correlation_matrix.png

Authors: Kelly Larissa Vomo Donfack, Frédéric Pamoukjian
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

# ── Load data ─────────────────────────────────────────────────────────────────
df = pd.read_csv("data/cleaned_data.csv")

# Variables included in the correlation analysis
VARIABLES = [
    "sex",
    "smoking",
    "bmi_binary",
    "early_or_multiple_cancer",
    "familial_cancer",
    "early_familial_cancer",
    "early_aid",
    "severe_aid",
    "early_cvd",
    "early_cvrf",
    "familial_cvd",
    "early_familial_cvd",
    "familial_cvrf",
    "early_familial_cvrf",
    "metastatic_disease",
    "death",
]

# ── Cramér's V function ───────────────────────────────────────────────────────
def cramers_v(x, y):
    """Compute Cramér's V statistic for two categorical series."""
    confusion_matrix = pd.crosstab(x, y)
    chi2, _, _, _ = chi2_contingency(confusion_matrix)
    n = confusion_matrix.sum().sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    phi2_corr = max(0, phi2 - ((k - 1) * (r - 1)) / (n - 1))
    r_corr = r - ((r - 1) ** 2) / (n - 1)
    k_corr = k - ((k - 1) ** 2) / (n - 1)
    return np.sqrt(phi2_corr / min((k_corr - 1), (r_corr - 1)))

# ── Build correlation matrix ──────────────────────────────────────────────────
vars_present = [v for v in VARIABLES if v in df.columns]
n = len(vars_present)
matrix = pd.DataFrame(np.zeros((n, n)), index=vars_present, columns=vars_present)

for i, v1 in enumerate(vars_present):
    for j, v2 in enumerate(vars_present):
        if i == j:
            matrix.loc[v1, v2] = 1.0
        elif i < j:
            val = cramers_v(df[v1].dropna(), df[v2].dropna())
            matrix.loc[v1, v2] = val
            matrix.loc[v2, v1] = val

print("Cramér's V matrix computed.")
print(matrix.round(3))

# ── Export matrix ─────────────────────────────────────────────────────────────
matrix.to_csv("results/cramers_v_matrix.csv")
print("\nSaved to results/cramers_v_matrix.csv")

# ── Plot heatmap ──────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(
    matrix,
    annot=True,
    fmt=".2f",
    cmap="YlOrRd",
    vmin=0,
    vmax=1,
    linewidths=0.5,
    ax=ax,
)
ax.set_title("Cramér's V Correlation Matrix", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("figures/correlation_matrix.png", dpi=150)
plt.close()
print("Heatmap saved to figures/correlation_matrix.png")
