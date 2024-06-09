
'''
------------------------------------------------------
# using tkinter to create a simple User interface
'''
import json
import tkinter as tk
from tkinter import messagebox, simpledialog

# Task management logic
def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    else:
        messagebox.showerror("Error", "Invalid task number")

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Tkinter UI
class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.tasks = load_tasks()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=15)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.task_listbox.bind('<Delete>', self.delete_task_event)
        self.update_task_listbox()

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task_dialog)
        self.add_button.pack(pady=5)

    def add_task_dialog(self):
        task_name = simpledialog.askstring("Task Name", "Enter task name:")
        if task_name:
            task_desc = simpledialog.askstring("Task Description", "Enter task description:")
            task_due_date = simpledialog.askstring("Due Date", "Enter due date (YYYY-MM-DD):")
            task_priority = simpledialog.askstring("Priority", "Enter task priority (low, medium, high):")

            task = {
                "name": task_name,
                "description": task_desc,
                "due_date": task_due_date,
                "priority": task_priority
            }
            add_task(self.tasks, task)
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks):
            task_display = f"{idx + 1}. {task['name']} (Due: {task['due_date']}, Priority: {task['priority']})"
            self.task_listbox.insert(tk.END, task_display)

    def delete_task_event(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            delete_task(self.tasks, index)
            self.update_task_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()


'''
------------------------------------------------------------------
immplementing the basic functions of the Task Management system
----------------------------------------------------------------------
'''

def add_task(tasks):
    task_name = input("Enter task name: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter task priority (low, medium, high): ")
    task = {
        "name": task_name,
        "description": description,
        "due_date": due_date,
        "priority": priority
    }
    tasks.append(task)

def view_tasks(tasks):
    for idx, task in enumerate(tasks):
        print(f"Task {idx + 1}:")
        print(f"  Name: {task['name']}")
        print(f"  Description: {task['description']}")
        print(f"  Due Date: {task['due_date']}")
        print(f"  Priority: {task['priority']}")
        print()

def update_task(tasks):
    task_id = int(input("Enter task number to update: ")) - 1
    if 0 <= task_id < len(tasks):
        task = tasks[task_id]
        task['name'] = input(f"Enter new name (current: {task['name']}): ") or task['name']
        task['description'] = input(f"Enter new description (current: {task['description']}): ") or task['description']
        task['due_date'] = input(f"Enter new due date (current: {task['due_date']}): ") or task['due_date']
        task['priority'] = input(f"Enter new priority (current: {task['priority']}): ") or task['priority']
    else:
        print("Invalid task number.")


def delete_task(tasks):
    task_id = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        print("Task deleted.")
    else:
        print("Invalid task number.")


import json

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def main():
    tasks = load_tasks()
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


