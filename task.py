from datetime import datetime
import json
import pandas as pd

class TaskManager:
    """
    A task management system that stores and manages tasks in JSON format.
    
    Provides functionality to create, update, remove, and filter tasks by status.
    All tasks are persisted to a JSON file automatically.
    """

    def __init__(self):
        """Initializes the TaskManager by creating an empty tasks list and loading existing tasks from file."""
        self.tasks = []
        self.load()
        
    def generate_id(self):
        """
        Generates a unique ID for new tasks based on the current number of tasks.
        
        Returns:
            int: Next sequential ID (length of tasks list + 1)
        """
        return len(self.tasks) + 1 if self.tasks else 1

    def add_task(self, description):
        """
        Creates a new Task object with the provided description and adds it to the tasks list.
        Automatically saves changes to file.
        
        Args:
            description (str): The description of the task to create
        """
        new_task = self.Task(self, description)
        self.tasks.append(new_task)
        print(f"new task is created by the id of {new_task.id}")
        self.save()

    def remove_task(self, id):
        """
        Removes a task by its ID and adjusts the IDs of remaining tasks to keep them sequential.
        
        Args:
            id (int): The ID of the task to remove
            
        Returns:
            str: Success or error message
        """
        if id > len(self.tasks) or id <= 0:
            return "Task with given id does not exist"

        for i in range(len(self.tasks)):
            if self.tasks[i].id == id:
                index = i
            elif self.tasks[i].id > id:
                self.tasks[i].id -= 1
            else:
                continue
        self.tasks.pop(index)
        self.save()
        return "Task removed successfully"

    def update_task(self, id, new_description):
        """
        Updates a task's description and sets the updated_at timestamp to the current time.
        
        Args:
            id (int): The ID of the task to update
            new_description (str): The new description for the task
            
        Returns:
            str: Success message
        """
        task = self.tasks[id - 1]
        task.description = new_description
        task.updated_at = datetime.now().strftime("%H:%M:%S %d-%m-%Y")
        self.save()
        return "Task updated successfully"

    def list(self, filter_by_status=None):
        """
        Returns all tasks as a pandas DataFrame. If filter_by_status is provided, only returns tasks matching that status.
        
        Args:
            filter_by_status (str, optional): Filter tasks by status ("todo", "in progress", "Done"). Defaults to None (no filter).
            
        Returns:
            pd.DataFrame: DataFrame containing task information with columns: id, Description, Created at, Status, Updated at
        """
        listed = []
        if filter_by_status is not None:
            for task in self.tasks:
                if task.status == filter_by_status:
                    listed.append(task.to_dict())
        else:
            for task in self.tasks:
                listed.append(task.to_dict())
        
        return pd.DataFrame(listed, columns=["id","Description","Created at","Status","Updated at"])
    

    def mark_in_progress(self, id):
        """
        Changes a task's status to "in progress" and updates the updated_at timestamp.
        
        Args:
            id (int): The ID of the task to mark as in progress
            
        Returns:
            str: Success message
        """
        task = self.tasks[id -1]
        task.status = "in progress"
        task.updated_at = datetime.now().strftime("%H:%M:%S %d-%m-%Y")
        self.save()
        return "Task marked as in progress"
    
    def mark_done(self, id):
        """
        Changes a task's status to "Done" and updates the updated_at timestamp.
        
        Args:
            id (int): The ID of the task to mark as done
            
        Returns:
            str: Success message
        """
        task = self.tasks[id -1]
        task.status = "Done"
        task.updated_at = datetime.now().strftime("%H:%M:%S %d-%m-%Y")
        self.save()
        return "Task marked as Done"
    
    def save(self, filename="tasks.json"):
        """
        Converts all tasks to dictionaries and saves them as JSON to the specified file.
        
        Args:
            filename (str, optional): The name of the file to save to. Defaults to "tasks.json".
            
        Returns:
            str: Success message
        """
        data = [task.to_dict() for task in self.tasks]
        with open(filename, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return "Tasks saved to file successfully"
    
    def load(self, filename="tasks.json"):
        """
        Reads tasks from a JSON file and reconstructs Task objects from the stored data.
        
        Args:
            filename (str, optional): The name of the file to load from. Defaults to "tasks.json".
        """
        with open(filename, "r") as f:
            data = json.load(f)
        
        self.tasks = []
        for item in data:
            task = self.Task(
                self,
                description=item["Description"],
                created_at=item["Created at"],
                status=item["Status"],
                updated_at=item["Updated at"]
            )
            self.id = item["id"]    
            self.tasks.append(task)
    
    class Task:
        """
        Represents a single task with description, status, and timestamps.
        
        This nested class is part of TaskManager and requires a TaskManager instance for ID generation.
        
        Attributes:
            id (int): Unique identifier for the task
            description (str): The task description text
            status (str): Current status ("todo", "in progress", "Done")
            created_at (str): Creation timestamp in format "HH:MM:SS DD-MM-YYYY"
            updated_at (str): Last update timestamp in format "HH:MM:SS DD-MM-YYYY"
        """

        def __init__(self,
                     task_manager,
                     description,
                     created_at=None,
                     status="todo",
                     updated_at=None):
            """
            Initializes a new Task object.
            
            Args:
                task_manager (TaskManager): The TaskManager instance that created this task
                description (str): The description of the task (required)
                created_at (str, optional): Creation timestamp. If None, uses current time
                status (str, optional): Task status. Defaults to "todo"
                updated_at (str, optional): Last update timestamp. If None, uses current time
            """
            self.manager = task_manager
            self.id = self.manager.generate_id()
            self.description = description
            self.status = status
            self.created_at = created_at if created_at is not None else datetime.now().strftime("%H:%M:%S %d-%m-%Y")
            self.updated_at = updated_at if updated_at is not None else datetime.now().strftime("%H:%M:%S %d-%m-%Y")
        
        def to_dict(self):
            """
            Converts a task object into a dictionary format suitable for JSON serialization and DataFrame display.
            
            Returns:
                dict: Dictionary with keys: id, Description, Created at, Status, Updated at
            """
            return {"id":self.id,"Description": self.description,"Created at": self.created_at,"Status": self.status,"Updated at": self.updated_at}


# Example usage
if __name__ == "__main__":
    # Create manager
    manager = TaskManager()

    # Add a task
    manager.add_task("Complete project documentation")

    # List all tasks
    print(manager.list())

    # Mark task as in progress
    manager.mark_in_progress(1)

    # Update task
    manager.update_task(1, "Complete comprehensive documentation")

    # List only completed tasks
    print(manager.list(filter_by_status="Done"))

    # Remove task
    manager.remove_task(1)


