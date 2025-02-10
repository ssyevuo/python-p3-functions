#!/usr/bin/env python3

#greet programmer function
def greet_programmer():
    print("Hello, programmer!")

greet_programmer()

#pass a name Guido
def greet(name):
    print(f"Hello, {name}!")

greet("Guido")

#greeting with a default parameter
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()

#add two numbers i.e 45 and 55
def add(num1, num2):
    return num1 + num2
add(45, 55)

#halves a number i.e divide 100 by 2
def halve(number):
    return number/2
halve(100)
