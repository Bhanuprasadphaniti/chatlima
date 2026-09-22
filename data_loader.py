import pandas as pd

def load_data():
    df = pd.read_csv("students.csv")
    return df