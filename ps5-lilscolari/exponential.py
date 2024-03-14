"""
Name: Cameron Scolari
Collaborators: N/A
Date: 10/20/2022
Description: This program writes our own _recursive_ version of exponential, **
"""

# TODO: Return the value of base ** exp, using recursion instead of a loop!
def exponential(base, exp):
    value = 1
    if exp < 0:
        raise ValueError("'exp' variable cannot have a negative value")
    elif exp == 0:
        return value
    else:
        value = base * exponential(base, exp - 1)
        return value

# TODO: ask for user input, then call the exponential function
base_answer = eval(input('Enter a number for the base: '))
exp_answer = eval(input('Enter a positive number for the exponent: '))

exponential(base_answer, exp_answer)
print(exponential(base_answer, exp_answer))