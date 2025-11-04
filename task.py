from datetime import datetime
import pandas as pd

class TaskManager:

    def __init__(self):
        self.tasks = []

    def generate_id(self):
        return len(self.tasks) + 1

    def add_task(self, description):
        new_task = self.Task(self, description)
        self.tasks.append(new_task)
        print(f"new task is created by the id of {new_task.id}")

    def remove_task(self, id):
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
        return "Task removed successfully"

    def update_task(self, id, new_description):
        task = self.tasks[id - 1]
        task.description = new_description
        task.updated_at = datetime.now().strftime("%H:%M:%S %d-%m-%Y")
        
        return "Task updated successfully"

    def list(self, filter_by_status=None):
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
        task = self.tasks[id -1]
        task.status = "in progress"
        task.updated_at = datetime.now().strftime("%H:%M:%S %d-%m-%Y")

        return "Task marked as in progress"
    
    def mark_done(self,id):
        task = self.tasks[id -1]
        task.status = "Done"
        task.updated_at = datetime.now().strftime("%H:%M:%S %d-%m-%Y")
        return "Task marked as Done"

    class Task:

        # Simple Task schema for task manager. The variable "task_manager" is the instance of outer class, which is the TaskManager class.
        # Description must be given as parameter for the task to be created.
        # The other parameters are all default by constructor __init__ method. If needs be, the parameters can be given and the task is created accordingly.

        def __init__(self,
                     task_manager,
                     description,
                     created_at=None,
                     status= "todo",
                     updated_at=None):
            
            self.manager = task_manager
            self.id = self.manager.generate_id()
            self.description = description
            self.status = status
            self.created_at = created_at if created_at is not None else datetime.now().strftime("%H:%M:%S %d-%m-%Y")
            self.updated_at = updated_at if updated_at is not None else datetime.now().strftime("%H:%M:%S %d-%m-%Y")
        
        def to_dict(self):
            return {"id":self.id,"Description": self.description,"Created at": self.created_at,"Status": self.status,"Updated at": self.updated_at}


print(datetime.now())

manager = TaskManager()
manager.add_task("Hello")
manager.add_task("Merhaba")
manager.add_task("Merhaba Dünya")
manager.add_task("AS")
print(manager.tasks[0].description)

print(manager.tasks[0].status)
manager.update_task(1, "Selamın Aleyküm")

print(manager.tasks[0].description)
print(manager.list())
print(manager.mark_in_progress(1))
print(manager.list("in progress"))
print("----------------")
print(manager.list("todo"))
print("----------------")
print(manager.list())
print(manager.mark_done(2))
print(manager.list())
print(manager.remove_task(2))
print(manager.remove_task(3))
print(manager.remove_task(4))
print(manager.list())
