from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        filing_year = request.form['filing_year']

        # Dummy data
        result = {
            "party_name": "RAMANAND vs GENERAL PUBLIC",
            "next_hearing": "10-Aug-2025",
            "pdf_link": "https://example.com/fake-judgment.pdf"
        }

        # Save query log (optional)
        conn = sqlite3.connect('queries.db')
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS queries (case_type TEXT, case_number TEXT, filing_year TEXT)')
        cur.execute('INSERT INTO queries VALUES (?, ?, ?)', (case_type, case_number, filing_year))
        conn.commit()
        conn.close()

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
