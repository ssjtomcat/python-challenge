import os
import csv

# Path to CSV file
election_dataCSV = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

# Variable to keep count of totalvotes
total_votes = 0

# Read CSV file
with open(election_dataCSV, 'r') as csvfile:

	# Split the data on commas
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Skip header
    next(csvreader)

    # create dictionary to hold vote information
    vote_info = {}

    # Loop through rows
    for row in csvreader:

    	# count number of votes
    	total_votes += 1

    	# Candidate name from csv file
    	candidate_name = row[2]

    	# CHeck if candidate name is in dictionary 
    	if candidate_name not in vote_info.keys():

    		# Add new candidate
    		vote_info[candidate_name] = 1

    	else:

    		# Adds one vote to known candidate
    		vote_info[candidate_name] += 1


    # Print Polling Results
    print("Election Results")
    print("--------------------------------------")
    print("Total Votes: ", total_votes)
    print("--------------------------------------")

    for key,value in vote_info.items():
    	print(key,":", '{0:.02%}'.format(value/(total_votes)), (value), "votes")
    print("--------------------------------------")
    print("Winner: ", max(vote_info, key=lambda i: vote_info[i]))
    print("--------------------------------------")

    # Write to text file
    file = open("Results.txt","w")

    file.write("Election Results" + '\n')
    file.write("--------------------------------------" + '\n')
    file.write("Total Votes: " + str(total_votes) + '\n')
    file.write("--------------------------------------"+ '\n')

    for key,value in vote_info.items():
    	file.write(key + ": " + '{0:.02%}'.format(value/(total_votes)) + " " + str((value)) + " votes" + '\n')
    file.write("--------------------------------------"+ '\n')

    file.write("Winner: " + max(vote_info, key=lambda i: vote_info[i]) + '\n')
    file.write("--------------------------------------"+ '\n')
