.PHONY: help all bench benchmark gen generate-report clean clean-caches python39 python310 python311 python312 python313

help:
	@echo "Targets:"
	@echo "  make all                       # Clean + run all Python versions + generate report"
	@echo "  make bench | benchmark        # Run benchmarks"
	@echo "  make gen   | generate-report  # Generate Markdown report from CSV"
	@echo "  make clean                    # Remove venvs and results"
	@echo "  make clean-caches             # Clear pip and uv caches"
	@echo "  make python39                 # Run benchmarks only on Python 3.9"
	@echo "  make python310                # Run benchmarks only on Python 3.10"
	@echo "  make python311                # Run benchmarks only on Python 3.11"
	@echo "  make python312                # Run benchmarks only on Python 3.12"
	@echo "  make python313                # Run benchmarks only on Python 3.13"

all: clean clean-caches python39 python310 python311 python312 python313 gen

bench: 
	@chmod +x scripts/run_benchmarks.sh
	./scripts/run_benchmarks.sh

benchmark: bench

gen:
	python3 scripts/compare_results.py \
		results/benchmark_results.csv \
		results/benchmark_results.md

generate-report: gen

clean:
	- find . -maxdepth 1 -type d -name ".venv*" -exec rm -rf {} +
	- rm -rf .venv venv ENV 2>/dev/null || true
	- rm -rf results/* 2>/dev/null || true
	mkdir -p results/logs
	[ -f results/logs/.gitkeep ] || echo "placeholder" > results/logs/.gitkeep

clean-caches:
	@echo "Clearing pip cache..."
	- python3 -m pip cache purge 2>/dev/null || true
	@echo "Clearing uv cache..."
	- uv cache clean 2>/dev/null || true
	@echo "Cache cleanup completed."

python39:
	@chmod +x scripts/run_benchmarks.sh
	PYTHONS_CSV="/opt/homebrew/bin/python3.9" ./scripts/run_benchmarks.sh

python310:
	@chmod +x scripts/run_benchmarks.sh
	PYTHONS_CSV="/opt/homebrew/bin/python3.10" ./scripts/run_benchmarks.sh

python311:
	@chmod +x scripts/run_benchmarks.sh
	PYTHONS_CSV="/opt/homebrew/bin/python3.11" ./scripts/run_benchmarks.sh

python312:
	@chmod +x scripts/run_benchmarks.sh
	PYTHONS_CSV="/opt/homebrew/bin/python3.12" ./scripts/run_benchmarks.sh

python313:
	@chmod +x scripts/run_benchmarks.sh
	PYTHONS_CSV="/opt/homebrew/bin/python3.13" ./scripts/run_benchmarks.sh
