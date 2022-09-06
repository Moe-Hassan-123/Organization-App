"""
@author: Mohamed Hassan.
The Backend Server for my Organization App.

it has a list of api calls that allows
the react app to interact with the database
"""

import sqlite3
from flask import(
            Flask,
            )
import helpers.database as DB
from helpers.project import Project
import project

app = Flask(__name__)

# opens a connection with the database
# Check same thread = False allows to operate on the db from diffrent threads -
# which can be bad for concurrency in a scale but that is okay as its a local project for now.
db = sqlite3.connect('./database/db.sqlite3', check_same_thread=False)
# opens a cursor to be able to control the database and query it
cur = db.cursor()
# adds the necessary schema from schema.sql
cur.executescript( open("./database/schema.sql", encoding="UTF-8").read() )

@app.route("/projects")
def retrieve_projects() -> dict:
    """ retrives the data of the projects created by the user from the database.

    Returns:
        dict: The projects in the form of json Object.
    """
    # TODO REPLACE 1 with the user_id coming from the request.
    return DB.get_all_projects(cur, 1)


@app.route('/add', methods=["POST"])
def add_project() -> dict:
    """ Adds a new project to the database

    Returns:
        dict: Formatted as json, first value is a bool wheteher it worked or not.
                                 the second value is a message to be displayed. 
    """
    #pylint: disable=broad-except

    # TODO get data from request.
    data = {}
    proj = Project(**data)
    try:
        DB.add_project(cur, proj)
    except Exception as err_msg:
        return {"result": [0, err_msg]}
    return {"result": [1, "The project has been added succesfully"]}


@app.route('/img', methods=["POST"])
def get_user_data():
    """returns the data of the user in the form of a json.

    Returns:
        dict: formatted as json with the name and image of the user.
    """
    # TODO since i have a no authentication sign-in in my mind
    # the user id will be a value attached to a button that when clicked
    # will call this function and pass the user_id in a post request.
    # from 1 to 6 perhaps for 6 users.
    # this can be the basis for a sign-in system but its not needed as its a local project.
    return DB.fetch_user(db, 0)

@app.route('/delete', methods=["POST"])
def method_name():
    """
    Deletes a project from the database.
    Returns:
        2-list:
        [0]:  bool: indicates whether the insertion was successful or not.
        [1]:  str: a message to be displayed
    """
    ## TODO GET THESE VALUES FROM THE REQUEST
    user_id = project_id = 0
    try:
        DB.delete_project(cur, user_id, project_id)
    except Exception as err_msg:
        return {"result": [0, err_msg]}
    return {"result": [1, "The Project was deleted succesfully"]}


if __name__ == "__main__":
    app.run(debug=True, port=12221)
    db.commit()
