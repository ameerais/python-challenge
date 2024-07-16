# Import required libraries
import os, csv
from pathlib import Path 

# Set the path for the CSV file using pathlib
csv_file_path = Path("Resources", "election_data.csv")

# Initialize vote counters for each candidate
total_votes = 0 
votes_stockham = 0
votes_degette = 0
votes_doane = 0

# Open the CSV file in read mode
with open(csv_file_path, newline="", encoding="utf-8") as election_data:

    # Read the CSV file contents
    csv_reader = csv.reader(election_data, delimiter=",") 

    # Skip the header row
    header = next(csv_reader)     

    # Process each row in the CSV file
    for row in csv_reader: 

        # Increment the total vote count
        total_votes += 1

        # Tally votes for each candidate
        if row[2] == "Charles Casper Stockham": 
            votes_stockham += 1
        elif row[2] == "Diana DeGette":
            votes_degette += 1
        elif row[2] == "Raymon Anthony Doane": 
            votes_doane += 1

# Create a dictionary to store the candidates and their corresponding vote counts
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [votes_stockham, votes_degette, votes_doane]

# Combine the candidate names and their vote counts into a dictionary
vote_counts = dict(zip(candidates, votes))

# Determine the winner by finding the candidate with the maximum votes
winner = max(vote_counts, key=vote_counts.get)

# Calculate the percentage of votes for each candidate
percent_stockham = (votes_stockham / total_votes) * 100
percent_degette = (votes_degette / total_votes) * 100
percent_doane = (votes_doane / total_votes) * 100

# Print the election results summary
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {percent_stockham:.3f}% ({votes_stockham})")
print(f"Diana DeGette: {percent_degette:.3f}% ({votes_degette})")
print(f"Raymon Anthony Doane: {percent_doane:.3f}% ({votes_doane})")
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")

# Define the path for the output file using pathlib
output_file_path = Path("analysis", "Summary.txt")

# Write the election results summary to the output file
with open(output_file_path, "w") as file:
    file.write(f"Election Results\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write(f"----------------------------\n")
    file.write(f"Charles Casper Stockham: {percent_stockham:.3f}% ({votes_stockham})\n")
    file.write(f"Diana DeGette: {percent_degette:.3f}% ({votes_degette})\n")
    file.write(f"Raymon Anthony Doane: {percent_doane:.3f}% ({votes_doane})\n")
    file.write(f"----------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write(f"----------------------------\n")
