"""
@author: Mohamed Hassan.
The Backend Server for my Organization App.

it has a list of api calls that allows
the react app to interact with the database
"""

import json
import sqlite3
from flask import(
            Flask,
            )
import helpers.database as DB

app = Flask(__name__)
# opens a connection with the database
db = sqlite3.connect('./database/db.sqlite3', check_same_thread=False)
# opens a cursor to be able to control the database and query it
cur = db.cursor()
# adds the necessary schema from schema.sql
cur.executescript( open("./database/schema.sql", encoding="UTF-8").read() )

@app.route("/projects")
def retrieve_projects() -> json:
    """ retrives the data of the projects created by the user from the database.

    Returns:
        dict: The projects in the form of json Object.
    """
    # request.data("user_id")
    return DB.get_all_projects(cur, 1)


@app.route('/add', methods=["POST"])
def add_project() -> bool:
    """ Adds a new project to the database

    Returns:
        bool: indicating whether or not the operation was successful.
    """
    # TODO Build a function to add a project
    # it should return a bool to determine whether or not it was successful
    return True


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
