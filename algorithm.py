import pandas as pd

def load_data():
    # Load CSV data into DataFrame
    df = pd.read_csv('/Users/yashgupta/Downloads/sahyog 3.csv')
    return df

def process_input(loan_amnt, selected_interest, year, turnover, family_inc):
    # Load data
    df = load_data()

    # Your algorithm logic here
    # Example filter based on input values
    results_df = df[(df['Maximum Loan Amount'] >= loan_amnt) & 
                     (df["min.Interest rate"] <= selected_interest) &
                     (df['minimum Business turnover'] <= turnover) &
                     (df['Minimal Annual Income'] <= family_inc) &
                     (df['minimum years in current business']<= year)]

    return results_df
