import os
# Import module for reading CSV files
import csv

#Get current working directory
cwkdir = os.getcwd()
#Append file directory and make a complete file path
filepath = os.path.join( cwkdir,'Resources','election_data.csv')

#Initialize variables
totalcount = 0; kcount = 0; ccount = 0; lcount = 0; ocount = 0; max_votecount = 0

#Function for % calculation
def percentage (part, whole):
    return 100 * float(part)/float(whole)

#Open and read CSV file
with open(filepath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')

     for i in csvreader:
         voterid = i[0]
         country = i[1]
         candidate = i[2]
         # Find Total Vote Count
         totalcount = totalcount + 1

         # Find votecount by candidates
         if candidate =="Khan":
            kcount = kcount + 1
         if candidate =="Correy":
            ccount = ccount + 1
         if candidate =="Li":
            lcount = lcount + 1
         if candidate =="O'Tooley":
            ocount = ocount + 1
            
# Define (dictionary) list : candidate and votes
     candidatevote = {"Khan": kcount,"Correy": ccount,"Li" :lcount, "O'Tooley": ocount}
     # Find winner 
     for candidate, value in candidatevote.items():
         if value > max_votecount:
            max_votecount = value
            winner = candidate
# Display results       
print(f'Election Results'+'\n')
print(f'-------------------------------'+'\n')
print(f'Total Votes: {totalcount}'+'\n')
print(f'-------------------------------'+'\n')

print(f'Khan: {percentage(kcount,totalcount):.3f}%  ({kcount})')
print(f'Correy: {percentage(ccount,totalcount):.3f}%  ({ccount})')
print(f'Li: {percentage(lcount,totalcount):.3f}%  ({lcount})')
print(f'O\'Tooley: {percentage(ocount,totalcount):.3f}%  ({ocount})')
print(f'--------------------------------'+'\n')
print(f'Winner: {winner} '+'\n')
print(f'--------------------------------'+'\n')

 # output to a text file


file = open("output.txt","w")
    
file.write(f'Election Results'+'\n')
file.write(f'-------------------------------'+'\n')
file.write(f'Total Votes: {totalcount}'+'\n')
file.write(f'-------------------------------'+'\n')
file.write(f'Khan: {percentage(kcount,totalcount):.3f}%  ({kcount})')
file.write(f'Correy: {percentage(ccount,totalcount):.3f}%  ({ccount})')
file.write(f'Li: {percentage(lcount,totalcount):.3f}%  ({lcount})')
file.write(f'O\'Tooley: {percentage(ocount,totalcount):.3f}%  ({ocount})')
file.write(f'--------------------------------'+'\n')
file.write(f'Winner: {winner} '+'\n')
file.write(f'--------------------------------'+'\n')
file.close()
