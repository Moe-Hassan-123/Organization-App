-- If i want to use it outside of the local setting i should implement a real user structure,
-- current structure is password-less.


CREATE TABLE IF NOT EXISTS 'users' (
    'user_id'     INTEGER PRIMARY KEY,
    'name'        TEXT NOT NULL,
    'image'       BLOB
  );

-- used to store projects associated with users.
CREATE TABLE IF NOT EXISTS 'projects' (
    'project_id'           INTEGER PRIMARY KEY,
    'title'                TEXT NOT NULL,
    'overview'             TEXT NOT NULL,
    'links'                JSON,
    'creation_date'        TEXT DEFAULT CURRENT_TIMESTAMP,
    'user_id'              INTEGER NOT NULL REFERENCES 'users' --creates a foreign reference with primary key of users
  );

-- store tasks for each project.
CREATE TABLE IF NOT EXISTS tasks (
    'task_id'         INTEGER PRIMARY KEY,
    'isdone'          INTEGER (1),
    'task'            TEXT NOT NULL,
    'project_id'      INTEGER NOT NULL REFERENCES 'projects' --creates a foreign reference with primary key of projects
  );