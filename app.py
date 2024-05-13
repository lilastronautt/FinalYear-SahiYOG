# from flask import Flask, render_template, request
# from algorithm import load_data, process_input

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit_form():
#     loan_amnt_str = request.form.get('loan_amnt')
#     selected_interest_str = request.form.get('selected_interest')
#     year_str = request.form.get('year')
#     turnover_str = request.form.get('turnover')
#     family_inc_str = request.form.get('family_inc')

#     if loan_amnt_str is None or selected_interest_str is None or year_str is None or turnover_str is None or family_inc_str is None:
#         return "Error: Form inputs cannot be empty."

#     try:
#         loan_amnt = float(loan_amnt_str)
#         selected_interest = float(selected_interest_str)
#         year = int(year_str)
#         turnover = float(turnover_str)
#         family_inc = float(family_inc_str)
#     except ValueError:
#         return "Error: Invalid input format."

#     # Load data and process input
#     df = load_data()
#     results_df = process_input(loan_amnt, selected_interest, year, turnover, family_inc)

#     return render_template('results.html', results=results_df.to_html())

# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=5000, debug=True)

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from algorithm import load_data, process_input

app = Flask(__name__, static_folder='/Users/yashgupta/SahiYOG-New/FinalYear-SahiYOG/static/css')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    middleName = db.Column(db.String(50))
    lastName = db.Column(db.String(50), nullable=False)
    contactNumber = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    businessName = db.Column(db.String(100))
    businessCategory = db.Column(db.String(20))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    firstName = request.form.get('firstName')
    middleName = request.form.get('middleName')
    lastName = request.form.get('lastName')
    contactNumber = request.form.get('contactNumber')
    email = request.form.get('email')
    age = request.form.get('age')
    gender = request.form.get('gender')
    businessName = request.form.get('businessName')
    businessCategory = request.form.get('businessCategory')

    new_user = User(firstName=firstName, middleName=middleName, lastName=lastName,
                    contactNumber=contactNumber, email=email, age=age, gender=gender,
                    businessName=businessName, businessCategory=businessCategory)
    db.session.add(new_user)
    db.session.commit()

    return "Form submitted successfully!"

@app.route('/loan-form', methods=['GET', 'POST'])
def submit_loan_form():
    if request.method == 'POST':
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
    else:
        return render_template('index.html')

if __name__ == '__main__':
    db.create_all()  # Creates the database tables based on your models
    app.run(debug=True)
