-- Get All Projects
SELECT
    content
FROM 
    projects
WHERE 
    projects.user_id == (?)
ORDER BY
    creation_date ASC
