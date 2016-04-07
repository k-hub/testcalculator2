def add(listc):
    total = 0
    for nums in listc:
        total += float(nums)
    return total


def subtract(listc):
    total = float(listc[0])
    new_list = listc[1:]
    for i in new_list:
        total -= float(i) 
    return total


# def multiply(num1, num2):
#     return num1 * num2


# def divide(num1, num2):
#     # Need to turn at least argument to float for division to
#     # not be integer division
#     return float(num1) / float(num2) 


# def square(num1):
#     # Needs only one argument
#     return num1 * num1


# def cube(num1):
#     # Needs only one argument
#     return num1 * num1 * num1


# def power(num1, num2):
#     return num1 ** num2  # ** = exponent operator


# def mod(num1, num2):
#     return num1 % num2
