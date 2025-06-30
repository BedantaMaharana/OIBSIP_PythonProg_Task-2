import tkinter as tk
from tkinter import messagebox
from utils.calculator import validate_input, calculate_bmi, categorize_bmi
from utils.database import save_data, load_user_data
from utils.graph import show_graph
import os

DATA_FILE = "assets/data.csv"

def show_result():
    name = name_entry.get().strip()
    weight = weight_entry.get().strip()
    height = height_entry.get().strip()

    if not name or not weight or not height:
        messagebox.showerror("Input Error", "All fields are required.")
        return

    weight, height = validate_input(weight, height)
    if weight is None or height is None:
        messagebox.showerror("Validation Error", "Enter valid weight (10–300kg) and height (0.5–2.5m).")
        return

    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)
    result_label.config(text=f"Your BMI is {bmi} ({category})")
    save_data(name, weight, height, bmi, category, DATA_FILE)

def show_history():
    name = name_entry.get().strip()
    if not name:
        messagebox.showinfo("History", "Please enter your name to view history.")
        return

    user_data = load_user_data(name, DATA_FILE)
    if user_data.empty:
        messagebox.showinfo("History", "No history found for this user.")
        return

    history_text = "\n".join(
        f"{row.Date[:16]} → BMI: {row.BMI} ({row.Category})"
        for row in user_data.itertuples()
    )
    messagebox.showinfo(f"{name}'s History", history_text)

def view_graph():
    name = name_entry.get().strip()
    show_graph(name, DATA_FILE)

# GUI Setup
app = tk.Tk()
app.title("Advanced BMI Calculator")
app.geometry("400x430")
app.configure(bg="#f2f2f2")
app.resizable(False, False)

tk.Label(app, text="BMI Calculator", font=("Helvetica", 18, "bold"), bg="#f2f2f2", fg="#333").pack(pady=15)

form_frame = tk.Frame(app, bg="#f2f2f2")
form_frame.pack(pady=5)

tk.Label(form_frame, text="Name:", font=("Arial", 12), bg="#f2f2f2").grid(row=0, column=0, sticky='w')
name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Weight (kg):", font=("Arial", 12), bg="#f2f2f2").grid(row=1, column=0, sticky='w')
weight_entry = tk.Entry(form_frame, width=30)
weight_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Height (m):", font=("Arial", 12), bg="#f2f2f2").grid(row=2, column=0, sticky='w')
height_entry = tk.Entry(form_frame, width=30)
height_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Button(app, text="Calculate BMI", command=show_result, bg="#007acc", fg="white", font=("Arial", 12), width=20).pack(pady=15)

result_label = tk.Label(app, text="", font=("Arial", 12), bg="#f2f2f2", fg="green")
result_label.pack()

tk.Button(app, text="View History", command=show_history, bg="#6a737d", fg="white", font=("Arial", 11), width=20).pack(pady=5)
tk.Button(app, text="Show BMI Graph", command=view_graph, bg="#6a737d", fg="white", font=("Arial", 11), width=20).pack(pady=5)

tk.Label(app, text="© 2025 Your Name", font=("Arial", 8), bg="#f2f2f2", fg="gray").pack(side="bottom", pady=10)

app.mainloop()
