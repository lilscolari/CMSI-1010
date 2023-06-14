"""
Name: Cameron Scolari
Collaborators: N/A
Date: 10/13/2022
Description: This program implements our own version of the != operator.
"""

a = 3
b = 3
c = 5
d = 6

def not_equal(x, y):
    if x == y:
        return False
    else:
        return True

not_equal_test1 = not_equal(a, b)
print(not_equal_test1)
not_equal_test2 = not_equal(c, d)
print(not_equal_test2)