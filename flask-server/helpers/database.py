"""
@author: Mohamed Hassan

The Module is used to interact with the database.
it allows adding to, removing from and querying of the database.
"""
#pylint: disable=import-error
import sqlite3
from project import Project

def get_all_projects(cur: sqlite3.Cursor, user_id: int) -> dict:
    """Fetches all projects associated the user id, returns them formated as json.

    Args:
        cur: Takes a cursor to the current active database
        user_id: The current Active User.

    Returns:
        dict: formatted as json, dictionary of a list of projects,
                each project is a 2-list containing the overview and links.
    """
    cur.execute(
        """
        SELECT
            project_id, overview, links
        FROM
            projects
        WHERE
            projects.user_id == (?)
        ORDER BY
            creation_date ASC
        """
        ,
        (
        user_id,
        )
    )

    # Format the data into json data.
    result: dict = {"projects": []}
    for item in cur.fetchall():
        result["projects"].append({
            "overview": item[0],
            "links": item[1],
            "id": item[2],
            })
    return result


def fetch_user(cur: sqlite3.Cursor, user_id: int) -> dict:
    """Fetches user's data from the database

    Args:
        cur: A cursor to the current active databse
        user_id: The current Active User.

    Returns:
        dict: json formatted dict that has the name of the user as "name"
        and the image of the user (blob) as "image"
    """

    cur.execute(
        """
        SELECT
            name, image
        FROM
            users
        WHERE
            id == (?)
        """
        ,
        (
            user_id,
        )
    )
    name, img = cur.fetchall()
    # Return the data formatted as json.
    return {"name": name[0], "image": img[0]}

def get_all_tasks (cur: sqlite3.Cursor, user_id: int):
    """Fetches all the todos for the current user at then "when" time.

    Returns:
        dict: Json Formatted, has all tasks that the user created up untill the when.
    """
    cur.execute(
        """
        SELECT (isdone, task, deadline)
        FROM tasks
        WHERE tasks.project_id
            IN (SELECT projects.project_id
                FROM projects
                WHERE user_id = ?)
        """,
        (
            user_id,
        )
    )
    # TODO turn this into a json and return it.
    print(cur.fetchall())
    return ...


def add_project(cur: sqlite3.Cursor, pro: Project):
    """ Adds a new project to the database

    Returns:
        bool: indicates whether the insertion was succesful or not.
    """
    cur.execute(
        """
        INSERT INTO projects
            ('title', 'overview', 'content', 'user_id')
        VALUES
            (?, ?, ?, ?)
        """
        ,
        (
            pro.title,
            pro.overview,
            pro.content,
            pro.user_id,
        )
    )

    project_id = cur.lastrowid
    for todo in pro.todos:
        cur.execute(
            """
            INSERT INTO tasks (isdone, task, deadline, project_id)
            VALUES
                (?, ?, ?)
            """
            ,
            (
                0,          # False as in not done yet.
                todo[0],    # The Task
                todo[1],    # The Deadline
                project_id, # The Id of the associated project
            )
        )

def delete_project(cur: sqlite3.Cursor, user_id: int, project_id: int):
    """Deletes the project from the database

    Args:
        user_id (int): The user id
        project_id (int): the project title and overview
    """
    cur.execute(
        """
        DELETE FROM projects
        WHERE
            projects_id = ?
        AND
            user_id = ?
        """
        ,
        (
            user_id,
            project_id,
        )
    )
