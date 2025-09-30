.PHONY: env gen train eval aware clean-data clean-env help all

SHELL := /bin/zsh

env: ## Create Python virtual environment with uv and install dependencies
	uv venv .venv
	. .venv/bin/activate && uv sync
	. .venv/bin/activate && python -m ipykernel install --user --name=the-bark-bias-cure --display-name="The Bark Bias Cure"

gen: ## Generate the dataset
	. .venv/bin/activate && python utils/generate_data.py

train: ## Train the model
	. .venv/bin/activate && python utils/train_model.py

eval: ## Evaluate the model
	. .venv/bin/activate && python utils/evaluate_model.py

aware: ## Generate bias awareness content
	. .venv/bin/activate && python utils/raise_awareness.py

clean-data: ## Remove generated models, data, and reports artifacts
	setopt local_options null_glob; rm -rf models/* data/* reports/*
	mkdir -p models data reports

clean-env: ## Remove the Python virtual environment and kernel
	- jupyter kernelspec remove -f the-bark-bias-cure || true
	rm -rf .venv

help: ## Show this help message
	@printf "Available targets:\n"
	@awk 'BEGIN {FS=":.*##"; printf "\n"} /^[a-zA-Z0-9_-]+:.*##/ { printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

all: env gen train eval aware ## Setup env, generate data, train, evaluate, and awareness


