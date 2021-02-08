# python-challenge

# STEP ONE: Set up dependencies, data, and libraries. 

import os, csv
from pathlib import Path

# Give the file location. 
input_file = Path("python-challenge", "PyBank", "budget_data.csv")

# Iterate through the data. 
all_months = []
all_profit = []
profit_change = []

# Open CSV.
with open(input_file,newline="", encoding="utf-8") as budget:

# Store the contents of budget data.
csvreader = csv.reader(budget,delimiter=",")

# Skip the header. 
header = next(csvreader)

# Iterate through the rows in the files and rhe months and profit to the correct lists. 
for row in csvreader: 
  all_months.append(row[0])
  all_profit.append(int(row[1]))
 
 # STEP 2: Find monthly profits. 
 
 # Iterate through profits to get the change in monthly profits. 
 for i in range(len(all_profit)-1):
   profit_change.append(all_profit[i+1]-all_profit[i])
   
# STEP 3: Get max and mins. 

max_increase_value = max(profit_change)
max_decrease_value = min(profit_change)
   
