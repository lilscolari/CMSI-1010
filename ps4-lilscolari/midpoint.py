"""
Name: Cameron Scolari
Collaborators: N/A
Date: 10/13/2022
Description: This program finds the midpoint of a list.
"""

def midpoint(my_list):
    total = len(my_list)
    if total % 2 == 1:
        mid = int((total / 2) + 1)
    else:
        mid = int(total / 2)
    return mid

list1 = [1, 2]
list2 = [1, 2, 3]

print(midpoint(list1))
print(midpoint(list2))