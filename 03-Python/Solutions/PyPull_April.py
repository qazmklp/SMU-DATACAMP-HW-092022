#import file

import csv

csvpath = "C:/Users/april/OneDrive/Desktop/SMU BOOT CAMP922/GITLAB/SMU-VIRT-DATA-PT-09-2022-U-LOLC/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv"


rows = 0
votes = {}



with open(csvpath, encoding='utf-8') as csvfile:
    csvreader =csv.reader(csvfile, delimiter=',')

    #read the header skip if there is no header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    for row in csvreader:
        # print(row)
         rows += 1
         candidate = row[2]

         #build candidate dictionary
         if candidate in votes.keys():
            votes[candidate] += 1
         else:
            votes[candidate] = 1

        

   
        
# print(rows)

# for x in votes.keys():
#     print(x)
#     print(f"{votes[x]} total votes which is {100*votes[x]/rows}%")
#     print()
#https://stackoverflow.com/questions/268272/getting-key-wih-manimum-value-in-dictionary
winner = max(votes, key=votes.get)
# print(winner)


# Specify the variable to hold the contents
output= f""" Election Results
----------------------
Total Votes:{rows}
----------------------"""
#loop from prof Booth

for x in votes.keys():
    total_votes=round(100*votes[x]/rows,3)
    # print(x)
    newline=f"""
    {x}:{total_votes}% ({votes[x]}) """
    # print()
    output += newline

# print winner = max(votes, key=votes.get)
lastline=f"""
--------------------
Winner:{winner} 
---------------------"""
output+= lastline
print(output)

# print(output) to text file

with open('Pypull.text','w') as f:
    f.write(output)



#use Hard Code write to the text file
ouput_hardcode=f"""
Election Results
  -------------------------
  Total Votes: {rows}
  -------------------------
  Charles Casper Stockham: {round(100*votes["Charles Casper Stockham"]/rows,3)}% {votes["Charles Casper Stockham"]}
  Diana DeGette: {round(100*votes["Diana DeGette"]/rows,3)}% {votes["Diana DeGette"]}
  Raymon Anthony Doane: {round(100*votes["Raymon Anthony Doane"]/rows,3)}% {votes["Raymon Anthony Doane"]}
  -------------------------
  Winner: {winner} 
  -------------------------"""

print(ouput_hardcode)

# print(output) to text file

with open('Pypull hardcode.text','w') as f:
    f.write(ouput_hardcode)






