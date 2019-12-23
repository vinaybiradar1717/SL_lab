# 4a. Write a python program to create a class ‘Rectangle’. This class 
# should include a constructor to initialize the dimensions. Include a 
# function in the class to compute the area of the rectangle. 
# Create objects of the class and print area.

class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length*self.breadth

print(Rectangle(3,4).area())
print(Rectangle(5,6).area())