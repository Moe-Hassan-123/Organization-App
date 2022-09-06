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

app = Flask(__name__)
# opens a connection with the database
# Check same thread = False allows to operate on the db from diffrent threads which can be bad for concurrency in a scale
# but that is okay as its a local project for now.
# detect_types is used to allow to store the data in the database as a form of python object as datetime obj for example
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
    # user_id = request.data("user_id")
    return DB.fetch_user(db, 0)

if __name__ == "__main__":
    app.run(debug=True, port=12221)
    db.commit()
