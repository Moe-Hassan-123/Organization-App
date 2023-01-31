"""
@author: Mohamed Hassan
@email: mdhn6832@gmail.com

Helper Functions used to faciliate unit-testing
"""
import sqlite3

def reset_data_base(cur: sqlite3.Cursor) -> bool:
    """Executes a script to delete all data from the tables in the test database"""
    cur.execute(
        """
        SELECT name FROM sqlite_master WHERE type='table'
        """
    )
    tables = cur.fetchall()
    for table in tables:
        cur.execute(
            f"""
            DELETE FROM {table[0]}
            """
        )
        
def create_schema(cur: sqlite3.Cursor):
    """Excutes a script to initialize the database"""
    # HACK This won't work on any machine other than mine.
    script = open("/home/mohamed/code/Organization Website/server/database/schema.sql",
                  encoding="UTF-8").read()
    cur.executescript(script)


def connect_to_db() -> sqlite3.Cursor:
    """ Connects to a brand new resetted database and returns -
        the cursor
    """
    #pylint: disable=invalid-name
    db: sqlite3.Connection = sqlite3.connect('test.db', check_same_thread=False, detect_types=sqlite3.PARSE_DECLTYPES)
    cur = db.cursor() 
    create_schema(cur)
    reset_data_base(cur)
    db.commit()
    return cur

if __name__ == "__main__":
    connect_to_db()
