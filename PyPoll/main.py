#Imported modules to allow python to read csv files, and create a path to the file.
import os
import csv

#setting the path for the file
election_path = os.path.join("Resources", "election_data.csv")

#Will open the csv file 
with open(election_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    #Skips the header in the csv file
    csv_header = next(csv_file)

