# -*- coding: utf-8 -*-
import numpy as np
import sys
import csv

#######################################################

# ------- INITALIZE VARIABLES AND COSNTANTS ----------#

#######################################################

OUT = []
GENRE_SORES = {}
INPUT = []
personalities = ["extraversion", "intuition", "thinking", "judging", "assertiveness"]
genres = ["punk", "jazz", "classical", "rock", "alternative rock", 
          "reggae", "ambient", "world", "pop", "metal", "hip-hop",
          "electronica", "religious", "blues", "country", "soul"]
personality_scores =  [[-4, 10,2,-11,-5], 
                        [8, 8, 0, -3, 7],
                        [-2, 12, 4, 4, 5],
                        [-2, 12, 2,-6,0],
                        [-1, 7, -5, -6, -6],
                        [9,0,-6,-5,4],
                        [3,6,-6,-6,-2],
                        [3,9,-10,-2,1],
                        [10,-8,-16,0,-9],
                        [-9,11,9,-8,3],
                        [14,2,-2,-5,2],
                        [9,4,-4,-5,-1],
                        [6, -6, -12, 5, 1],
                        [7, 9, -4, -3, 7],
                        [7, -9, -10, 1, 3],
                        [13, -1, -13, -3, -1]]



#######################################################

# ---------------- HANDLE INPUT ----------------------#

#######################################################

#inputs a CSV file to be read and then processed
filename = sys.argv[1]

#read the file
with open(filename, 'r') as p:
    filenameReader = csv.reader(p, delimiter=" ")
    for row in filenameReader:
        INPUT.append(row[0].lower())
        

#######################################################

# ------------------- PROCESS ------------------------#

#######################################################

#gets the number of elements in the inputted CSV file
NUM_ELEMENTS = len(INPUT)

#initalizes the output list
for row in personalities:
    OUT.append(0)
  
#go through each element in genre and create the 
#personality profile for the current user
i = 0
for row in genres:
    GENRE_SORES[row] = personality_scores[i]
    i = i + 1
    
#update personaltiy scores depending on num
#occurences of each genre
for row in INPUT:
    scores = GENRE_SORES[row]
    a = np.add(scores, OUT)
    b = np.ndarray.tolist(a)
    OUT = b
  
#get the averages of the scores
#in order to complete personality profiler
averages = []
for row in OUT:
    avg =  row / NUM_ELEMENTS
    averages.append(avg)
    
    
    
#######################################################

# ----------- CYC STATEMENTS TO OUTPUT ---------------#

#######################################################
    
    
#create cyc statements for the CYC language
#corresponding to personality profiler
    
zero = "(has (PersonalityScore Extroverted " + str(averages[0]) + "))"
one = "(has (PersonalityScore Intuition " + str(averages[1]) + "))"
two = "(has (PersonalityScore Thinking " + str(averages[2]) + "))"
three = "(has (PersonalityScore Judging " + str(averages[3]) + "))"
four = "(has (PersonalityScore Assertiveness " + str(averages[4]) + "))"

f = open("output.txt", "w")
print >> f, zero
print >> f, one
print >> f, two
print >> f, three
print >> f, four
    
f.close()



    




































    

