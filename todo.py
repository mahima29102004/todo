import tkinter as tk
from tkinter import messagebox

# Create window
app = tk.Tk()
app.title("To-Do List App")
app.geometry("400x400")

# List to store tasks
tasks = []

# Functions
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task")

# Entry box
entry = tk.Entry(app, width=30)
entry.pack(pady=10)

# Buttons
add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(app, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Listbox
listbox = tk.Listbox(app, width=40, height=10)
listbox.pack(pady=10)

# Run app
app.mainloop()