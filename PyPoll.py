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



#open the elections results and read the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)
#Perform the analysis
    


