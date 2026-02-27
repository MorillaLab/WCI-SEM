.PHONY: install clean descriptive correlation help

help:
	@echo "multimorbidity-SEM — available commands:"
	@echo "  make install       Install Python dependencies"
	@echo "  make clean         Data cleaning & imputation"
	@echo "  make descriptive   Descriptive statistics (Tables 1 & 2)"
	@echo "  make correlation   Cramér's V correlation matrix"
	@echo "  make all           Run full Python pipeline"

install:
	pip install -r requirements.txt

clean:
	python analysis/01_data_cleaning.py

descriptive:
	python analysis/02_descriptive_stats.py

correlation:
	python analysis/03_correlation_matrix.py

all: clean descriptive correlation
	@echo "Python pipeline complete. Run analysis/04_sem_models.do in Stata 17+ for SEM."
