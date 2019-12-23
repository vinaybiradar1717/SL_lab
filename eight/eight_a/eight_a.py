# 8a 
# (i) Create a dictionary that contains the atomic element symbol and its name. 
# (ii)Add a unique & duplicate element into this dictionary by interacting with the user. Observe the output and justify it. 
# (iii) Display the number of atomic elements in this dictionary 
# (iv) Ask user to enter an element to search in the dictionary. Display appropriate results. 

dictionary = {
    "Iron": "Fe",
    "Carbon": "C",
    "Neon": "Ne",
    "Silicon": "Si"
}
#print(dictionary)

name = input("Enter the atomic name: ")
symbol = input("Enter the atomic symbol: ")
dictionary[name] = symbol
#print(dictionary)

print(len(dictionary))

search = input("Enter the element that you want to search: ")
if search in dictionary:
    print("Element present ")
    print(search," ",dictionary[search])
else:
    print("Element not present in dictionary.")