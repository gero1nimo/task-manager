from time import ctime, sleep

import sys
import json

class Task:
    def __init__(self, description):
        self.description = description
        self.status = "Not Begun"
        self.createdAt = ctime()
        self.updatedAt = None

    def values(self):
        return self.description, self.createdAt, self.status, self.updatedAt

    def to_dict(self):
        return {self.description: {"NAME": self.description, "Creation Date": self.createdAt, "Status": self.status, "Update Date": self.updatedAt}}



class TaskManager:
    def __init__(self):
        self.tasks = []
        self.current_task = None

    def add_task(self, task):
        self.tasks.append(task)
        self.current_task = Task
        return "Task added successfully"

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return "Task deleted successfully"
        return "Task not found"

    def update_task(self, task, new_description):
        if task in self.tasks:
            task.description = new_description
            return "Task updated successfully"

    def load_tasks(self):
        tasks = []
        for i in self.tasks:
            tasks.append(i.to_dict())

        return tasks

    def mark_in_progress(self, task):
        if task in self.tasks:
            task.status = "In Progress"
            task.updatedAt = ctime()
            return "Task updated successfully"

    def mark_done(self, task):
        if task in self.tasks:
            task.status = "Done"
            task.updatedAt = ctime()
            return "Task updated successfully"

    def list_tasks(self, status):
        wanted_tasks = []
        for i in self.tasks:
            if i.status == status:
                wanted_tasks.append (i.to_dict())
        return wanted_tasks


manager = TaskManager()
task1 = Task("Task 1")
task2 = Task("Task 2")
task3 = Task("Task 3")
manager.add_task(task1)
manager.add_task(task2)

manager.mark_done(task1)
manager.mark_in_progress(task2)

print(manager.load_tasks())
print(manager.list_tasks("Done"))