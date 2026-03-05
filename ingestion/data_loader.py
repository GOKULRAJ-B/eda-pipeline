import pandas as pd
import os

def load_dataset(file_path):

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".csv":
        df = pd.read_csv(file_path)

    elif ext in [".xls", ".xlsx"]:
        df = pd.read_excel(file_path)

    elif ext == ".json":
        df = pd.read_json(file_path)

    else:
        raise ValueError("Unsupported file format")

    print("Dataset Loaded Successfully")
    return df