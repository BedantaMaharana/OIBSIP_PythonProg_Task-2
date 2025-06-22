import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# Constants
DATA_FILE = "data.csv"

# Create the CSV file if it doesn't exist
if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=["Name", "Weight", "Height", "BMI", "Category", "Date"]).to_csv(DATA_FILE, index=False)

# Utility Functions
def validate_input(weight, height):
    try:
        weight = float(weight)
        height = float(height)
        if 10 <= weight <= 300 and 0.5 <= height <= 2.5:
            return weight, height
        else:
            return None, None
    except:
        return None, None

def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def save_data(name, weight, height, bmi, category):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df = pd.read_csv(DATA_FILE)
    df.loc[len(df)] = [name, weight, height, bmi, category, date]
    df.to_csv(DATA_FILE, index=False)

def show_result():
    name = name_entry.get().strip()
    weight = weight_entry.get().strip()
    height = height_entry.get().strip()

    if not name or not weight or not height:
        messagebox.showerror("Input Error", "All fields are required.")
        return

    weight, height = validate_input(weight, height)
    if weight is None or height is None:
        messagebox.showerror("Validation Error", "Weight (10–300kg) and Height (0.5–2.5m) must be valid numbers.")
        return

    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)
    result_label.config(text=f"Your BMI is {bmi} ({category})")
    save_data(name, weight, height, bmi, category)

def show_history():
    df = pd.read_csv(DATA_FILE)
    name = name_entry.get().strip()
    if not name:
        messagebox.showinfo("History", "Please enter your name to view history.")
        return

    user_data = df[df['Name'].str.lower() == name.lower()]
    if user_data.empty:
        messagebox.showinfo("History", "No history found for this user.")
        return

    history_text = "\n".join(
        f"{row.Date[:16]} → BMI: {row.BMI} ({row.Category})"
        for row in user_data.itertuples()
    )
    messagebox.showinfo(f"{name}'s History", history_text)

def show_graph():
    df = pd.read_csv(DATA_FILE)
    name = name_entry.get().strip()
    if not name:
        messagebox.showinfo("Graph", "Please enter your name to view graph.")
        return

    user_data = df[df['Name'].str.lower() == name.lower()]
    if user_data.empty:
        messagebox.showinfo("Graph", "No data found for this user.")
        return

    user_data['Date'] = pd.to_datetime(user_data['Date'])
    user_data = user_data.sort_values('Date')

    plt.figure(figsize=(8, 4))
    plt.plot(user_data['Date'], user_data['BMI'], marker='o', color='royalblue', linestyle='-')
    plt.title(f"{name}'s BMI Over Time", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.xticks(rotation=30)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

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
tk.Button(app, text="Show BMI Graph", command=show_graph, bg="#6a737d", fg="white", font=("Arial", 11), width=20).pack(pady=5)

tk.Label(app, text="© 2025 Your Name", font=("Arial", 8), bg="#f2f2f2", fg="gray").pack(side="bottom", pady=10)

app.mainloop()
