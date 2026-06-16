import csv
from .task import Task



file_name = "data/tasks.csv"

def save_task_to_file(tasks, file_name):
    with open(file_name, mode= 'w', newline= '', encoding='utf-8') as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow([task.name, task.description, task.priority])



def load_task_from_file(file_name):
    tasks = []
    try:
        with open(file_name, mode= 'r', newline= '', encoding= 'utf-8') as file:
            reader = csv.reader(file)
            for row in reader :
                if len(row) == 3:
                    name, description, priority = row
                    tasks.append(Task(name, description, priority))
    except FileNotFoundError:
        print("could'nt find the file")
    
    return tasks