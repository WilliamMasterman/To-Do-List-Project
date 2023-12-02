import matplotlib.pyplot as plt
from datetime import datetime

class Task:
    def __init__(self, title, due_date, description, category, completed=False):
        """
        This represents an individual task

        Returns: None

        Arguments:
            title (str): Title of the task.
            due_date (datetime): Due date of the task
            description (str): Description of the task
            category (str): Category of the task
        """
        self.title = title
        self.due_date = due_date
        self.description = description
        self.category = category
        self.completed = completed
        
class TaskList:
    def __init__(self):
        """
        Initializes category object for class

        Returns: None

        Arguments: None
        """
        self.categories = {}


    def delete_task(self, title: str):
        """
        Deletes a task based on its title

        Returns: None
        
        Arguments: title (str): The title of the task
        """
        if not isinstance(title, str):
            raise TypeError("Invalid input type")
        
        for category, tasks in self.categories.items():
            for task in tasks:
                if task.title == title:
                    tasks.remove(task)
                    print(f"Task '{title}' deleted")
        
    
    def add_task(self, task):
        """
        This adds a task to the corresponding category

        Returns: None

        Arguments: Task (task): task object to be added
        """
        if task.category not in self.categories:
            self.categories[task.category] = []
        self.categories[task.category].append(task)


    def edit_task(self, new_title, new_due_date, new_description, new_category):
        """
        Edits a task with new information

        Returns: None

        Arguments:
            new_title (str): New title of the task
            new_due_date (datetime): New due date of the task
            new_description (str): New description of the task
            new_category (str): New category of the task
        """
        self.title = new_title
        self.due_date = new_due_date
        self.description = new_description
        self.category = new_category