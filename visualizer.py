
import matplotlib.pyplot as plt
import os


def create_charts(df, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    text_cols = df.select_dtypes(include=["object"]).columns

    chart_count = 0

    
    for num_col in numeric_cols:
       
        for text_col in text_cols:
            if df[text_col].nunique() <= 10:
                grouped = df.groupby(text_col)[num_col].mean()

                plt.figure(figsize=(8, 5))
                plt.bar(grouped.index, grouped.values, color="steelblue")
                plt.title(f"Average {num_col} by {text_col}")
                plt.xlabel(text_col)
                plt.ylabel(f"Average {num_col}")
                plt.xticks(rotation=45)
                plt.tight_layout()

                filename = f"{num_col}_by_{text_col}.png".lower().replace(" ", "_")
                plt.savefig(f"{output_folder}/{filename}")
                plt.close()
                chart_count += 1
                print(f"  Chart saved: {filename}")

   
    for text_col in text_cols:
        if 2 <= df[text_col].nunique() <= 8:
            counts = df[text_col].value_counts()

            plt.figure(figsize=(7, 7))
            plt.pie(counts.values, labels=counts.index, autopct="%1.1f%%")
            plt.title(f"Distribution of {text_col}")
            plt.tight_layout()

            filename = f"distribution_{text_col}.png".lower().replace(" ", "_")
            plt.savefig(f"{output_folder}/{filename}")
            plt.close()
            chart_count += 1
            print(f"  Chart saved: {filename}")

    print(f"  Total charts created: {chart_count}")