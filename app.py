from flask import Flask, render_template, request
from algorithm import load_data, process_input

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    loan_amnt_str = request.form.get('loan_amnt')
    selected_interest_str = request.form.get('selected_interest')
    year_str = request.form.get('year')
    turnover_str = request.form.get('turnover')
    family_inc_str = request.form.get('family_inc')

    if loan_amnt_str is None or selected_interest_str is None or year_str is None or turnover_str is None or family_inc_str is None:
        return "Error: Form inputs cannot be empty."

    try:
        loan_amnt = float(loan_amnt_str)
        selected_interest = float(selected_interest_str)
        year = int(year_str)
        turnover = float(turnover_str)
        family_inc = float(family_inc_str)
    except ValueError:
        return "Error: Invalid input format."

    # Load data and process input
    df = load_data()
    results_df = process_input(loan_amnt, selected_interest, year, turnover, family_inc)

    return render_template('results.html', results=results_df.to_html())

if __name__ == '__main__':
    app.run(debug=True)
