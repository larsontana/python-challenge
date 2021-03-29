# Import libraries and dependencies. 
import os
import csv

# Join file paths. 
Budget_Data = os.path.join('Resources', 'budget_data.csv')
print(Budget_Data)

with open(Budget_Data) as csv_file:
    csv_Reader = csv.reader(csv_file, delimiter=",")
    csv_Header = next(csv_file)
    print(f"Header: {csv_Header}")

# Creating empty list to store the value.
    Profit = []
    Total_Months = []
    AverageChange = []

    for rows in csv_Reader:
        Total_Months.append(rows[0])
        Profit.append(int(rows[1]))

    # Iterate through the lists. 
    for i in range(len(Profit)-1):
        AverageChange.append(Profit[i+1]-Profit[i])


Total_Profits = sum(Profit)
TotalMonths = len(Total_Months)
Average_Profit_Change = sum(AverageChange) / len(AverageChange)
Max_Increase_Value = max(AverageChange)
Max_Decrease_Value = min(AverageChange)


# Print output. 
print(TotalMonths)
print(Total_Profits)
print(Average_Profit_Change)
print(Max_Increase_Value)
print(Max_Decrease_Value)

# Print output. 

print("Financial Analysis")

print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*---*--*-*-')

print('Total Months : ' + str(TotalMonths))
print("Total: " + "$" + str(sum(Profit)))
print('Average Change: ' + '$' + str(round(Average_Profit_Change, 2)))
print("Greatest Increase in Profits: " + str(Total_Months[AverageChange.index(
    max(AverageChange))+1]) + " " + "$" + str(Max_Increase_Value))
print("Greatest Decrease in Profits: " + str(Total_Months[AverageChange.index(
    min(AverageChange))+1]) + " " + "$" + str(Max_Decrease_Value))


# output to a text file
output = open("Analysis/Py_Bank_Output.txt", "w")
output.write("Financial Analysis" + "\n")
output.write('Total Months : ' + str(TotalMonths) + "\n")
output.write("Total: " + "$" + str(sum(Profit)) + "\n")
output.write('Average Change: ' + '$' +
             str(round(Average_Profit_Change, 2)) + "\n")
output.write("Greatest Increase in Profits: " + str(Total_Months[AverageChange.index(
    max(AverageChange))+1]) + " " + "$" + str(Max_Increase_Value) + "\n")
output.write("Greatest Decrease in Profits: " + str(Total_Months[AverageChange.index(
    min(AverageChange))+1]) + " " + "$" + str(Max_Decrease_Value))

output.close()