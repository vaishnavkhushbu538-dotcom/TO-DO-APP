
import tkinter as tk
from tkinter import messagebox

tasks = []

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        task = tasks.pop(selected)
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

app = tk.Tk()
app.title("Modern To-Do App")
app.geometry("400x500")
app.config(bg="#1e1e2f")

frame = tk.Frame(app, bg="#1e1e2f")
frame.pack(pady=20)

title = tk.Label(frame, text="TO-DO LIST", font=("Arial", 18, "bold"), bg="#1e1e2f", fg="white")
title.pack()

entry = tk.Entry(frame, width=25, font=("Arial", 14))
entry.pack(pady=10)

btn_frame = tk.Frame(frame, bg="#1e1e2f")
btn_frame.pack()

add_btn = tk.Button(btn_frame, text="Add", width=10, command=add_task, bg="#4CAF50", fg="white")
add_btn.grid(row=0, column=0, padx=5)

del_btn = tk.Button(btn_frame, text="Delete", width=10, command=delete_task, bg="#f44336", fg="white")
del_btn.grid(row=0, column=1, padx=5)

listbox = tk.Listbox(app, width=35, height=15, font=("Arial", 12))
listbox.pack(pady=20)

app.mainloop()
