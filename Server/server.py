"""
@author: Mohamed Hassan
@email: mdhn6832@gmail.com

Api to control the database and query it
"""

import sqlite3

import helpers.database as DB
from helpers.project import Project

#pylint: disable=broad-except


# Check same thread = False allows to operate on the db from diffrent threads -
# which can be bad for concurrency in a scale but that is okay as its a local project for now.
db = sqlite3.connect('./database/db.sqlite3', check_same_thread=False)
cur = db.cursor()
# adds the necessary schema from schema.sql
cur.executescript( open("./database/schema.sql", encoding="UTF-8").read() )

def retrieve_projects(user_id: int) -> dict:
    """ retrives the data of the projects created by the user from the database.

    Returns:
        dict: The projects in the form of json Object.
    """
    return DB.get_all_projects(cur, user_id)

def add_project(data: dict) -> tuple:
    """ Adds a new project to the database

    Returns:
        2-tuble:
        [0]: bool: determines the sucsess or failure of the operation
        [1]: str: A message to be printed.
    """

    proj = Project(**data)

    try:
        DB.add_project(cur, proj)
        db.commit()
    except Exception as err_msg:
        return 0, err_msg
    
    return 1, "The project has been added succesfully"


def get_user_data(user_id: int) -> str:
    """Gets the name of the user from the database

    Returns:
        str: name of the user.
    """
    # HACK since i have a no authentication sign-in in my mind
    # the user id will be a value attached to a button that when clicked
    # will call this function and pass the user_id in a post request.
    # this can be the basis for a sign-in system but its not needed as its a local project.
    return DB.fetch_user(cur, user_id)


def delete_project(user_id: int, project_id: int):
    """
    Deletes a project from the database.
    Args:
        user_id (int): the id of the user that owns the project.
        project_id (int): the id of the project that should be deleted.
    Returns:
        2-list:
        [0]:  bool: indicates whether the insertion was successful or not.
        [1]:  str: a message to be displayed
    """
    try:
        DB.delete_project(cur, user_id, project_id)
        db.commit()
    except Exception as err_msg:
        return {"result": [0, err_msg]}
    return {"result": [1, "The Project was deleted succesfully"]}
