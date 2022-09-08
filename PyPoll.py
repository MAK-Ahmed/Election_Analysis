# Data we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of all candidates who received votes
# 3. The percentage of votes each candidate won 
# 4. The total number of votes each cadidate won
# 5. The winner of the election based on popular vote

    #import modules (dependencies)
# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0

#candidate options and candidate votes
candidate_options = []

#declare a empty dictionary
candidate_votes = {}

# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here

      # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # print the header row.
    headers = next(file_reader)


# Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

    #Begin to track the candidiate's vote count
            candidate_votes[candidate_name] = 0

      #add to the candidatess vote count
        candidate_votes[candidate_name] += 1


#the results need to be written to a text file
with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    

      #calcuating 
      #formula is vote_percentage = votes/total_votes) * 100
      #calculate the percentage of votes for each candidate and convert to an integer

      #1. iterate through the candadate list
    for candidate_name in candidate_votes:
      #get the vote count for each candidate - this is using the dictionary and key variable
        votes = candidate_votes[candidate_name]

      #calculate the percentage of votes
        vote_percentage = float(votes)/float(total_votes) * 100

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)



      #Determining the winning candidate using a for loop

      # 1. is winning count greater than vote count set the winning to be equal to that number
        if (votes > winning_count) and (vote_percentage > winning_percentage):

      #2 if true then set the values as follows 
          winning_count=votes
          winning_percentage=vote_percentage

      #3 assign the candidate name to the winner
          winning_candidate_name = candidate_name

    winning_summary = (f"-------------------------\n"
          f"Winner: {winning_candidate_name}\n"
          f"Winning Vote Count: {winning_count:,}\n"
          f"Winning Percentage: {winning_percentage:.1f}%\n"
          f"-------------------------\n")

      #print(winning_summary)