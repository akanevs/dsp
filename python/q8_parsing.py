# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# file reads in football data from csv file

import csv

#name of csv data file
fname_football = '/Users/akanevs/ds/metis/metisgh/prework/dsp/python/football.csv'

print('Reading footlball data ...')
    
team_name = []
goals_for = []
goals_against = []

temp = 0
csvfile = open(fname_football)
reader = csv.reader(csvfile)
for row in reader:
    #start with 2nd row
    if temp>0:
        team_name.append(str(row[0]))
        goals_for.append(int(row[5]))
        goals_against.append(int(row[6]))
    temp=temp+1

#absolute difference between for and against goals
mindiff = 1000
for j in range(len(goals_for)):
    if mindiff > abs(goals_for[j] - goals_against[j]):
        mindiff = abs(goals_for[j] - goals_against[j])
        mindiff_team = team_name[j]
    
print('Minumum difference in for and against goals:',mindiff)
print('Team:',mindiff_team)

#Output ====================================================
#bash-3.2$ python q8.py
#Reading footlball data ...
#Minumum difference in for and against goals: 1
#Team: Aston_Villa
