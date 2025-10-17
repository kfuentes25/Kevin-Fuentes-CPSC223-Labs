from math_operations import *

num1_str = input("Please enter your first number: ")
num2_str = input("Please enter your second number: ")
operation_str = input("Please enter if you would like to add, subtract, multiply, or divide: ")

num1 = float(num1_str)
num2 = float(num2_str)

if operation_str == 'add':
    print(add(num1, num2))
if operation_str == 'subtract':
    print(subtract(num1, num2))

if operation_str == 'multiply':
    print(multiply(num1, num2))

if operation_str == 'divide':
    print(divide(num1, num2))