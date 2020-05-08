.PHONY: clean clean-test clean-pyc clean-build develop docs help
.DEFAULT_GOAL := help
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

develop: clean ## install development env
	pip install -e .[testing,docs] --upgrade

clean: clean-test clean-build clean-pyc ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	@rm -fr build/
	@rm -fr dist/
	@rm -fr .eggs/

clean-pyc: ## remove Python file artifacts
	@find wagtailformblocks -name '*.pyc' -delete
	@find tests -name '*.pyc' -delete
	@find . -name '*.egg-info' | xargs rm -rf

clean-test: ## remove test and coverage artifacts
	@rm -fr .tox/
	@rm -f .coverage
	@rm -fr htmlcov/

lint: flake8 isort

flake8:
	@flake8 wagtailformblocks/ tests/

isort:
	@isort --recursive wagtailformblocks/ tests/

test: ## run tests quickly with the default Python
	py.test tests/

test-all: ## run tests on every Python version with tox
	tox

coverage:
	py.test -q --reuse-db tests/ --cov=wagtailformblocks --cov-report=term-missing
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/wagtailformblocks.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ wagtailformblocks
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist
	twine upload -r lukkien dist/*

dist: clean ## builds source and wheel package
	python setup.py sdist bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python setup.py install
