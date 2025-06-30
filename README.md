# OIBSIP_PythonProg_Task-2

# Advanced BMI Calculator (Python + Tkinter)

A Body Mass Index (BMI) calculator built with Python and Tkinter. This application enables users to calculate BMI, view historical data, and visualize BMI trends — all within an easy-to-use interface.

# Objective

To design and develop a user-friendly desktop application that:
-> Calculates BMI based on user input
-> Categorizes BMI into standard health classes
-> Stores data for multiple users
-> Displays historical BMI records
-> Visualizes trends through interactive charts

# Tools & Technologies Used

Tool/Library and their purpose 

1.Python -> Core programming language
2.Tkinter -> GUI development
3.Pandas -> Data storage & handling
4.Matplotlib -> Data visualization as graphs
5.Git & GitHub -> Version control & sharing

# Project Structure & Code Overview

# `main.py`
-> Main GUI file using **Tkinter**.
-> Handles user input, button clicks, and displays results.
-> Calls other modules to validate input, calculate BMI, save data, show history and graph.

# `utils/calculator.py`
--> Contains logic to:
  -> Validate weight and height.
  -> Calculate BMI using the formula.
  -> Categorize BMI (Underweight, Normal, Overweight, Obese).

# `utils/database.py`
-> Manages the `data.csv` file.
-> Saves each BMI record with timestamp.
-> Loads user-specific history for viewing or graphing.

# `utils/graph.py`
-> Uses **matplotlib** to generate a **BMI over time graph**.
-> Pulls user data and plots BMI values by date.

# `assets/data.csv`
-> Stores all user records: name, weight, height, BMI, category, and date.
-> Created automatically if it doesn’t exist.

# `.gitignore`
-> Prevents sensitive or auto-generated files (like `data.csv`) from being pushed to GitHub.

# `requirements.txt`
txt
pandas
matplotlib
tk


# How to Run

# 1. Clone the repository
```bash
git clone https://github.com/your-username/advanced-bmi-calculator.git
cd advanced-bmi-calculator
