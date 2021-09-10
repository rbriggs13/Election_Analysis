#The data we need to retrieve.
#1. The toal number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

import csv
import os

#Assign a variable for the file to load
file_to_load = os.path.join("Resources", "election_results.csv")

#Creating a filename variable and open it in order to write in it
file_to_save = os.path.join("analysis", "election_analysis.txt")

#variable to count all the votes
total_votes = 0
#list for the candidates
candidate_options = []
#dictionary to hold the votes for each candidate
candidate_votes = {}
#variables used to determine the winner
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#open the elections results and read the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    headers = next(file_reader)


    #Count each vote in the csv file
    for row in file_reader:
        total_votes += 1
        
        #adding candidate names to the list
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            #starting the track the candidate's vote count
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] +=1

#calculate vote percentage and print the results
for candidate in candidate_options:
    votes = candidate_votes[candidate]
    vote_percent = float(votes)/float(total_votes) * 100

    #setting the winning candidate
    if votes > winning_count and vote_percent > winning_percentage:
        winning_count = votes
        winning_percentage = vote_percent
        winning_candidate = candidate

    print(f'{candidate}: {vote_percent:.1f}% ({votes:,})\n')


#print the winning candidate
winning_summary = (
    f'-----------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n'
    f'-----------------------\n'
)

print(winning_summary)

