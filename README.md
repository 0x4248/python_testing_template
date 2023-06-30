# Python testing template

This is a template for testing python code in a python environment.

There is a makefile which automaticity creates a virtual environment and installs the requirements.

# Usage

First you need to set up a virtual environment. This can be done by running the following command:

```bash
make setup
```

or if you are using windows:

```bash
python -m venv .
```

# Setup

You will also need to install the requirements. This can be done by running the following command:

```bash
# Install requirements
pip install -r scripts\requirements\requirements.txt
# Install top ten requirements
pip install -r scripts\requirements\top_ten.txt
```

# Files

## Main.py

This is where the main code goes. This is the code that you want to test.

## Modules

Put in here python modules and functions that you want to test.

## Test

In this folder you can put in tests for your modules and functions. To run the tests, run the following command from the root of the project:

```bash
pytest
```