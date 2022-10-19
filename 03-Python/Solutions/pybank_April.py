
#open and import file

import csv

csvpath = "C:/Users/april/OneDrive/Desktop/SMU BOOT CAMP922/GITLAB/SMU-VIRT-DATA-PT-09-2022-U-LOLC/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"

rows = 0
total=0

tot_changes=0
num_changes=0
last_profit=0

max_change=-999999999999
min_change=999999999999
min_month=""
max_month=""

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader =csv.reader(csvfile, delimiter=',')


    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
            
    for row in csvreader:
        # print(row)
         rows += 1
         total += int(row[1]) 

        
        #calculate changes
         if rows !=1:
            change = int(row[1])-last_profit
            tot_changes += change
            num_changes += 1


            #find max and min
            if (change>max_change):
                max_change = change
                max_month = row[0]
            elif(change < min_change):
                min_change = change
                min_month = row[0]
            else:
                pass
            
        

         last_profit=int(row[1])  

        
ave_change=round(tot_changes/num_changes,3)  
      
# print(rows)
# print(total)
# print(num_changes)
# print(ave_change)
# print(f"Max Change: {max_month}:{max_change}")
# print(f"Min Change: {min_month}: {min_change}")

# output_path = "Solutions\PyBank\Pybank.text"

output_path = f"""        Financia Analysis
        --------------------------------------------------------
        Total Months: {rows}
        Total: ${total}
        Average Change: ${ave_change}
        Greatest Increase in Profits: {max_month}  (${max_change})
        Greatest Decrease in Profit: {min_month}  (${min_change})
        ---------------------------------------------------------"""


# print(output_path) to text file

with open('Pybank.text','w') as f:
    f.write(output_path)



