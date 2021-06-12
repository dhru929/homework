# CSV Output Generation

This project sets out to produce all the eligible rates for a given loan in ine CSV output. This will run a given scenario through the rate sheet model and spit out all elgible lenders into one CSV.

---

## Technologies

We used python and a few modules to achieve this. Two biggest modules used were CSV and Path which help us write CSV and access certain spaces within our computer's drives.

---

## Installation Guide

First piece of business is to ask user where they would like to save the CSV and then if they want to save (just in case of overwrites)
if they respon yes, which confirm function returns a boolean, will write all of the eligible loans to a CSV file.
  # output_path = questionary.text("Enter a file path to where you want to save csv and name of csv(.csv):").ask()
  #  #output_path = Path(output_path)
  #  #confirm_qual_loans = questionary.confirm("Would you like to save qualifying loans? (Yes or No):").ask()
#
 #   if confirm_qual_loans == True:    
  #          with open(output_path,'w', newline='') as f:
   #             writer = csv.writer(f, delimiter = ',')
#            for data in qualifying_loans:
#                 writer.writerow(data)
# else: 
#    print('Ok - will not save')


---

## Examples

This section should include screenshots, code blocks, or animations showing how your project works.

---

## Usage
Below is an example of question, then answer. you will get to input your specific loan attributes into the generator.

? Enter a file path to a rate-sheet (.csv): C:\Users\17049\Desktop\homework\module2\Starter_Code\qualifier\data\daily_rate_sheet.csv
? What's your credit score? 850
? What's your total monthly income? 10500
? What's your desired loan amount? 400000
? What's your home value? 1000000
The monthly debt to income ratio is 0.38
Found 7 qualifying loans

---

## Contributors

Dhru Patel
Kowsi (TA) - helped fix some bugs in the code

---

## License

N/A