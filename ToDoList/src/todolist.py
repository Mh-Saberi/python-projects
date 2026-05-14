from .task import Task
from .file_manager import save_task_to_file, load_task_from_file
import os

class ToDoList :
    def __init__(self, file_name= None):
        if file_name is None:
            if not os.path.exists("data"):
                os.makedirs("data")
            file_name = os.path.join("data", "tasks.csv")
        
        self.file_name = file_name
        self.todo_tasks = load_task_from_file(file_name)

    def add_task(self, task):
        priority_map = {"high": 0, "mid": 1, "low": 2}
        self.todo_tasks.append(task)
        self.todo_tasks.sort(key=lambda t: priority_map.get(t.priority, 3))
        self.save()

    def delete_task(self, index):
        if 0 <= index < len(self.todo_tasks):
            del self.todo_tasks[index]
            self.save()
            return "the task deleted successfully.✅"
        
        return "Invalid index. couldn't delete the task.⚠️"
        
    def show_tasks(self):
        if not self.todo_tasks:
            print("ToDo list is empty")
        for i, task in enumerate(self.todo_tasks):
            print(f"{i}. {task}")

    def save(self):
        save_task_to_file(self.todo_tasks, self.file_name)