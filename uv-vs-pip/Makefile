.PHONY: help all bench benchmark gen generate-report graph clean clean-caches python39 python310 python311 python312 python313

# Default number of iterations
ITERATIONS ?= 3

help:
	@echo "Targets:"
	@echo "  make all                       # Clean + run all Python versions + generate report"
	@echo "  make bench | benchmark        # Run benchmarks (default: 3 iterations)"
	@echo "  make gen   | generate-report  # Generate Markdown report from CSV"
	@echo "  make graph                     # Generate performance graphs (PNG)"
	@echo "  make clean                    # Remove venvs and results"
	@echo "  make clean-caches             # Clear pip and uv caches"
	@echo "  make python39                 # Run benchmarks only on Python 3.9"
	@echo "  make python310                # Run benchmarks only on Python 3.10"
	@echo "  make python311                # Run benchmarks only on Python 3.11"
	@echo "  make python312                # Run benchmarks only on Python 3.12"
	@echo "  make python313                # Run benchmarks only on Python 3.13"
	@echo ""
	@echo "Environment Variables:"
	@echo "  ITERATIONS=N                  # Number of iterations per Python version (default: 3)"
	@echo "  PYTHONS_CSV=path1,path2       # Override Python versions to test"
	@echo ""
	@echo "Examples:"
	@echo "  make bench                    # Run 3 iterations (default)"
	@echo "  make bench ITERATIONS=5       # Run 5 iterations"
	@echo "  make python39 ITERATIONS=10  # Run Python 3.9 with 10 iterations"

all: clean clean-caches python39 python310 python311 python312 python313 gen

bench: 
	@chmod +x scripts/run_benchmarks.sh
	ITERATIONS=$(ITERATIONS) ./scripts/run_benchmarks.sh

benchmark: bench

gen:
	python3 scripts/compare_results.py \
		results/benchmark_results.csv \
		results/benchmark_results.md \
		results/benchmark_results.png

generate-report: gen

graph:
	python3 scripts/compare_results.py \
		results/benchmark_results.csv \
		results/benchmark_results.md \
		results/benchmark_results.png

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
	ITERATIONS=$(ITERATIONS) PYTHONS_CSV="/opt/homebrew/bin/python3.9" ./scripts/run_benchmarks.sh

python310:
	@chmod +x scripts/run_benchmarks.sh
	ITERATIONS=$(ITERATIONS) PYTHONS_CSV="/opt/homebrew/bin/python3.10" ./scripts/run_benchmarks.sh

python311:
	@chmod +x scripts/run_benchmarks.sh
	ITERATIONS=$(ITERATIONS) PYTHONS_CSV="/opt/homebrew/bin/python3.11" ./scripts/run_benchmarks.sh

python312:
	@chmod +x scripts/run_benchmarks.sh
	ITERATIONS=$(ITERATIONS) PYTHONS_CSV="/opt/homebrew/bin/python3.12" ./scripts/run_benchmarks.sh

python313:
	@chmod +x scripts/run_benchmarks.sh
	ITERATIONS=$(ITERATIONS) PYTHONS_CSV="/opt/homebrew/bin/python3.13" ./scripts/run_benchmarks.sh
