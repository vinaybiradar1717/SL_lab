# 1a. Write Python code to do the following:
#     i. Create list with inputs from user
#     ii. Determine minimum and maximum elements in the list
#     iii. Insert new element into the list
#     iv. Delete an element from the list
#     v. Determine if an element is present in the list.


print("enter 5 values")
list_a = []
for i in range(0,5):
    list_a.append(int(input()))

print(list_a)

min_a = min(list_a)
print(min_a)

max_a = max(list_a)
print(max_a)

list_a.append(int(input("enter new value")))
print(list_a)

list_a.remove(int(input("which element you wnat to remove")))
print(list_a)

x = int(input("element to search"))
if x in list_a:
    print("yes it exists in list")
else:
    print("notpresent in list")