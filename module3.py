"""
Module 3: Object-Oriented Programming

Basic concepts of object-oriented programming (OOP)
The differences between the procedural and object approaches (motivations and profits)
Classes, objects, properties, and methods;
Designing reusable classes and creating objects;
Inheritance and polymorphism;
Exceptions as objects.


the foundations and basic concepts of object-oriented programming;
the differences between the procedural and object approaches on the example of the stack;
properties (instance and class variables, attributes)
methods (class and object methods, the constructor, parameters, and properties)
the concept of inheritance (functions, methods, class hierarchies, polymorphism, composition, single vs. multiple inheritance)
the objective nature of Python exceptions.

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


