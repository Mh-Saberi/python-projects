from src.todolist import ToDoList
from src.task import Task

def main():
    my_todo = ToDoList("data/tasks.csv")


    while True:
        print("📝 managing ToDo lists :")
        print("1. ➕ add a new task :")
        print("2. ❌ remove a task")
        print("3. 📋 show my ToDo list")
        print("4. 🚪 Exit")

        try:
            choice = int(input("your choice : "))
        except Exception as e:
            print(f"We encountered the following error: {e}⚠️")
            continue
        
        match choice:
            case 1:
                name = input("name of the task? :")
                description = input("any descriptions? :")
                priority = input("priority : (high / mid / low): ")
                my_todo.add_task(Task(name, description, priority))
                print("task added successfully✅")

            case 2:
                try:
                    index = int(input("what's the index of task you want to remove?  "))
                    if my_todo.delete_task(index):
                        print("task removed successfully✅")
                    else:
                        print("invalid index!")
                except Exception as e:
                    print(f"We encountered the following error: {e}⚠️")

            case 3:
                my_todo.show_tasks()

            case 4:
                print("bye! Have a productive day🌸")
                break

            case _ :
                print("invalid input!")   
                continue         

if __name__ == "__main__":
    main()