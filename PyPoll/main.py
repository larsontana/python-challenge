# Import depencies and libraries. 
import os
import csv

# Join file paths. 
Election_Data = os.path.join("Resources", "election_data.csv")

# Declare variables. 
Total_Votes = 0
Khan_Votes = 0
Correy_Votes = 0
Li_Votes = 0
Otooley_Votes = 0

with open(Election_Data) as csv_file:
    csv_Reader = csv.reader(csv_file, delimiter=",")
    csv_Header = next(csv_Reader)
    print(f'Header : {csv_Header}')

# Add total votes. 
    for row in csv_Reader:
        Total_Votes += 1

        # Checking if the names exist. 
        if row[2] == "Khan":
            Khan_Votes += 1
        elif row[2] == "Correy":
            Correy_Votes += 1
        elif row[2] == "Li":
            Li_Votes += 1
        elif row[2] == "O'Tooley":
            Otooley_Votes += 1

# Define candidates. 
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [Khan_Votes, Correy_Votes, Li_Votes, Otooley_Votes]

# Add the list to the map. 
add_pair = zip(candidates, votes)

# Store values. 
Key_value_pair = dict(add_pair)
Max_value = max(Key_value_pair, key=Key_value_pair.get)

# Percent values.
Khan_Percent = round((Khan_Votes/Total_Votes) * 100, 2)
Correy_Percent = round((Correy_Votes/Total_Votes)*100, 2)
Li_Percent = round((Li_Votes/Total_Votes) * 100, 2)
Otooley_Percent = round((Otooley_Votes/Total_Votes) * 100, 2)

# Print output. 

print("Election Results")
print("*-*-*-*-*-*-*--**-*-*-**-*-*-*-*")
print(f"Total votes :  {Total_Votes}")
print("*-*-*-*-*-*-*--**-*-*-**-*-*-*-*")
print(f'Khan:{Khan_Percent: .3f} ({Khan_Votes})')
print(f'Correy: {Correy_Percent: .3f} ({Correy_Votes})')
print(f'Li: {Li_Percent: .3f} ({Li_Votes}) ')
print(f"O'Tooley: {Otooley_Percent: .3f} ({Otooley_Votes})")

print("*-*-*-*-*-*-*--**-*-*-**-*-*-*-*")
print(f"Winner : {Max_value}")

# Output to a text.

output = open("Analysis/Py_Poll.txt", "w")
output.write("Election Results" + "\n")
output.write(f"Total votes :  {Total_Votes}  \n")
output.write("*-*-*-*-*-*-*--**-*-*-**-*-*-*-* \n")
output.write(f'Khan:{Khan_Percent: .3f} ({Khan_Votes}) \n')
output.write(f'Correy: {Correy_Percent: .3f} ({Correy_Votes}) \n')
output.write(f'Li: {Li_Percent: .3f} ({Li_Votes}) \n')
output.write(f"O'Tooley: {Otooley_Percent: .3f} ({Otooley_Votes}) \n")
output.write("*-*-*-*-*-*-*--**-*-*-**-*-*-*-* \n")
output.write(f"Winner : {Max_value}")


output.close()