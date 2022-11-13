"""
Module 3: Object-Oriented Programming

Basic concepts of object-oriented programming (OOP)
The differences between the procedural and object approaches (motivations and profits)
Classes, objects, properties, and methods;
Designing reusable classes and creating objects;
Inheritance and polymorphism;
Exceptions as objects.

"""

class Stack:
    def __init__(self):
        self.s = []


    def push(self, num):
        self.s.append(num)

    def pop(self):
        del self.s[-1]


my_stack = Stack()

my_stack.push(5)
my_stack.push(6)
my_stack.pop()
print(my_stack.s)


