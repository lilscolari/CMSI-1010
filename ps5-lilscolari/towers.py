"""
Name:
Collaborators:
Date:
Description:
"""


def print_all_rods():
    global rod_left
    global rod_middle
    global rod_right
    print(rod_left, rod_middle, rod_right)


class Rod(object):
    def __init__(self, name, elements):
        self.name = name
        self.elements = elements
        
    def __str__(self):
        result = self.name + ': (bottom) '
        for element in self.elements:
            result += str(element) + ' '

        result += '(top)'
        return result
    
    def take_off_top_disk(self):
        ## YOUR CODE HERE to replace pass
        pass
        
    def add_disk(self, num):
        ## YOUR CODE HERE to replace pass
        pass


def move_one_disk(curr_rod, new_rod):
    ## YOUR CODE HERE to replace pass
    pass


def hanoi(num, source_rod, helper_rod, target_rod):
    ## ADD YOUR CODE HERE to replace pass
    ## step a: Move n - 1 disks from source to helper
    ## step b: Move disk n from source to target, then call print_all_rods
    ## step c: move n - 1 disks from helper to target
    pass


## Let's try out and test our program!
num_disks = 4
disks = list(range(num_disks, 0, -1))
rod_left = Rod('ROD_LEFT', disks)
rod_middle = Rod('ROD_MIDDLE', [])
rod_right = Rod('ROD_RIGHT', [])
hanoi(num_disks, rod_left, rod_middle, rod_right)
