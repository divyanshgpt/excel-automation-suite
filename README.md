# ⚡ Excel Automation Suite

A professional Python web application that automatically cleans,
analyzes and visualizes any Excel file in seconds.

## 🌟 Features
- Reads any Excel file automatically
- Removes duplicate records
- Handles missing values intelligently
- Detects and preserves ID columns
- Cleans and standardizes data formatting
- Generates summary statistics
- Creates professional charts and visualizations
- Exports cleaned Excel file
- Beautiful web interface built with Flask

## 🛠️ Technologies Used
- Python 3
- Flask (Web Framework)
- Pandas (Data Processing)
- OpenPyXL (Excel Handling)
- Matplotlib (Charts)
- HTML & CSS (Frontend)

## 🚀 How To Run

### Install dependencies
pip install -r requirements.txt

### Run the web app
python app.py

### Or run via terminal only
python main.py

### Open in browser
http://127.0.0.1:5000

## 📁 Project Structure
excel_automation_suite/
├── src/
│   ├── reader.py        # Excel file reader
│   ├── cleaner.py       # Data cleaning
│   ├── analyzer.py      # Statistics
│   └── visualizer.py    # Charts
├── templates/
│   ├── index.html       # Upload page
│   └── results.html     # Results page
├── static/
│   └── style.css        # Styling
├── app.py               # Flask web app
├── main.py              # Terminal runner
└── requirements.txt     # Dependencies

## 👨‍💻 Author
Divyansh
