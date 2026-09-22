import pandas as pd
import os

def load_data():
    file_path = "students.csv"

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Could not find {file_path}. Please check the file is in this folder.")

    df = pd.read_csv(file_path)
    return df