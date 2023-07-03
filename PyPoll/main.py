#Imported modules to allow python to read csv files, and create a path to the file.
import os
import csv

#setting the path for the file
election_path = os.path.join("Resources", "election_data.csv")

print("Election Results")
print("--------------------------")

#varable to store the total number of voters
total=0


#Will open the csv file 
with open(election_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    #Skips the header in the csv file
    csv_header = next(csv_file)
    #prints the total number of rows in the csv file
    total = len(list(csvreader))
    print(f"Total Votes:  {total}")

print("--------------------------")

#list to hold the names on the candidates
candidates = []

#will go through the csv file and store the unique names if all candidates
with open(election_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    #Skips the header in the csv file
    csv_header = next(csv_file)

    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])

#sets a dictionary with the candidates and a starting vote count of 0 for each candidate
votes = {}

for candidate in candidates:
    votes[candidate]=0

#will add a vote count to the appropriate candidate
with open(election_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    #Skips the header in the csv file
    csv_header = next(csv_file)

    
    #will check if candidate is in the votes dict and add a vote for each ballot
    for row in csvreader:
        for candidate in votes:
            if str(row[2]) == candidate:
                votes[candidate] += 1
#this will convert the votes dict to a dict that has lists for values so that i 
#may add teh percentages associated with each candidate
new_votes = {key: [value] for key, value in votes.items()}

#this will calculate the percentage vote for each candidate
percentages = []
for value in votes.values():
    percentage = ((value / total) * 100)
    percentages.append(percentage)

#This will add the percentage values in the list 'percentages' to the keys in the new_votes dictionary
for key, value in new_votes.items():
    value.append(percentages.pop(0))

print(new_votes)


winner = max(votes, key=votes.get)

print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")
