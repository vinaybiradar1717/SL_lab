class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name: "+self.name)
        print("Age: "+str(self.age))
        print("marks: "+str(self.marks))
    
    def accept(self):
        self.name = input("Enter name: ")
        self.age = input("Enter age: ")
        for i in range(1,4):
            self.marks.append(int(input("Enter marks of subject "+str(i))))


Student("Akbar",22,[45,42,39]).display()
Student("Rahul",21,[36,44,47]).display()

Stud = Student("","",[])
Stud.accept()
Stud.display()