class Task :
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority

    def __str__(self):
        return (f"task name: {self.name}, "
                f"description: {self.description}, "
                f"priority: {self.priority}")
