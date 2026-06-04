import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, render_template, request, send_file
from src.reader import load_excel
from src.analyzer import explore_data_dict, generate_statistics_dict
from src.cleaner import remove_duplicates, handle_missing_values, clean_data, export_clean_data
from src.visualizer import create_charts

app = Flask(__name__)

UPLOAD_FOLDER = "data/raw"
PROCESSED_FOLDER = "data/processed"
REPORTS_FOLDER = "reports"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)
os.makedirs(REPORTS_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():

    if "file" not in request.files:
        return render_template("index.html", error="No file uploaded!")

    file = request.files["file"]

    if file.filename == "":
        return render_template("index.html", error="No file selected!")

    if not file.filename.endswith(".xlsx"):
        return render_template("index.html", error="Please upload an Excel (.xlsx) file only!")


    file_name = os.path.splitext(file.filename)[0]
    save_path = f"{UPLOAD_FOLDER}/{file.filename}"
    file.save(save_path)

    df = load_excel(save_path)
    if df is None:
        return render_template("index.html", error="Could not read the file!")


    raw_info = explore_data_dict(df)


    df = remove_duplicates(df)
    df = handle_missing_values(df)
    df = clean_data(df)


    stats = generate_statistics_dict(df)


    chart_folder = f"{REPORTS_FOLDER}/{file_name}"
    create_charts(df, chart_folder)


    cleaned_path = f"{PROCESSED_FOLDER}/{file_name}_cleaned.xlsx"
    export_clean_data(df, cleaned_path)


    charts = []
    if os.path.exists(chart_folder):
        charts = [f for f in os.listdir(chart_folder) if f.endswith(".png")]


    table_html = df.to_html(classes="data-table", index=False)

    return render_template(
        "results.html",
        table=table_html,
        raw_info=raw_info,
        stats=stats,
        charts=charts,
        chart_folder=file_name,
        cleaned_file=f"{file_name}_cleaned.xlsx"
    )


@app.route("/download/<filename>")
def download(filename):
    path = f"{PROCESSED_FOLDER}/{filename}"
    return send_file(path, as_attachment=True)


@app.route("/charts/<folder>/<filename>")
def get_chart(folder, filename):
    path = f"{REPORTS_FOLDER}/{folder}/{filename}"
    return send_file(path, mimetype="image/png")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)