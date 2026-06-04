
import pandas as pd


def load_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        print(f"  File loaded successfully!")
        print(f"  Rows: {df.shape[0]}, Columns: {df.shape[1]}")
        return df
    except FileNotFoundError:
        print(f"  Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"  Something went wrong: {e}")
        return None