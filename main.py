# Import necessary modules
import os, csv
from pathlib import Path 

# Define the file path using pathlib
data_file = Path("Resources","budget_data.csv")

# Initialize empty lists for processing data
months = []
profits = []
profit_changes = []
 
# Open the CSV file in read mode
with open(data_file, newline="", encoding="utf-8") as file:

    # Read the content of the CSV file
    csv_reader = csv.reader(file, delimiter=",") 

    # Skip the header row
    header = next(csv_reader)  

    # Loop through each row in the CSV file
    for row in csv_reader: 

        # Append month and profit data to their respective lists
        months.append(row[0])
        profits.append(int(row[1]))

    # Calculate monthly changes in profit
    for i in range(len(profits)-1):
        
        # Compute the change and add to the list
        profit_changes.append(profits[i+1] - profits[i])
        
# Determine the maximum and minimum profit changes
max_profit_increase = max(profit_changes)
max_profit_decrease = min(profit_changes)

# Find the corresponding months for max and min changes
max_profit_month = profit_changes.index(max_profit_increase) + 1
min_profit_month = profit_changes.index(max_profit_decrease) + 1 

# Print the financial analysis summary
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profits)}")
print(f"Average Change: ${round(sum(profit_changes)/len(profit_changes),2)}")
print(f"Greatest Increase in Profits: {months[max_profit_month]} (${(str(max_profit_increase))})")
print(f"Greatest Decrease in Profits: {months[min_profit_month]} (${(str(max_profit_decrease))})")

# Define the output file path
output_summary = Path("analysis","Summary.txt")

# Write the summary to the output file
with open(output_summary, "w") as summary_file:
    summary_file.write("Financial Analysis")
    summary_file.write("\n")
    summary_file.write("----------------------------")
    summary_file.write("\n")
    summary_file.write(f"Total Months: {len(months)}")
    summary_file.write("\n")
    summary_file.write(f"Total: ${sum(profits)}")
    summary_file.write("\n")
    summary_file.write(f"Average Change: ${round(sum(profit_changes)/len(profit_changes),2)}")
    summary_file.write("\n")
    summary_file.write(f"Greatest Increase in Profits: {months[max_profit_month]} (${(str(max_profit_increase))})")
    summary_file.write("\n")
    summary_file.write(f"Greatest Decrease in Profits: {months[min_profit_month]} (${(str(max_profit_decrease))})")
