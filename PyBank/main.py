#Imported modules to allow python to read csv files, and create a path to the file.
import os
import csv

#setting the path for the file
budget_path = os.path.join("Resources", "budget_data.csv")

#Will open the csv file 


print("Financial Analysis")
print("------------------------------")

with open(budget_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    #Skips the header in the csv file
    csv_header = next(csv_file)

    #prints the total number of rows in the csv file
    totalM = len(list(csvreader))
    print(f"Total months:  {totalM}")

with open(budget_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    #Skips the header in the csv file
    csv_header = next(csv_file)

    #This will add the value for each row and place it into the variable 
    Profit = 0
    for row in csvreader:
        Profit += int(row[1])

    print(f"Total: {Profit}")
    


    




