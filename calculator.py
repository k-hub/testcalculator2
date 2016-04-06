"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True: #starting while loop
    input = raw_input('> ') #have user enter an operator and two numbers
    output = input.split(' ') #split will 
    operator = output[0] #operator will determine what function to use in arithmetic.py
    num1 = int(output[1]) # input in str, need to convert str to int
    num2 = int(output[2])
    
    if operator == '+':
        print add(num1, num2)
    elif operator == '-':
        print subtract(num1, num2)
    elif operator == '*':
        print multiply(num1, num2)
    elif operator == '/':
        print divide(num1, num2)