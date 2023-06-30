# Python testing template
# A simple template for testing python code in a python environment
# Github: https://www.github.com/lewisevans2007/python_testing_template
# By: Lewis Evans

# ========== DO NOT EDIT THIS SECTION ==========
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# ==============================================

# Enter tests here and run the file to test modules you put in the modules folder
from modules import add
def test_add():
    result = add.add(1, 2)
    assert result == 3