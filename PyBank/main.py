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

#This will calculate the average change and print in terminal    
change = (Profit / totalM)
print(f"Average Change: ${round(change, 2)}")

#This will go through each line and compare the last value and will
#store whichever value is higher until it finds the highest value (max)
with open(budget_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    #Skips the header in the csv file
    csv_header = next(csv_file)

    max_increase = 0
    for row in csvreader:
        if int(row[1]) > int(max_increase):
            highmonth = row[0]
            max_increase = row[1]

    print(f"Greatest Increase in Profits: {highmonth} (${max_increase})")  

#This will go through each line and compare the last value and will
#store whichever value is lower until it finds the lowest value (minimum)
with open(budget_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    #Skips the header in the csv file
    csv_header = next(csv_file)

    max_decrease = 0
    for row in csvreader:
        if int(row[1]) < int(max_decrease):
            lowmonth = row[0]
            max_decrease = row[1]

    print(f"Greatest Decrease in Profits: {lowmonth} (${max_decrease})")  

#Path for the output file.
output_path = os.path.join("analysis", "budget_analysis.txt")

#This will write the data to the text file
with open(output_path, "w",) as datafile:
    #List for everything that will be written to the text file. str() functions to cast my
    #variables as strings and write them into the text file.
    data = ["Financial Analysis ", "------------------------------",
            "Total months: " + str(totalM), "Total: $"+ str(Profit),"Average Change: $" + str(round(change,2)),
            "Greatest Increase in Profits: " + str(highmonth) +" ($" + str(max_increase) + ")",
            "Greatest Decrease in Profits: " + str(lowmonth) +" ($" + str(max_decrease) + ")"
            ]
    for line in data:
        datafile.write(line + '\n')