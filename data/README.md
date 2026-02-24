# Data Availability

The dataset used in this study consists of **677 de-identified patient records** prospectively collected at Hôpital Avicenne (APHP, Bobigny, France) between January 2016 and December 2022.

## Access Policy

Due to patient privacy regulations and French ethical requirements, the raw dataset is **not publicly available**. De-identified data supporting this study are available from the corresponding author upon reasonable request, pending ethical approvals.

**Contact:**
> Prof. Guilhem Bousquet
> Université Sorbonne Paris Nord, UFR SMBH, 1 rue Chablis, 93000 Bobigny, France
> Email: guilhem.bousquet@aphp.fr
> ORCID: [0000-0001-5594-6694](https://orcid.org/0000-0001-5594-6694)

## Dataset Description

| Property | Value |
|---|---|
| Number of patients | 677 |
| Number of variables | 28 |
| Inclusion period | January 2016 – December 2022 |
| Median follow-up (Model 1) | 2.14 years |
| Median follow-up (Model 2) | 3.03 years |
| Data type | Prospective clinical registry |

## Variables Collected

- **Demographics:** age, sex, BMI
- **Cancer data:** cancer site, age at first diagnosis, metastatic status, early or multiple cancers
- **Smoking history:** pack/year index (categorized)
- **Personal disease history:** autoimmune diseases (AID), cardiovascular diseases (CVD), cardiovascular risk factors (CVRF)
- **Familial history:** familial cancer, familial AID, familial CVD, familial CVRF — including early-onset events across first- and second-degree relatives
- **Outcomes:** metastatic disease, death (at 2 and 3 years of follow-up)

## Missing Data

Missing values were observed in the following columns: *smoking*, *age at first cancer diagnosis*, and *early or multiple cancer*. These were imputed using an iterative imputer prior to analysis (see `analysis/01_data_cleaning.py`).

## Ethics & Compliance

In accordance with French law, all patients were informed of the use of their clinical data collected during routine care and did not oppose to it. No additional ethical approval was required for this retrospective use of prospectively collected registry data.
