# Court Data Fetcher (Dummy Version)

This is a simple Flask-based web app created for Codveda Internship Task.  
Users can enter court case details (case type, number, year) and see dummy results.

---

## Features
- Input: Case Type, Case Number, Filing Year
- Output: Dummy result (party name, hearing date, PDF link)
- SQLite used to log query data
- Simple Flask app with HTML template

---

## Run Instructions
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py
