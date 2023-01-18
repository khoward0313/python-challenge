
# import dependencies
import os 
import csv

# create path to CSV file
budget_csv = os.path.join ("Resources","budget_data.csv")
budget_csv

# create variables
total_months = 0
total = 0

# open the file
with open(budget_csv) as csv_file:
    csv_reader=csv.reader(csv_file)

    # read the header
    header =  next(csv_reader)

    # get data from first row 
    first_row = next(csv_reader)

    # increase total months by 1
    total_months += 1

    total += int(first_row[1])

    for row in csv_reader:
        total_months += 1
        total += int(row[1])

print(total)

