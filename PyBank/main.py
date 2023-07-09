#Imported modules to allow python to read csv files, and create a path to the file.
import os
import csv

#setting the path for the file
budget_path = os.path.join("Resources", "budget_data.csv")

#Will open the csv file 


print("Financial Analysis")
print("------------------------------")

#This will give the total number of months in the data set
with open(budget_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    #Skips the header in the csv file
    csv_header = next(csv_file)

    #prints the total number of rows in the csv file
    totalM = len(list(csvreader))
    print(f"Total months:  {totalM}")

#Calculates the sum of the profit/losses column is the csv file
with open(budget_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    #Skips the header in the csv file
    csv_header = next(csv_file)

    #This will add the value for each row and place it into the variable 
    Profit = 0
    for row in csvreader:
        Profit += int(row[1])

    print(f"Total: ${Profit}")

#This will run through each line and compare it to the last value to find the change.
#it will also calculate the average change by storing all changes in a list and finding the mean 
with open(budget_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    #Skips the header in the csv file
    csv_header = next(csv_file)

    max_increase = 0
    previous_row = None
    change = 0
    max_decrease = 0
    highmonth = None
    lowmonth = None
    changes = []

    #this will calculate the average change by storing all changes in a list and finding the mean  
    for row in csvreader:
        if previous_row is not None:
            #will find the change in the values and add it to the list
            change = int(row[1]) - previous_row
            changes.append(change)
            #this will store the highest positive change by comparing the change to the previous high change 
            if change > 0 and change > max_increase:
                max_increase = change
                highmonth = row[0]
            #this will store the lowest negative change by comparing the change to the previous low change
            elif change < 0 and change < max_decrease:
                max_decrease = change
                lowmonth = row[0]
        #will store the first value as the previous row as there is nothing prior to the first value
        previous_row = int(row[1])
        
    average_change = sum(changes) / len(changes)
    print(f"Average Change: ${round(average_change, 2)}")
    print(f"Greatest Increase in Profits: {highmonth} (${max_increase})")
    print(f"Greatest Decrease in Profits: {lowmonth} (${max_decrease})")
    
#Path for the output file.
output_path = os.path.join("analysis", "budget_analysis.txt")

#This will write the data to the text file
with open(output_path, "w",) as datafile:
    #List for everything that will be written to the text file. str() functions to cast my
    #variables as strings and write them into the text file.
    data = ["Financial Analysis ", "------------------------------",
            "Total months: " + str(totalM), "Total: $"+ str(Profit),"Average Change: $" + str(round(average_change,2)),
            "Greatest Increase in Profits: " + str(highmonth) +" ($" + str(max_increase) + ")",
            "Greatest Decrease in Profits: " + str(lowmonth) +" ($" + str(max_decrease) + ")"
            ]
    for line in data:
        datafile.write(line + '\n')