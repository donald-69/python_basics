from python_classes2 import Cylinder


from student import Student


class Person:
    def __init__(self, name, age): #constructor
        print("Creating a person")
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old. ")

p1= Person("Jack",19) #p1 == object ==variable
p2 = Person("Mary",21)
p3 = Person("Zack",99)

p1.say_hello()
p2.say_hello()
p3.say_hello()

#objects = data + functions
name = "Chan"
name.upper()

#data
c1 = Cylinder(10, 32)
c2 = Cylinder(76.4, 25)

#functions
c1.area()
c1.volume()
c1.print_details()



std1 = Student("John Doe" , "20/4/2005", "Male")

std1.print_details()
std1.calculate_age()
