"""
A Class That allows to compress all the data about the project into a single class instance.
"""

#pylint: disable=too-many-arguments

class Project ():
    """Stores the data of the project"""
    def __init__(self,
                 title: str,
                 overview: str,
                 content: str,
                 todos: list,
                 user_id: int,
                 project_id: int|None = None
                 ) -> None:
        self.title: str = title
        self.overview: str = overview
        self.content: str = content
        self.todos: list = todos
        self.user_id: int = user_id
        self.project_id: int|None = project_id

    @property
    def title(self) -> str:
        """Returns the title of the project"""
        return self._title

    @title.setter
    def title(self, val: str) -> None:
        """sets the title of the project"""
        if not isinstance(val, str):
            raise TypeError("Title is not a string")
        if val == "":
            raise ValueError("Title can't be empty")
        self._title = val

    @property
    def overview(self) -> str:
        """returns the overview of the project"""
        return self._overview

    @overview.setter
    def overview(self, val: str) -> None:
        """sets the overview of the project"""
        if not isinstance(val, str):
            raise TypeError("Overview is not a string")
        if val == "":
            raise ValueError("Overview can't be empty")
        self._overview = val

    @property
    def content(self) -> str:
        """returns the content of the project"""
        return self._content

    @content.setter
    def content(self, val: str) -> None:
        """sets the content of the project"""
        if not isinstance(val, str):
            raise TypeError("Content is not a string")
        self._content = val

    @property
    def todos(self) -> list:
        """returns the todos of the project"""
        return self._todos

    @todos.setter
    def todos(self, val: list) -> None:
        """sets the todos of the project"""
        # HACK this has a very very bad computation complexity O(N).
        # If this should ever go to real production this should be
        # removed and replaced with a better method.
        if not isinstance(val, list):
            raise TypeError("Todos must be a list of lists")
        for todo in val:
            if not isinstance(todo, list):
                raise TypeError("Todos must be a list of lists")
        self._todos = val


