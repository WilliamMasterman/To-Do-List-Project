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

    
    def add_task(self, task):
        """
        This adds a task to the corresponding category

        Returns: None

        Arguments: Task (task): task object to be added
        """
        if task.category not in self.categories:
            self.categories[task.category] = []
        self.categories[task.category].append(task)


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

                    #if the category doesnt have anything in it, remove the category
                    #Keeps the category around until its not useful anymore
                    if not tasks:
                        del self.categories[category]
                        print(f"Category '{category}' removed")

                    return

        #if the title isnt found, tell user
        print(f"Task '{title}' not found")


    def view_tasks(self):
        """
        Creates formatted str for all aspects of task

        Returns: A string containing information about each task for each defining category

        Arguments: None
        """
        tasks_str = ""
        for category, tasks in self.categories.items():
            tasks_str += f"\n===== Category: {category} =====\n"
            #Displaying the information given via user input
            for task in tasks:
                tasks_str += f"Title: {task.title}\n"
                tasks_str += f"Due Date: {task.due_date}\n"
                tasks_str += f"Description: {task.description}\n"
                tasks_str += f"Category: {task.category}\n"
                tasks_str += f"Completed: {'Yes' if task.completed else 'No'}\n\n"
        return tasks_str


    def edit_task(self, title, new_title, new_due_date, new_description, new_category):
        """
        Edits a task with new information

        Returns: None

        Arguments:
            title (str): title of the task to be edited
            new_title (str): New title of the task
            new_due_date (datetime): New due date of the task
            new_description (str): New description of the task
            new_category (str): New category of the task
        """
        for tasks in self.categories.values():
            for task in tasks:
                # goes through and checks to see if the edited values are correct
                if task.title == title:
                    task.title = new_title
                    task.due_date = new_due_date
                    task.description = new_description
                    task.category = new_category
                    print(f"Task '{title}' edited")
                    return

        #if the title is not found print an error and restart the menu
        print(f"Task '{title}' not found")


    def mark_task_complete(self, title):
        """
        Marks a task as complete

        Returns: None
        prints a message about whether the task was marked complete
        
        Arguments: title (str): the title of the task that is to be completed
        """
        for tasks in self.categories.values():
            # goes through the value pair of the dict and changes task.completed to be true
            for task in tasks:
                if task.title == title:
                    task.completed = True
                    print(f"Task '{title}' marked as complete")
                    return

        #if input title is not found throw error
        print(f"Task '{title}' not found")

class SpecialProjects(TaskList):

    def add_task_to_project(self, task, project_name):
        """
        Adds a task to a specific project

        Returns: None

        Arguments:
            task (Task): the task to be added to the project
            project_name (str): the name of the project to which the task will be added
        """
        #this checks to see if the project name is in the categories dict
        #if not it creates an emoty list
        # if it is then it appends a task
        if project_name not in self.categories:
            self.categories[project_name] = []
        self.categories[project_name].append(task)

    def view_completion_rate(self):
        """
        Calculates and returns the completion rate of tasks that are not overdue

        Returns: str - a string indicating the completion rate

        Arguments: None
        """
        total_tasks = 0
        completed_tasks = 0

        #iterates through all tasks and adds one to the total task counter
        for tasks in self.categories.values():
            for task in tasks:
                total_tasks += 1
                #checks to see if the task was completed before the due date,
                #if yes then it adds one to the completed task counter
                if datetime.now() <= task.due_date and task.completed:
                    completed_tasks += 1

        #calculates the completion rate
        if total_tasks == 0:
            completion_rate = 0
        else:
            completion_rate = (completed_tasks / total_tasks) * 100

        #returns the completion rate to 2 decimal points
        return f"Completion Rate: {completion_rate:.2f}%"