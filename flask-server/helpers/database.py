"""
@author: Mohamed Hassan
The Module is used to interact with the database.

it allows adding and removing and querying of the database.
"""
import sqlite3

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
            overview, links
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
    result = {"projects": []}
    for item in cur.fetchall():
        result["projects"].append({
            "overview": item[0],
            "links": item[1]
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
    return {"name": name[0], "image": img[0]}
