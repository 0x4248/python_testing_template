# Python testing template
# A simple template for testing python code in a python environment
# Github: https://www.github.com/lewisevans2007/python_testing_template
# By: Lewis Evans

setup: setup-enviroment setup-requirements

setup-enviroment:
	@echo "Setting up python enviroment"
	@python3 -m venv .