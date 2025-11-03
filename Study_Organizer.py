import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import os

TASK_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            for task in f.read().splitlines():
                listbox.insert(tk.END, task)

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task():
    task = task_entry.get().strip()
    date = cal.get_date() if calendar_shown.get() else ""
    if task:
        if date:
            task = f"{task} (Due: {date})"
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task to delete.")
        return
    for index in reversed(selected):
        listbox.delete(index)
    save_tasks()

def show_calendar():
    if not calendar_shown.get():
        cal.pack(before=add_button, pady=(0,10))
        calendar_shown.set(True)
    else:
        cal.pack_forget()
        calendar_shown.set(False)

window = tk.Tk()
window.title("Study Organizer")
window.geometry("450x700")
window.config(bg="#212121")

tk.Label(window, text="Study Organizer", font=("Segoe UI", 18, "bold"), bg="#212121", fg="#249DC2").pack(pady=20)

task_entry = tk.Entry(window, width=40, font=("Segoe UI", 14, "bold"), bg="#333333", fg="#DCDCDC", insertbackground="white", relief="flat")
task_entry.pack(pady=10)

calendar_button = tk.Button(window, text="📅", font=("Segoe UI", 14, "bold"), bg="#373B38", fg="white", relief="flat", width=4, command=show_calendar)
calendar_button.pack(pady=5)

calendar_shown = tk.BooleanVar(value=False)
cal = Calendar(window, selectmode="day", date_pattern="yyyy-mm-dd", background="#2D2D2D", foreground="white", headersbackground="#212121", headersforeground="white", selectbackground="#249DC2")

add_button = tk.Button(window, text="Add Task", command=add_task, font=("Segoe UI", 14, "bold"), bg="#249DC2", fg="white", relief="flat", width=20)
add_button.pack(pady=10)

delete_button = tk.Button(window, text="Delete Task", command=delete_task, font=("Segoe UI", 14, "bold"), bg="#DA1616", fg="white", relief="flat", width=20)
delete_button.pack(pady=10)

listbox = tk.Listbox(window, width=50, height=15, font=("Segoe UI", 12, "bold"), bg="#2D2D2D", fg="#E4CC43", selectbackground="#5DDD63", selectmode=tk.MULTIPLE, relief="flat")
listbox.pack(pady=10)

load_tasks()
window.mainloop()
