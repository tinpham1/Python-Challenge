# -*- coding: UTF-8 -*-

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts

candidates = {}

# Winning Candidate and Winning Count Tracker

winning_candidate = ""
winning_count = 0


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(".", end="")

        # Increment the total vote count for each row

        total_votes = total_votes + 1

        # Get the candidate's name from the row

        candidates_name = row[2]

        # If the candidate is not already in the candidate list, add them

        if candidates_name not in candidates:
            candidates[candidates_name] = 0

        # Add a vote to the candidate's count

        candidates[candidates_name] = candidates[candidates_name] + 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)

    print(total_votes)

    # Write the total vote count to the text file

    txt_file.write(f"Total Vote Count: {total_votes}")

    # Generate Election Results Header, Print Total Votes

    print(f"\n")
    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"-------------------------")

    # Loop through the candidates to determine vote percentages and identify the winner   
    
    for candidate, votes in candidates.items():
        

        # Get the vote count and calculate the percentage

        vote_percentage = votes / total_votes * 100


        # Update the winning candidate if this one has more votes
        
        if votes > winning_count:
            winning_candidate = candidate
            winning_count = votes
    
        # Print and save each candidate's vote count and percentage

        print(f"{candidate}: {round(vote_percentage, 3)}% ({votes})")

    # Print the winning candidate

    print(f"-------------------------")
    print(f"Winner: {winning_candidate}")
    print(f"-------------------------")

    # Save the winning candidate summary to the text file

    txt_file.write(f"\n\n")
    txt_file.write(f"Election Results\n")
    txt_file.write(f"-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write(f"-------------------------\n")
    for candidate, votes in candidates.items():
        vote_percentage = votes / total_votes * 100
        txt_file.write(f"{candidate}: {round(vote_percentage, 3)}% ({votes})\n")
    txt_file.write(f"-------------------------\n")
    txt_file.write(f"Winner: {winning_candidate}\n")
    txt_file.write(f"-------------------------\n")