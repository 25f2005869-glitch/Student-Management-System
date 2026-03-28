# ============================================
# Student Management System (GUI)
# Author: Saloni Tiwari
# Topic: Tkinter + File Handling
# ============================================

import tkinter as tk
from tkinter import messagebox

# ========================================
# Helper Functions
# ========================================
def load_students():
    try:
        with open("students.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_students():
    with open("students.txt", "w") as file:
        for s in students:
            file.write(s + "\n")

def normalize(name):
    return name.strip().lower()


# ========================================
# Functions (Operations)
# ========================================
def add_student():
    name = entry.get().strip()

    if not name:
        messagebox.showerror("Error", "Name cannot be empty!")
        return

    if normalize(name) in [normalize(s) for s in students]:
        messagebox.showwarning("Warning", "Student already exists!")
        return

    students.append(name)
    save_students()
    entry.delete(0, tk.END)
    view_students()
    messagebox.showinfo("Success", "Student added!")


def view_students():
    listbox.delete(0, tk.END)
    for s in students:
        listbox.insert(tk.END, s)


def search_student():
    name = entry.get().strip()

    if normalize(name) in [normalize(s) for s in students]:
        messagebox.showinfo("Result", "Student found!")
    else:
        messagebox.showerror("Result", "Student not found!")


def delete_student():
    name = entry.get().strip()

    for s in students:
        if normalize(s) == normalize(name):
            students.remove(s)
            save_students()
            view_students()
            messagebox.showinfo("Success", "Student deleted!")
            return

    messagebox.showerror("Error", "Student not found!")


# ========================================
# GUI Setup
# ========================================
students = load_students()

root = tk.Tk()
root.title("Student Management System")
root.geometry("400x450")

tk.Label(root, text="Student Management System", font=("Arial", 14, "bold")).pack(pady=10)

# Entry
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Buttons
tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="View Students", command=view_students).pack(pady=5)
tk.Button(root, text="Search Student", command=search_student).pack(pady=5)
tk.Button(root, text="Delete Student", command=delete_student).pack(pady=5)

# Listbox
frame = tk.Frame(root)
frame.pack(pady=10)

scroll = tk.Scrollbar(frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, width=40, height=10, yscrollcommand=scroll.set)
listbox.pack()

scroll.config(command=listbox.yview)

# Load initial data
view_students()

# Run
root.mainloop()