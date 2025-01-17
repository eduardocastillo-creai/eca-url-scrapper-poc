PYTHON := python3.11
VENV := .venv
ACTIVATE := source $(VENV)/bin/activate
POETRY := poetry

.DEFAULT_GOAL := help

install-poetry:
	@curl -sSL https://install.python-poetry.org | $(PYTHON) -
	@echo "Poetry installed successfully."

create-venv:
	@$(PYTHON) -m venv $(VENV)
	@echo "Virtual environment created at $(VENV)."
	@echo "Activate it using: source $(VENV)/bin/activate"
	@echo "Then run: poetry install to manage dependencies."

install: install-poetry
	@$(POETRY) install --no-root
	@$(POETRY) run python postinstall.py
	@echo "Dependencies installed."

add-dep:
	@[ -n "$(package)" ] || (echo "Error: Please specify a package (e.g., make add-dep package=<package_name>)" && exit 1)
	@$(POETRY) add $(package)

add-dev-dep:
	@[ -n "$(package)" ] || (echo "Error: Please specify a package (e.g., make add-dev-dep package=<package_name>)" && exit 1)
	@$(POETRY) add $(package) --group dev

build:
	@$(POETRY) build

help:
	@echo "Usage:"
	@echo "  make install          Install Poetry and dependencies"
	@echo "  make create-venv      Create and activate a virtual environment"
	@echo "  make add-dep          Add a production dependency (e.g., make add-dep package=<package_name>)"
	@echo "  make add-dev-dep      Add a development dependency (e.g., make add-dev-dep package=<package_name>)"
	@echo "  make build            Build the project for distribution"
