"""
@author: Mohamed Hassan
@email: mdhn6832@gmail.com

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
        dict: formatted as json, dictionary of a list of projects
    """
    cur.execute(
        """
        SELECT
            project_id, title, overview, content
        FROM
            projects
        WHERE
            projects.user_id == (?)
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


def fetch_user(cur: sqlite3.Cursor, user_id: int) -> str:
    """Fetches user's data from the database

    Args:
        cur: A cursor to the current active databse
        user_id: The current Active User.

    Returns:
        str: Name of the user
    """

    cur.execute(
        """
        SELECT
            name
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
    return cur.fetchall()[0]

def get_all_todos (cur: sqlite3.Cursor, user_id: int) -> list:
    """Fetches all the todos for the current user at then "when" time.

    Returns:
        list: all tasks that the user created.
        [0]: str: the project that the task belongs into.
        [1]: str: the statement of the todo.
        [2]: bool: determines if the task is done or not.
    """
    
    # TODO get the names of the projects and link them with
    # their id so that i can match it in the results below
    # and return the name of the project instead of the id.
    
    projects = {}
    cur.execute(
        """
        SELECT (project_id, task, isdone)
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
    todos = cur.fetchall()
    # replace the number of the project with the project it self
    for todo in todos:
        todo[0] = projects[todo[0]]
    return todos


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
