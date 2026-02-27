# Contributing to multimorbidity-SEM

Thank you for your interest in contributing! Here's how to get involved.

## 🐛 Reporting Bugs

Open a [GitHub Issue](https://github.com/MorillaLab/multimorbidity-SEM/issues) with:
- A clear title and description
- The script or notebook where the issue occurs
- Steps to reproduce, including Python/Stata versions
- Expected vs. actual behaviour

## 💡 Suggesting Analyses or Features

Open an issue tagged `enhancement` describing the proposed analysis and its scientific rationale.

## 🔧 Submitting Code

1. Fork the repository and create a branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Keep analysis scripts modular and well-commented.
3. For Stata `.do` files, include a header block with author, date, and description.
4. Clear notebook cell outputs before committing.
5. Open a pull request against `main` with a description of the change and why it's needed.

## 📋 Code Style

- Python: PEP 8, formatted with `black`
- Variable names: descriptive, snake_case
- Stata: use `label variable` for all variables and include `log using` at the top of each `.do` file

## 📜 License

By contributing, you agree that your contributions will be licensed under GPL-3.0.
