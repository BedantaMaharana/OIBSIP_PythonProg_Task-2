import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox
import os
def show_graph(name, file_path):
    if not name:
        messagebox.showinfo("Graph", "Please enter your name to view graph.")
        return

    if not os.path.exists(file_path):
        messagebox.showinfo("Graph", "No data file found.")
        return

    df = pd.read_csv(file_path)
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
