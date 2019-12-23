# 10a. Create a list of 6 numbers. Use ‘list-comprehension’ to create a 
# new list where each element in the original list is multiplied by 3. 
# Use ‘lambda’ and ‘reduce’ function find the sum of the elements of the original list
#  as well as the new list.


import sys
import functools

list1 = []
for i in range(4):
    list1.append(int(input("Enter number: ")))

list2 = list([i*3 for i in list1])
print(list2)

print(functools.reduce(lambda x,y: x+y,list1))
print(functools.reduce(lambda x,y: x+y,list2))