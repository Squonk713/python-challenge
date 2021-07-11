
### import modules and oper source file ###

import os
import csv

budget_data = os.path.join("budget_data.csv")

with open(budget_data, mode="r", newline="", encoding='UTF-8') as budget_data_csv:
    budget_data_reader = csv.reader(budget_data_csv, delimiter=",")    

    next(budget_data_reader, None) 

### get row count of values ###

    budget_df = list(budget_data_reader)

    row_count = len(budget_df)

### loop data into lists ###

    values_sum = []
    dates = []

    for row in budget_df:
            value = row[1]
            date = row[0]
            values_sum.append(value)
            dates.append(date)

### convert string values to integer ###

    values_int = list(map(int, values_sum))

### sum values ###

    values_total = sum(values_int[:])

### calculate average difference ###

valuesdiff = [values_int[n]-values_int[n-1] for n in range(1,len(values_int))]

diff_total = sum(valuesdiff[:])

count = len(valuesdiff)

AvgDiff = diff_total / count

### get max values and dates ###

MaxIncrease = max(valuesdiff)
MaxDecrease = min(valuesdiff)

IncreaseDate = dates[valuesdiff.index(MaxIncrease)]
DecreaseDate = dates[valuesdiff.index(MaxDecrease)]

### terminal output ###

print("---------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: " + str(row_count))
print("Total Profits: " + "$" + str(values_total))
print("Average Change: " + "$" + str(int(AvgDiff)))
print("Greatest Increase in Profits: " + str(IncreaseDate) + " ($" + str(MaxIncrease) + ")")
print("Greatest Decrease in Profits: " + str(DecreaseDate) + " ($" + str(MaxDecrease)+ ")")
print("----------------------------------------------------------")

### txt file output ###

with open('financial_analysis.txt', 'w') as analysis:
     analysis.write("---------------------------------------------------------\n")
     analysis.write("Financial Analysis\n")
     analysis.write("----------------------------------------------------------\n")
     analysis.write("Total Months: " + str(row_count)+"\n")
     analysis.write("Total Profits: " + "$" + str(values_total)+"\n")
     analysis.write("Average Change: " + "$" + str(int(AvgDiff))+"\n")
     analysis.write("Greatest Increase in Profits: " + str(IncreaseDate) + " ($" + str(MaxIncrease) + ")\n")
     analysis.write("Greatest Decrease in Profits: " + str(DecreaseDate) + " ($" + str(MaxDecrease)+ ")\n")
     analysis.write("----------------------------------------------------------\n")
 
