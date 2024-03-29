import unittest
from datetime import datetime
from ToDoList_Final import Task, TaskList

class TestTaskList(unittest.TestCase):
    def setUp(self):
        self.task_list = TaskList()

    def test_mark_task_complete(self):
        #create task and add to task list
        task_title = "Test Task"
        task_due_date = datetime.now()
        task_description = "Test Description"
        task_category = "Test Category"
        task = Task(task_title, task_due_date, task_description, task_category)
        self.task_list.add_task(task)

        #mark task complete
        self.task_list.mark_task_complete(task_title)

        #check if it is correctly maked complete
        for tasks in self.task_list.categories.values():
            for task in tasks:
                if task.title == task_title:
                    self.assertTrue(task.completed, f"Task '{task_title}' should be marked as complete")
                    return

        #if input title is not found, test should fail
        self.fail(f"Task '{task_title}' not found in the task list")

    def test_add_task(self):
        #make sure task is added correctly
        task = Task("Test Task", datetime(2023, 1, 1), "Test Description", "Test Category")
        self.task_list.add_task(task)
        self.assertIn(task, self.task_list.categories.get("Test Category", []))

    def test_delete_task(self):
        #make sure task correctly deletes
        task = Task("Test Task", datetime(2023, 1, 1), "Test Description", "Test Category")
        self.task_list.add_task(task)
        self.task_list.delete_task("Test Task")
        self.assertNotIn("Test Task", [t.title for t in self.task_list.categories.get("Test Category", [])])

    def test_view_tasks(self):
        #create 2 tasks mand make sure that they display correctly
        task1 = Task("Task 1", datetime(2023, 1, 1), "Description 1", "Category 1")
        task2 = Task("Task 2", datetime(2023, 1, 2), "Description 2", "Category 1")
        self.task_list.add_task(task1)
        self.task_list.add_task(task2)

        expected_output = (
            "\n===== Category: Category 1 =====\n"
            "Title: Task 1\n"
            "Due Date: 2023-01-01 00:00:00\n"
            "Description: Description 1\n"
            "Category: Category 1\n"
            "Completed: No\n\n"
            "Title: Task 2\n"
            "Due Date: 2023-01-02 00:00:00\n"
            "Description: Description 2\n"
            "Category: Category 1\n"
            "Completed: No\n\n"
        )

        actual_output = self.task_list.view_tasks()
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
