# Import pathlib
from pathlib import Path
import csvptyet

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filterspy
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

def test_save_csv():
    # @TODO: Your code here!co
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
    csvpath = Path('C:\Users\17049\Desktop\homework\module2\Starter_Code\qualifier\data\qualifying_loans.csv')
    op = test_filters()
    with open(csvpath,'w', newline='') as f:
                writer = csv.writer(f, delimiter = ',')
                for data in op:
                     writer.writerow(data)

    return csvpath

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = fileio.load_csv(Path('C:\\Users\\17049\\Desktop\\homework\\module2\\Starter_Code\\qualifier\\data\\daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    # @TODO: Test the new save_csv code!
    # YOUR CODE HERE!
    # Run qualification filters



    bank_data_filtered = max_loan_size.filter_max_loan_size(loan, bank_data)
    bank_data_filtered = credit_score.filter_credit_score(current_credit_score, bank_data_filtered)
    bank_data_filtered = debt_to_income.filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = loan_to_value.filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    len_bank_fil = len(bank_data_filtered)
    print(len(bank_data_filtered))
    assert len(bank_data_filtered) == 6

    return bank_data_filtered
