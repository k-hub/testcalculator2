"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True: #starting while loop
    input = raw_input('> ') #have user enter an operator and two numbers
    output = input.split(' ') #split will 
    if len(output) == 2:
        operator = output[0] #operator will determine what function to use in arithmetic.py
        try:
            num1 = float(output[1]) # input in str, need to convert str to int
        except:
            print "You did not enter an integer. Please enter an integer."
            continue


    elif len(output) == 3:
        operator = output[0]
        num1 = float(output[1])
        num2 = float(output[2])
    
    if operator == '+':
        print add(num1, num2)
    elif operator == '-':
        print subtract(num1, num2)
    elif operator == '*':
        print multiply(num1, num2)
    elif operator == '/':
        print divide(num1, num2)
    elif operator == 'square':
        print square(num1)
    elif operator == 'cube':
        print cube(num1)
    elif operator == 'pow':
        print power(num1, num2)
    elif operator == 'mod':
        print mod(num1, num2)