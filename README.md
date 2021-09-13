# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has requested an analysis of the data from a local congressional election in order to audit the election. The following tasks were required for a complete audit.

1. Calculate the total number of votes cast.
2. Retrieve a complete list of candidates who recieved votes.
3. Determine the percentage of votes each candidate received based on the total number of votes.
4. Calculate the total number of votes each candidate received.
5. Determine the winner of the election based on the popular vote.

## Resources
- Data Source: election_results.csv
- Software used: Python 3.9.7 and Visual Studio Code 1.60

## Summary
The analysis of the election data shows that:
- The total amount of votes cast in the election was 369,711 votes
- The Candiates in the election were:
   - Charles Casper Stockham
   - Diana DeGette
   - Raymon Anthony Doane
- The results for each candidate were:
   - Charles Casper Stockham received 23.0% of the vote (85,213 votes).
   - Diana DeGette received 73.8% of the vote (272,892 votes).
   - Raymon Anthony Doane received 3.1% of the vote (11,606 votes).
 - The winner of the election was Diana Degette with 73.8% of the vote with 272,892 out of the 369,711 votes.

# Election_Analysis_Challenge

## Challenge Overview
The purpose of this project was to to analyze the data from a congressional election in colorado. The analysis needed to determine the total votes cast, the percentage and number of votes from each county in the election, the percentage and number of votes from each candidate in the election, and the winner of the election by the popular vote.

## Results
- There were 369,711 total votes cast in this election
- The county votes were as follows:
    - Jefferson: 10.5% (38,855 votes)
    - Denver: 82.8% (306,055 votes)
    - Arapahoe: 6.7% (24,801 votes)
 - Denver had the largest turnout of voters with 82.8%
 - The candiate votes were as follows:
    - Charles Casper Stockham: 23.0% (85,213 votes)
    - Diana DeGette: 73.8% (272,892 votes)
    - Raymon Anthony Doane: 3.1% (11,606 votes)

 - The winner of the election was Diana Degette with 73.8% of the vote and 272,892 votes in total out of the 369,711 votes cast.

All of this information can also be found in the analysis folder of this repository.

## Audit Summary
The great thing about this code is that with a few small adjustments it can be used to audit any election. The first thing that would have to change is the code that locates both the data file and creates/locates the text file where the results are written. The current code is shown below:

```
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

```
(It should be noted this code is locatecd on rows 8-11)
The sections in the parathesis would have to be changed to reflect the current locations of the files that you would want to work with. With the data file being the variable file_to_load and the text file being file_to_save. The other thing that would have to be changed would be all the sections of code involving the format of the data file. This is shown in the code below:

```

# Read the header
    header = next(reader)

```
and

```

# Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

```

(It should be noted this code is located on lines 39-40 and 48-52 respectively)
The first line of code skips the header line in the count, this would have to be changed if the data file either doesn't have a header or if it isn't located on the first line. The other code is taking the candiate name from the 3rd column and the county name from the 2nd column. This would have to be edited if that information isn't present in those columns in the data file being used. With these simple changes this code can be repurposed for use in any congressional election.
