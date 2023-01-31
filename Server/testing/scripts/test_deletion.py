"""Tests the Adding Project Function
"""
# HACK pylint complains about the path append being before the import.
# this was the only sensible solution.
#pylint: disable=import-error
#pylint: disable=wrong-import-position

import sys
sys.path.append('/home/mohamed/code/Organization Website/helpers')
sys.path.append('/home/mohamed/code/Organization Website/testing/')
from test_functions import connect_to_db
from database import delete_project


connect_to_db()

# def test_deletion_from_empty_database():
#     """Checks"""
#     assert delete_project(1, 1) is False