# src/cleaner.py

import pandas as pd
import os


def remove_duplicates(df):
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    print(f"  Duplicates removed: {before - after}")
    print(f"  Rows before: {before}, Rows after: {after}")
    return df


def handle_missing_values(df):
    print("  Handling missing values...")
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].fillna("Unknown")
        elif df[column].dtype in ["float64", "int64"]:
            if df[column].nunique() == len(df[column].dropna()):
                existing = set(df[column].dropna().astype(int))
                max_val = int(df[column].max())
                full_sequence = set(range(1, max_val + 2))
                missing_numbers = sorted(full_sequence - existing)
                missing_index = 0
                for i in df[column][df[column].isna()].index:
                    df.at[i, column] = missing_numbers[missing_index]
                    missing_index += 1

                print(f"    {column} looks like ID column, filled missing numbers in sequence")
            else:
                mean_val = round(df[column].mean(), 1)
                df[column] = df[column].fillna(mean_val)
        else:
            df[column] = df[column].fillna("Unknown")
    print("  Missing values handled!")
    return df


def clean_data(df):
    print("  Cleaning and standardizing data...")
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].str.strip()
            df[column] = df[column].str.title()
        elif df[column].dtype == "float64":
            df[column] = df[column].round(1)
            try:
                if df[column].apply(float.is_integer).all():
                    df[column] = df[column].astype(int)
            except:
                pass
    df = df.reset_index(drop=True)
    print("  Data cleaned successfully!")
    return df


def export_clean_data(df, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_excel(output_path, index=False)
    print(f"  Cleaned data saved: {output_path}")