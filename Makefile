.PHONY: clean-pyc clean-build help test
.DEFAULT_GOAL := help

help: ## print this help screen
	@perl -nle'print $& if m{^[a-zA-Z0-9_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'

clean: clean-build clean-pyc
	@echo "all clean now .."

clean-build: ## remove build artifacts
	@rm -fr build/
	@rm -fr dist/
	@rm -fr htmlcov/
	@rm -fr *.egg-info
	@rm -rf .coverage

clean-pyc: ## remove Python file artifacts
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*.orig' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +

init: ## create virtualenv for python3
	pipenv install --dev

init2: ## create virtualenv for python2
	pipenv install --two
	pipenv install "django<2.0"

lint: ## check style with flake8
	flake8 pypugjs

test: ## run testsuite
	@SCRIPT_DIR=$$( cd "$$( dirname "$$0" )" && pwd ); \
	export PYTHONPATH=$$PYTHONPATH:$$SCRIPT_DIR; \
	nosetests -w pypugjs/testsuite/  # --nocapture for debugging

coverage:  ## test and generate coverage data
	@SCRIPT_DIR=$$( cd "$$( dirname "$$0" )" && pwd ); \
	export PYTHONPATH=$$PYTHONPATH:$$SCRIPT_DIR; \
	nosetests -w pypugjs/testsuite/ --with-coverage

view-coverage: ## open coverage report in the browser
	@coverage report -m
	@coverage html
	@open htmlcov/index.html

release: clean ## package and upload a release (working dir must be clean)
	@scripts/bumpversion.sh && python setup.py bdist_wheel && twine upload dist/*
