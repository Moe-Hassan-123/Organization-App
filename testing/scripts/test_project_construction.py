"""Tests the Adding Project Function
"""

# HACK pylint complains about the path append being before the imports.
# this was the only sensible solution for my code structure.
#pylint: disable=import-error
#pylint: disable=wrong-import-position

import sys
sys.path.append('/home/mohamed/code/Organization Website/flask-server/helpers')
sys.path.append('/home/mohamed/code/Organization Website/testing/')
import pytest
# My Own testing faciliation libraries
import test_data as td

# The class being tested.
from project import Project

def test_empty_title():
    """tests adding a project with title being empty"""
    with pytest.raises(ValueError, match="Title can't be empty"):
        Project(**td.empty_title)

def test_title_wrong_type():
    """Checks that the type of the title is str"""
    with pytest.raises(TypeError, match="Title is not a string"):
        Project(**td.title_not_str)

def test_empty_overview():
    """tests adding a project with Overview being an empty string"""
    with pytest.raises(ValueError, match="Overview can't be empty"):
        Project(**td.empty_overview)

def test_overview_wrong_type():
    """tests creating a project with none overview"""
    with pytest.raises(TypeError, match="Overview is not a string"):
        Project(**td.overview_not_str)

def test_content_wrong_type():
    """Makes Sure content passed is a str"""
    with pytest.raises(TypeError, match="Content is not a string"):
        Project(**td.content_not_str)


def test_todo_wrong_format():
    """
        Checks that todo has the format of being a list of lists
        or an empty list if no todos were provided.
    """

    with pytest.raises(TypeError, match="Todos must be a list of lists"):
        Project(**td.todo_not_formatted_correctly)


def test_todo_wrong_type():
    """Checks that todo is a list of lists
    """
    with pytest.raises(TypeError, match="Todos must be a list of lists"):
        Project(**td.todo_not_list)


def test_correct_data():
    """tests adding a project with correct data"""
    Project(**td.correct_project_data)
