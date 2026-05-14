
# 📝 To-Do List CLI (Python)

A To-Do List manager written in Python using Object-Oriented Programming (OOP), CSV file handling, and a simple text-based menu system.

---

## 📌 Features

- Add tasks with a name, description, and priority (High / Med / Low)
- Delete tasks by index
- View all tasks in a formatted list
- Automatically save tasks to `data/tasks.csv`
- Automatically load tasks from CSV file at program startup
- Modular and clean folder structure (OOP + File I/O)

---

## 📁 Project Structure

```
todo_project/
│
├── main.py # Program entry point
├── data/
│ └── tasks.csv # CSV file (auto-generated)
└── src/
├── init.py
├── task.py # Task class definition
├── file_manager.py # CSV read/write logic
└── todolist.py # ToDoList class (logic layer)
```

---

## 🚀 How to Run

1. Make sure Python **3.10 or above** is installed.
3. Open a terminal inside the project directory.
4. Run the program:

```bash
python main.py
```

⚙️ Requirements

No third-party libraries are required.
This project only uses Python standard libraries: csv, os.

👩‍💻 Developer

Created with ❤️ by Mahtab
