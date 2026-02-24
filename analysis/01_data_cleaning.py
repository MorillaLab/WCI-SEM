"""
01_data_cleaning.py
-------------------
Data preprocessing and imputation for the multimorbidity SEM study.

Steps:
    1. Load raw dataset
    2. Handle missing values (iterative imputation)
    3. Standardize continuous variables
    4. Encode categorical variables
    5. Export cleaned dataset for downstream analysis

Authors: Kelly Larissa Vomo Donfack, Frédéric Pamoukjian
"""

import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.impute import IterativeImputer
from sklearn.preprocessing import StandardScaler

# ── 1. Load data ──────────────────────────────────────────────────────────────
# Replace with your actual file path
df = pd.read_csv("data/raw_data.csv")

print(f"Dataset shape: {df.shape}")
print(f"\nMissing values per column:\n{df.isnull().sum()[df.isnull().sum() > 0]}")

# ── 2. Handle missing values ──────────────────────────────────────────────────
# Columns with known missing values
cols_with_missing = ["smoking", "age_first_cancer_diagnosis", "early_or_multiple_cancer"]

imputer = IterativeImputer(max_iter=10, random_state=42)
df[cols_with_missing] = imputer.fit_transform(df[cols_with_missing])

print(f"\nMissing values after imputation:\n{df.isnull().sum()[df.isnull().sum() > 0]}")

# ── 3. Standardize continuous variables ───────────────────────────────────────
continuous_vars = ["age", "smoking", "bmi", "age_first_cancer_diagnosis"]

scaler = StandardScaler()
df[continuous_vars] = scaler.fit_transform(df[continuous_vars])

# ── 4. Encode / recode categorical variables ──────────────────────────────────
# Smoking categories: 0 = no smoking, 1 = <10 pack/year, 2 = >=10 pack/year
df["smoking_cat"] = pd.cut(
    df["smoking_raw"],
    bins=[-np.inf, 0, 10, np.inf],
    labels=[0, 1, 2]
).astype(int)

# BMI binary: 0 = BMI <= 40, 1 = BMI > 40
df["bmi_binary"] = (df["bmi_raw"] > 40).astype(int)

# ── 5. Export cleaned dataset ─────────────────────────────────────────────────
df.to_csv("data/cleaned_data.csv", index=False)
print("\nCleaned dataset saved to data/cleaned_data.csv")
