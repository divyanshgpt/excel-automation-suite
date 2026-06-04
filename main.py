import time
import os
from src.reader import load_excel
from src.analyzer import explore_data, generate_statistics, export_report
from src.cleaner import remove_duplicates, handle_missing_values, clean_data, export_clean_data
from src.visualizer import create_charts


def main():
    print("\n" + "=" * 50)
    print("   EXCEL AUTOMATION SUITE")
    print("   Automate. Clean. Analyze. Visualize.")
    print("=" * 50)

   
    print("\nEnter the full path to your Excel file:")
    print("Example: D:\\excel_automation_suite\\data\\raw\\employees.xlsx")
    file_path = input("\nFile path: ").strip()

    
    if not os.path.exists(file_path):
        print(f"\nError: File not found at {file_path}")
        print("Please check the path and try again.")
        return

    
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    output_folder = f"reports/{file_name}"
    cleaned_path = f"data/processed/{file_name}_cleaned.xlsx"
    report_path = f"{output_folder}/summary_report.txt"

    start_time = time.time()

    
    print("\n[STEP 1] Loading file...")
    df = load_excel(file_path)
    if df is None:
        return

    
    print("\n[STEP 2] Exploring data...")
    explore_data(df)

    
    print("\n[STEP 3] Cleaning data...")
    df = remove_duplicates(df)
    df = handle_missing_values(df)
    df = clean_data(df)

    
    print("\n[STEP 4] Analyzing data...")
    generate_statistics(df)

    
    print("\n[STEP 5] Creating charts...")
    create_charts(df, output_folder)

    
    print("\n[STEP 6] Exporting results...")
    export_report(df, report_path)
    export_clean_data(df, cleaned_path)

    
    duration = round(time.time() - start_time, 2)

    print("\n" + "=" * 50)
    print("   ALL TASKS COMPLETED SUCCESSFULLY!")
    print(f"   Time taken: {duration} seconds")
    print("=" * 50)
    print(f"\n  Outputs saved in: {output_folder}/")
    print(f"  Cleaned file    : {cleaned_path}")


if __name__ == "__main__":
    main()