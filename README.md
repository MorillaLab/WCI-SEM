# Decoding Multimorbidity: Understanding Cancers and Inflammatory Chronic Diseases Contribution to Death

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This repository contains the data analysis code and supplementary materials for the study:

> **Decoding multimorbidity: Understanding cancers, inflammatory chronic diseases contribution to death.**
>
> Kelly Larissa Vomo Donfack, Burak Gönüllu, Frédéric Pamoukjian, Eurydice Angeli, Grégory Ginot, Ian Morilla, Guilhem Bousquet\*, Géraldine Falgarone
>
> \*Correspondence: guilhem.bousquet@aphp.fr

## Abstract

This prospective monocentric cohort study (n = 677 cancer patients, 2016–2022) applies **Structural Equation Modeling (SEM)** to elucidate the complex relationships between familial risk, inflammaging, chronic diseases, and cancer outcomes. Four latent variables — ***Inflammaging***, ***Familial Cancer Risk***, ***Familial Vascular Risk***, and ***Early Chronic Disease*** — were constructed and validated (CFI up to 0.926; RMSEA as low as 0.043). Results reveal strong interconnections between cancer severity, metastatic disease, and mortality, with marked sex-specific differences.

---

## Repository Structure

```
.
├── README.md
├── data/
│   └── README.md               # Data availability statement
├── analysis/
│   ├── 01_data_cleaning.py     # Data preprocessing and imputation
│   ├── 02_descriptive_stats.py # Exploratory data analysis
│   ├── 03_correlation_matrix.py# Cramér's V correlation analysis
│   └── 04_sem_models.do        # SEM construction and testing (STATA)
├── results/
│   └── README.md               # Description of output files
└── figures/
    └── README.md               # Figure generation notes
```

---

## Methods Summary

### Study Design
- **Type:** Prospective, monocentric cohort
- **Site:** Hôpital Avicenne, APHP, Bobigny, France
- **Period:** January 2016 – December 2022
- **N:** 677 adult cancer patients
- **Median follow-up:** 2.14 years (Model 1), 3.03 years (Model 2)

### Latent Variables

| Latent Variable | Observed Indicators |
|---|---|
| ***Inflammaging*** | Sex, Smoking (pack/year), BMI |
| ***Familial Cancer Risk*** | Familial cancer, Early familial cancer |
| ***Familial Vascular Risk*** | Familial CVD, Early familial CVD, Familial CVRF, Early CVRF |
| ***Early Chronic Disease*** | Early AID, Severe AID, Early CVD, Early CVRF |

### Statistical Tools
- **Python** — data cleaning, recoding, descriptive analysis
- **STATA** — SEM model construction and testing (maximum likelihood estimation)
- **Model fit criteria:** CFI > 0.90, RMSEA < 0.06, SRMR < 0.08

---

## Key Findings

- ***Inflammaging*** (sex, smoking, BMI) showed a strong association with cancer (loading = 0.80) and was significantly associated with metastatic disease and mortality.
- ***Familial Vascular Risk*** was significantly associated with ***Familial Cancer Risk***, which itself was associated with ***Inflammaging***, suggesting shared constitutional genetic pathways.
- **Sex-specific analyses** revealed distinct pathways in women: familial risk and early chronic disease directly contributed to metastatic disease and death, while ***Inflammaging*** was directly (not mediated) associated with mortality.
- This is the first mathematical demonstration of interconnected links between familial cardiovascular risk, inflammaging, cancer, and chronic inflammatory diseases.

---

## Data Availability

De-identified data supporting this study are available from the corresponding author upon reasonable request, pending ethical approvals.

Contact: **Prof. Guilhem Bousquet** — guilhem.bousquet@aphp.fr  
ORCID: [0000-0001-5594-6694](https://orcid.org/0000-0001-5594-6694)

---

## Authors & Affiliations

| Author | Affiliation |
|---|---|
| Kelly Larissa Vomo Donfack | Université Sorbonne Paris Nord, LAGA, CNRS, UMR 7539 & IHSM UMA-CSIC, Málaga, Spain |
| Burak Gönüllu | Faculty of Medicine, Yeditepe University, Istanbul, Turkey |
| Frédéric Pamoukjian | Hôpital Avicenne, APHP, Service de Gériatrie |
| Eurydice Angeli | Hôpital Avicenne, APHP, Service d'Oncologie médicale |
| Grégory Ginot | Université Sorbonne Paris Nord, LAGA, CNRS, UMR 7539 |
| Ian Morilla† | Université Sorbonne Paris Nord, LAGA, CNRS, UMR 7539 & IHSM UMA-CSIC |
| Guilhem Bousquet†* | Unité SynKoMIC, Université Sorbonne Paris Nord & Hôpital Avicenne, APHP |
| Géraldine Falgarone† | Unité SynKoMIC, Université Sorbonne Paris Nord & Hôpital Avicenne, APHP |

†co-senior authorship

---

## Funding

No external funding. Kelly Larissa Vomo Donfack received a Ph.D. Grant from Sorbonne Paris Nord University.

## Conflict of Interest

The authors have declared that no conflict of interest exists.

---

## Citation

If you use this code or data in your work, please cite:

```
Vomo Donfack KL, Gönüllu B, Pamoukjian F, Angeli E, Ginot G, Morilla I*, Bousquet G*, Falgarone G*.
Decoding multimorbidity: Understanding cancers, inflammatory chronic diseases contribution to death.
[Journal], [Year]. DOI: [TBD]
```
