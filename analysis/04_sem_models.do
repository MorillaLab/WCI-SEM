/* 
04_sem_models.do
----------------
Structural Equation Modeling (SEM) for the multimorbidity study.
All models built and tested in STATA using maximum likelihood estimation.

Models:
    Model 1 — Full cohort, median follow-up 2.14 years
    Model 2 — Full cohort, median follow-up 3.03 years
    Model 3 — Full cohort + Late Chronic Disease latent variable (3yr follow-up)
    Model 4 — Women only (3yr follow-up)

Latent variables:
    Inflammaging        <- sex, smoking, bmi
    FamilialCancerRisk  <- familial_cancer, early_familial_cancer
    FamilialVascularRisk <- familial_cvd, early_familial_cvd, familial_cvrf, early_cvrf
    EarlyChronicDisease <- early_aid, severe_aid, early_cvd, early_cvrf

Fit indices reported: chi2, CFI, RMSEA, SRMR
Cutoffs: CFI > 0.90, RMSEA < 0.06, SRMR < 0.08

Authors: Kelly Larissa Vomo Donfack, Frédéric Pamoukjian
*/

* ── Load data ─────────────────────────────────────────────────────────────────
use "data/cleaned_data.dta", clear

* ── Standardize continuous variables ─────────────────────────────────────────
foreach v in age smoking bmi age_first_cancer_dx {
    egen z_`v' = std(`v')
}

* ══════════════════════════════════════════════════════════════════════════════
* MODEL 1 — Full cohort, 2-year follow-up
* ══════════════════════════════════════════════════════════════════════════════
sem ///
    (Inflammaging        -> z_sex z_smoking z_bmi) ///
    (FamilialCancerRisk  -> familial_cancer early_familial_cancer) ///
    (FamilialVascularRisk -> familial_cvd early_familial_cvd familial_cvrf early_cvrf) ///
    (EarlyChronicDisease -> early_aid severe_aid early_cvd early_cvrf) ///
    (FamilialVascularRisk -> FamilialCancerRisk) ///
    (FamilialCancerRisk  -> Inflammaging) ///
    (Inflammaging        -> cancer metastatic_2yr death_2yr) ///
    (EarlyChronicDisease -> Inflammaging FamilialVascularRisk early_or_multiple_cancer) ///
    (cancer              -> metastatic_2yr) ///
    (metastatic_2yr      -> death_2yr) ///
    , method(ml) standardized

* Store fit statistics
estat gof, stats(all)
estimates store model1

* ══════════════════════════════════════════════════════════════════════════════
* MODEL 2 — Full cohort, 3-year follow-up
* ══════════════════════════════════════════════════════════════════════════════
sem ///
    (Inflammaging        -> z_sex z_smoking z_bmi) ///
    (FamilialCancerRisk  -> familial_cancer early_familial_cancer) ///
    (FamilialVascularRisk -> familial_cvd early_familial_cvd familial_cvrf early_cvrf) ///
    (EarlyChronicDisease -> early_aid severe_aid early_cvd early_cvrf) ///
    (FamilialVascularRisk -> FamilialCancerRisk) ///
    (FamilialCancerRisk  -> Inflammaging) ///
    (Inflammaging        -> cancer metastatic_3yr death_3yr) ///
    (EarlyChronicDisease -> Inflammaging FamilialVascularRisk early_or_multiple_cancer) ///
    (cancer              -> metastatic_3yr) ///
    (metastatic_3yr      -> death_3yr) ///
    , method(ml) standardized

estat gof, stats(all)
estimates store model2

* ══════════════════════════════════════════════════════════════════════════════
* MODEL 3 — Full cohort + Late Chronic Disease (3-year follow-up)
* ══════════════════════════════════════════════════════════════════════════════
sem ///
    (Inflammaging        -> z_sex z_smoking z_bmi) ///
    (FamilialCancerRisk  -> familial_cancer early_familial_cancer) ///
    (FamilialVascularRisk -> familial_cvd early_familial_cvd familial_cvrf early_cvrf) ///
    (EarlyChronicDisease -> early_aid severe_aid early_cvd early_cvrf) ///
    (LateChronicDisease  -> at_least_2cvrf at_least_1aid) ///
    (FamilialVascularRisk -> FamilialCancerRisk) ///
    (FamilialCancerRisk  -> Inflammaging) ///
    (Inflammaging        -> cancer metastatic_3yr death_3yr LateChronicDisease) ///
    (EarlyChronicDisease -> Inflammaging FamilialVascularRisk early_or_multiple_cancer) ///
    (cancer              -> metastatic_3yr) ///
    (metastatic_3yr      -> death_3yr) ///
    , method(ml) standardized

estat gof, stats(all)
estimates store model3

* ══════════════════════════════════════════════════════════════════════════════
* MODEL 4 — Women only (3-year follow-up)
* ══════════════════════════════════════════════════════════════════════════════
preserve
keep if sex_female == 1

* Smoking and BMI treated as continuous (not categorical) in women's model
sem ///
    (Inflammaging        -> z_age z_smoking z_bmi) ///
    (FamilialCancerRisk  -> familial_cancer early_familial_cancer) ///
    (FamilialVascularRisk -> familial_cvd early_familial_cvd familial_cvrf early_cvrf) ///
    (EarlyChronicDisease -> early_aid severe_aid early_cvd early_cvrf) ///
    (FamilialVascularRisk -> FamilialCancerRisk EarlyChronicDisease early_or_multiple_cancer) ///
    (FamilialCancerRisk  -> Inflammaging) ///
    (Inflammaging        -> death_3yr) ///
    (early_or_multiple_cancer -> metastatic_3yr) ///
    (metastatic_3yr      -> death_3yr) ///
    , method(ml) standardized

estat gof, stats(all)
estimates store model4

restore

* ── Model comparison ──────────────────────────────────────────────────────────
estimates table model1 model2 model3, stats(chi2 df_m rmsea cfi srmr) b(%9.3f)

* ── Export standardized coefficients ─────────────────────────────────────────
foreach m in model1 model2 model3 model4 {
    estimates restore `m'
    estat teffects, compact
    outreg2 using "results/sem_`m'_coefficients.xls", replace
}
