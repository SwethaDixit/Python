import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.configure(background="#f0f0f0")  

        self.todo_list = []

        self.task_number_label = tk.Label(root, text="Task Number:", font=("Arial", 12), fg="#00698f")  
        self.task_number_label.pack(padx=10, pady=10)

        self.task_number_entry = tk.Entry(root, width=40, font=("Arial", 12))  
        self.task_number_entry.pack(padx=10, pady=10)

        self.task_label = tk.Label(root, text="Task:", font=("Arial", 12), fg="#00698f")  
        self.task_label.pack(padx=10, pady=10)

        self.task_entry = tk.Entry(root, width=40, font=("Arial", 12))  
        self.task_entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, font=("Arial", 12), bg="#007bff", fg="white")  # Set font, color, and background
        self.add_button.pack(padx=10, pady=10)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task, font=("Arial", 12), bg="#007bff", fg="white")  # Set font, color, and background
        self.update_button.pack(padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, font=("Arial", 12), bg="#007bff", fg="white")  # Set font, color, and background
        self.delete_button.pack(padx=10, pady=10)

        self.view_button = tk.Button(root, text="View Tasks", command=self.view_tasks, font=("Arial", 12), bg="#007bff", fg="white")  # Set font, color, and background
        self.view_button.pack(padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=40, font=("Arial", 12))  
        self.task_listbox.pack(padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Task added successfully!")
        else:
            messagebox.showerror("Error", "Please enter a task.")

    def update_task(self):
        task_number = self.task_number_entry.get()
        new_task = self.task_entry.get()
        if task_number and new_task:
            try:
                task_number = int(task_number)
                if 1 <= task_number <= len(self.todo_list):
                    self.todo_list[task_number - 1] = new_task
                    self.task_listbox.delete(task_number - 1)
                    self.task_listbox.insert(task_number - 1, new_task)
                    self.task_number_entry.delete(0, tk.END)
                    self.task_entry.delete(0, tk.END)
                    messagebox.showinfo("Success", "Task updated successfully!")
                else:
                    messagebox.showerror("Error", "Invalid task number.")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter a number.")
        else:
            messagebox.showerror("Error", "Please enter a task number and a new task.")

    def delete_task(self):
        task_number = self.task_number_entry.get()
        if task_number:
            try:
                task_number = int(task_number)
                if 1 <= task_number <= len(self.todo_list):
                    del self.todo_list[task_number - 1]
                    self.task_listbox.delete(task_number - 1)
                    self.task_number_entry.delete(0, tk.END)
                    messagebox.showinfo("Success", "Task deleted successfully!")
                else:
                    messagebox.showerror("Error", "Invalid task number.")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter a number.")
        else:
            messagebox.showerror("Error", "Please enter a task number.")

    def view_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list:
            self.task_listbox.insert(tk.END, task)

root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()