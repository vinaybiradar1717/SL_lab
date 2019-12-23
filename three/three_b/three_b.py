# 3b. Python File Handling & List Comprehension: 
# Write a python program to read contents of a 
# file (filename as argument) and store number of 
# occurrences of each word in a dictionary. Display the top 10 
# words with most number of occurrences in descending order. 
# Store the length of each of these words in a list and display the list. 
# Write a one-line reduce function to get the average length 
# and one-line list comprehension to display squares of all odd numbers and display both.  

import sys
import os
import functools

d = {}
list1 = []
f = open(sys.argv[1])
data = f.read().split()

#print(sys.argv)

for i in data:
    if i not in d:
        list1.append(len(i))
        d[i] = 0
    d[i] += 1

list1.sort(reverse=True)
list2 = list(list1[0:10])
print(list2)

list3 = []
for i,j in d.items():
    list3.append([i,j])
print(list3)
print(functools.reduce(lambda i,j: i+j,list2)/len(list2))
print([i*i for i in list2 if i%2!=0])