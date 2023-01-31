""" The Data used in unit tests
"""
correct_user_data = {
    "user_id": 1,
    "name": "Mohamed",
    "image": None,
}

correct_project_data = {
    "title": "test_title",
    "overview": "test_overview",
    "content": "test_content",
    "user_id": 1,
    "todos": [
        ["todo1", "task1"],
        ["todo2", "task2"],
    ]
}


################################# PROJECT ERRORS #################################

###################################
####### Title Errors ############## test_project_construction.py
empty_title = correct_project_data.copy()
empty_title["title"] = ""

title_not_str = correct_project_data.copy()
title_not_str["title"] = 123
###################################


###################################
####### Overview Errors ########### test_project_construction.py
empty_overview = correct_project_data.copy()
empty_overview["overview"] = ""

overview_not_str = correct_project_data.copy()
overview_not_str["overview"] = 123
###################################


###################################
####### Content Errors ############ test_project_construction.py
content_not_str = correct_project_data.copy()
content_not_str["content"] = 1.0
###################################


###################################
####### To-Do Errors ############### test_project_construction.py
todo_not_list = correct_project_data.copy()
todo_not_list["todos"] = {}

# Correct format should be
# [[1,2], [3,4], [5,6]] list of 2-item lists
todo_not_formatted_correctly = correct_project_data.copy()
todo_not_formatted_correctly["todos"] = [1, 2, 3]
###################################


###################################
####### Wrong Id Errors ########### test_adding_to_database.py
non_existent_user_id = correct_user_data.copy()
non_existent_user_id["user_id"] = 100
###################################


###################################
####### Wrong Project ID ########## test_adding_to_database.py
project_id_wrong_type = correct_project_data.copy()
project_id_wrong_type["project_id"] = "Wrong Type"
###################################


################################# USER ERRORS #################################

###################################
####### Wrong User Name ########### test_project_construction.py
user_name_wrong_type = correct_user_data.copy()
user_name_wrong_type["name"] = 123

user_id_wrong_type = correct_user_data.copy()
user_id_wrong_type["user_id"] = "Should be an int"
###################################
