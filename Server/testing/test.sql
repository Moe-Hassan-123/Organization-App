-- insert a user
INSERT INTO users (name, image)
VALUES ("Mohamed", NULL);

-- insert a project for the user

INSERT INTO Projects (title, overview, user_id) 
VALUES ("NOICE", "hello world!", 1);
-- the value of user id will be in the cookies.
