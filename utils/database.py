import pandas as pd
import os
from datetime import datetime

def save_data(name, weight, height, bmi, category, file_path):
    folder = os.path.dirname(file_path)
    if not os.path.exists(folder):
        os.makedirs(folder)  # ✅ Automatically create the 'assets' folder

    if not os.path.exists(file_path):
        pd.DataFrame(columns=["Name", "Weight", "Height", "BMI", "Category", "Date"]).to_csv(file_path, index=False)

    df = pd.read_csv(file_path)
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df.loc[len(df)] = [name, weight, height, bmi, category, date]
    df.to_csv(file_path, index=False)

def load_user_data(name, file_path):
    if not os.path.exists(file_path):
        return pd.DataFrame()
    df = pd.read_csv(file_path)
    return df[df['Name'].str.lower() == name.lower()]
