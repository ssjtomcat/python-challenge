import os
import csv

# List
profit_loss = []
profit_loss_change=[]
date = []


# Path to collect data from the Resources folder
budget_dataCSV = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

# Read in the CSV file to find number of rows
with open(budget_dataCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile)

    # Skip header
    next(csvreader)


    for row in csvreader:

        # Add to profit_loss
        profit_loss.append(float(row[1]))
        
        # Add to date
        date.append(row[0])

    # Find The average of the changes in "Profit/Losses" over the entire period
    for i in range(1, len(profit_loss)):

        # Create a column with the difference of two cells
        profit_loss_change.append(profit_loss[i] - profit_loss[i-1])

        average_change = sum(profit_loss_change)

        # Find max profit change
        max_increase = max(profit_loss_change)

        # Find the date of max profit change
        max_increase_date = str(date[profit_loss_change.index(max_increase)])

        # FInd min profit change
        min_increase = min(profit_loss_change)  
   
        # Find the date of min profit change
        min_increase_date = str(date[profit_loss_change.index(min_increase)])


    # Print out the budget data
    
    print("Financial Analysis")
    print("--------------------------------------")
    print("Total Months: ", len(date))
    print("Total: $", sum(profit_loss))
    print("Average Change: $", round(average_change))
    print("Greatest Increase in Profits:", max_increase_date, "($", max_increase,")")
    print("Greatest Decrease in Profits:", min_increase_date, "($", min_increase,")")

# Write to text file
file = open("Results.txt","w")

file.write("Financial Analysis" + '\n')
file.write("--------------------------------------" + '\n')
file.write("Total Months: " + str(len(date)) + '\n')
file.write("Total: $"+ str(sum(profit_loss)) + '\n')
file.write("Average Change: $" + str(round(average_change)) + '\n')
file.write("Greatest Increase in Profits:" + max_increase_date + " $" + str(max_increase) + '\n')
file.write("Greatest Decrease in Profits:" + min_increase_date + " $" + str(min_increase) + '\n')

file.close()