"""
02_descriptive_stats.py
-----------------------
Exploratory data analysis and descriptive statistics for the multimorbidity SEM study.

Produces:
    - Table 1: Baseline characteristics of the full cohort (n=677)
    - Table 2: Sex-stratified comparison (men vs women)
    - Summary statistics exported to results/

Authors: Kelly Larissa Vomo Donfack, Frédéric Pamoukjian
"""

import pandas as pd
import numpy as np
from scipy import stats

# ── Load cleaned data ─────────────────────────────────────────────────────────
df = pd.read_csv("data/cleaned_data.csv")

# ── Helper functions ──────────────────────────────────────────────────────────
def summarize_continuous(series):
    """Return mean ± SD string."""
    return f"{series.mean():.1f} ± {series.std():.1f}"

def summarize_categorical(series, total):
    """Return N (%) string."""
    n = series.sum()
    return f"{int(n)} ({n/total*100:.1f})"

def compare_groups(df, var, group_col="sex"):
    """
    Compare a variable between men and women.
    Returns p-value from t-test (continuous) or chi-square (categorical).
    """
    groups = [df[df[group_col] == g][var].dropna() for g in df[group_col].unique()]
    if df[var].nunique() > 2:
        stat, p = stats.ttest_ind(*groups)
    else:
        ct = pd.crosstab(df[var], df[group_col])
        stat, p, _, _ = stats.chi2_contingency(ct)
    return round(p, 3)

# ── Table 1: Full cohort ──────────────────────────────────────────────────────
n = len(df)
print("=" * 50)
print(f"TABLE 1 — Baseline characteristics (n={n})")
print("=" * 50)

continuous = {
    "Age (y)": "age_raw",
    "Smoking (pack/year)": "smoking_raw",
    "BMI": "bmi_raw",
    "Age at first cancer diagnosis": "age_first_cancer_diagnosis_raw",
}

for label, col in continuous.items():
    print(f"{label}: {summarize_continuous(df[col])}")

categorical = {
    "Sex (women)": "sex_female",
    "Smoking >= 10 pack/year": "smoking_severe",
    "Metastatic disease (2yr)": "metastatic_2yr",
    "Metastatic disease (3yr)": "metastatic_3yr",
    "AID": "aid",
    "Severe AID": "severe_aid",
    "Early AID": "early_aid",
    "CVD": "cvd",
    "Early CVD": "early_cvd",
    "CVRF": "cvrf",
    "Early CVRF": "early_cvrf",
    "Early or multiple cancers": "early_or_multiple_cancer",
    "Death at 2yr": "death_2yr",
    "Death at 3yr": "death_3yr",
}

for label, col in categorical.items():
    print(f"{label}: {summarize_categorical(df[col], n)}")

# ── Table 2: Sex-stratified ───────────────────────────────────────────────────
men   = df[df["sex_female"] == 0]
women = df[df["sex_female"] == 1]

print("\n" + "=" * 50)
print(f"TABLE 2 — Sex-stratified (Men n={len(men)}, Women n={len(women)})")
print("=" * 50)

for label, col in {**continuous, **categorical}.items():
    try:
        p = compare_groups(df, col if col in df.columns else None)
        print(f"{label}: p={p}")
    except Exception:
        pass

# ── Export ────────────────────────────────────────────────────────────────────
summary = df.describe().T
summary.to_csv("results/descriptive_stats.csv")
print("\nDescriptive stats saved to results/descriptive_stats.csv")
