# 12a. Create a Python class called ‘Student’ having ‘name’, ‘age’ 
# as attribute along with a list having the marks obtained for three subjects.  
# (i) Create a constructor to initialize two objects of this class. 
# (ii) Create a member function called ‘display’ printing the details of a specific object 
# (iii) Ask user to enter the values for an object through an ‘accept’ member function. 
# (iv) Display these details.

class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def display(self):
        print("Name: "+self.name)
        print("Age: "+str(self.age))
        print("Marks: "+str(self.marks))

    def accept(self):
        self.name = input("Enter name: "+self.name)
        self.age = int(input("Enter age: "+str(self.age)))
        for i in range(1,4):
            self.marks.append(int(input("Enter marks of subject" +str(i)+" ")))


Student("Vishal",22,[34,45,43]).display()
Stud = Student("","",[])
Stud.accept()
Stud.display()