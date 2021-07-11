
### import modules and oper source file ###

import os
import csv

election_data = os.path.join("election_data.csv")

with open(election_data, mode="r", newline="", encoding='UTF-8') as election_data_csv:
    election_data_reader = csv.reader(election_data_csv, delimiter=",")    

    next(election_data_reader, None) 

### get row count of values ###

    election_df = list(election_data_reader)

    row_count = len(election_df)

    print (row_count)

### loop data into lists ###

    candidates = []

    for row in election_df:
            candidate = row[2]
            candidates.append(candidate)

### get individual candidate vote count ###

    Khan_count = candidates.count("Khan")
    Correy_count = candidates.count("Correy")
    Li_count  = candidates.count("Li")
    OTooley_count  = candidates.count("O'Tooley")

    print(Khan_count)

### get individual candidate percentage ###

Khan_percentage = Khan_count / row_count * 100
Correy_percentage = Correy_count / row_count * 100
Li_percentage = Li_count / row_count * 100
OTooley_percentage = OTooley_count / row_count * 100

### identify the winner ###

candidates = ["Khan", "Correy", "Li", "O'Tooley"]
voteshare = [Khan_count, Correy_count, Li_count, OTooley_count]

dictionary_candidates_and_votes = dict(zip(candidates,voteshare))
key = max(dictionary_candidates_and_votes, key=dictionary_candidates_and_votes.get)

winner = key

### terminal output ###

print("---------------------------------------------------------")
print("Election Results")
print("----------------------------------------------------------")
print("Total Votes: " + str(row_count))
print("Khan: " + str(Khan_percentage) + "% ("  + str(Khan_count) + ")")
print("Correy: " + str(Correy_percentage) + "% ("  + str(Correy_count) + ")")
print("Li: " + str(Li_percentage) + "% ("  + str(Li_count) + ")")
print("O'Tooley: " + str(OTooley_percentage) + "% ("  + str(OTooley_count) + ")")
print("----------------------------------------------------------")
print("Winner:" + str(winner))
print("----------------------------------------------------------")

### txt file output ###

with open('election_analysis.txt', 'w') as analysis:
     analysis.write("---------------------------------------------------------\n")
     analysis.write("Election Results\n")
     analysis.write("----------------------------------------------------------\n")
     analysis.write("Total Votes: " + str(row_count))
     analysis.write("Khan: " + str(Khan_percentage) + "% ("  + str(Khan_count) + ")\n")
     analysis.write("Correy: " + str(Correy_percentage) + "% ("  + str(Correy_count) + ")\n")
     analysis.write("Li: " + str(Li_percentage) + "% ("  + str(Li_count) + ")\n")
     analysis.write("O'Tooley: " + str(OTooley_percentage) + "% ("  + str(OTooley_count) + ")\n")
     analysis.write("----------------------------------------------------------\n")
     analysis.write("Winner:" + str(winner) + "\n")
     analysis.write("----------------------------------------------------------\n")

 