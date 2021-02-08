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

# Associate costs with the month. 

max_increase_month = profit_change.index(max(profit_change)) + 1
min_decrease_month = profit_change.index(min(profit_change)) + 1

# Print data. 

print("Financial Analysis:")
print(f"All Months: {len(all_months)}")
print(f"All Profit: ${sum(all_profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Max Increase: {all_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Max Decrease: {all_months[min_increase_month)} (${str(min_increase_value))})")

# STEP 4: Output file data as txt file. 

output_file = Path("python-challenge", "PyBank", "Financial_Analysis_Summary.txt")
with open(output_file,"w") as file

# Write into the file.Note that "\n" inputs space. 

file.write("Financial Analysis:")
file.write("\n")
file.write(f"All Months: {len(all_months)}")
file.write("\n")
file.write(f"All Profit: ${sum(all_profit)}")
file.write("\n")
file.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
file.write("\n")
file.write(f"Max Increase: {all_months[max_increase_month]} (${(str(max_increase_value))})")
file.write("\n")
file.write(f"Max Decrease: {all_months[min_increase_month)} (${str(min_increase_value))})")
