# -*- coding: UTF-8 -*-

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0

# Add more variables to track other necessary financial data

average_change = 0
greatest_inc_profits = 0
greatest_dec_profits = 0
net_changes = []


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # Track the total and net change

    total = int(first_row[1])
    net_change = 0
    total_months = 1
    prev_profit_loss = int(first_row[1])

    # Process each row of data
    
    for row in reader:

        # Track the total
        
        total = total + int(row[1])
        total_months = total_months + 1

        # Track the net change

        net_change = int(row[1]) - prev_profit_loss
        net_changes.append(net_change)


        # Calculate the greatest increase in profits (month and amount)

        if net_change > greatest_inc_profits:
            greatest_inc_profits = net_change
            greatest_inc_profits_month = row[0]
            

        # Calculate the greatest decrease in losses (month and amount)

        if net_change < greatest_dec_profits:
            greatest_dec_profits = net_change
            greatest_dec_profits_month = row[0]

        prev_profit_loss = int(row[1])
        
# Calculate the average net change across the months

average_change = sum(net_changes) / len(net_changes)
        
# Generate the output summary

output =  (
    '\n'
    'Financial Analysis\n'
    '----------------------------\n'
    f'Total Months: {total_months}\n'
    f'Total: ${total}\n'
    f'Average Change: ${round(average_change, 2)}\n'
    f'Greatest Increase in Profits: {greatest_inc_profits_month} (${greatest_inc_profits})\n'
    f'Greatest Decrease in Profits: {greatest_dec_profits_month} (${greatest_dec_profits})\n'
)
# Print the output

print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
