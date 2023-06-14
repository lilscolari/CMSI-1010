"""
Name: Cameron Scolari
Date: 10/27/2022
Description: This is a Dice game. It has two classes: Die and DiceSet.
"""
from random import randint

"""
####### Die Class: ######
A simple class for representing die objects. A die has a given number of
sides (at least) four, set when the die is constructed and which can never
be changed. The die's value can be changed, but only by calling its roll()
method.
"""

class Die():

    # Constructs a die with the given starting value and number of sides.
    def __init__(self, initial_value, sides):
        self.initial_value = initial_value
        self.sides = sides

    """
    Simulates a roll by randomly updating the value of this die. 
    In addition to mutating the die's value, this method also 
    returns the new updated value.
    """

    def roll(self):
        self.initial_value = randint(1, self.sides)
        return self.initial_value

    # Returns the number of sides of this die.
    def get_number_sides(self):
        return self.sides

    # Returns the current value of this die.
    def get_current_value(self):
        return self.initial_value

    """
    Returns a string representation of this die, which is its value enclosed in square
    brackets, without spaces, for example "[5]".
    """

    def __str__(self):
        output = str('[' + str(self.initial_value) + ']')
        return output

"""
####### DiceSet Class: ######
A dice set holds a collection of Die objects. All of the die objects have
the same number of sides. 
"""

class DiceSet():
    """
    Creates a DiceSet containing the given number of dice, each with the 
    given number of sides. All die values start off as 1.
    """

    def __init__(self, sides_each_die, number_of_dice):
        self.sides_each_die = sides_each_die
        self.number_of_dice = number_of_dice

    """
    Returns the descriptor of the dice set; for example "5d20" for a set with
    five dice of 20 sides each; or "2d6" for a set of two six-sided dice.
    """

    def get_descriptor(self):
        output2 = str(str(self.number_of_dice) + 'd' + str(self.sides_each_die))
        return output2

    # Returns the total of the values of each die in the set.
    def get_total(self):
        total = 0
        count1 = 0
        for val in range(0, self.number_of_dice):
            count1 += 1
            total += list_of_die[count1][0]
        return total

    # Rolls all the dice in the set.
    def roll_all(self):
        for val in range(1, self.number_of_dice + 1):
            var = new_die.roll()
            list_of_die[val] = var, num1

    # Rolls the i-th die, updating its value.
    def roll_die(self, i):
        if i in list_of_die:
            new_val = new_die.roll()
            list_of_die[i] = new_val, num1
        else:
            pass

    # Returns the values of each of the dice in a list.
    def get_current_values(self):
        new_list = []
        for val in list_of_die:
            new_list.append(list_of_die[val][0])
        return new_list

    """
    Returns a string representation in which each of the die strings are
    joined without a separator, for example: "[2][5][2][3]".
    """

    def matches(self, dice_set):
        counter = 0
        if dice_set.number_of_dice == len(list_of_die):
            if dice_set.sides_each_die == list_of_die[1][1]:
                for val in range(1, len(list_of_die) + 1):
                    if list_of_die[val][0] in dice_set.get_current_values():
                        counter += 1
                    else:
                        pass
            else:
                pass
        else:
            pass
        if counter == len(list_of_die):
            print('true')
        else:
            print('false')

    def __str__(self):
        new_string = ""
        for val in range(1, self.number_of_dice + 1):
            new_die2 = Die(list_of_die[val][0], num1)
            part = new_die2.__str__()
            new_string += part
        return new_string

""" 
####### Main Program: ######
The program should begin by printing a welcome message. 
Then it repeatedly asks the user to enter a command and carries
it out. Each command will either print a response or an error 
message, followed by a blank line.
"""
list_of_die = {}
game = False
while not game:
    print("\nWelcome to the dice game!")
    enter = str(input("Please input a command: "))
    if enter == "h" or enter == 'help':
        print("\nHere is a list of commands:\n"
              "q or quit: Quits the program, but prints a nice message before just before quitting."
              "\n\nuse <s> <n> : Obtain a new set of dice. Here <n> is the number of dice, which must "
              "be \nbetween 2 and 99; and <s> is the number of sides for each die in the set, which must "
              "be \nbetween 4 and 99. Prints the descriptor of dice set just obtained and the dice set too."
              "\n\nroll all: Rolls all the dice, then prints the dice set.\n\nroll <i>: Rolls the i-th die in "
              "the set, then prints the dice set.\n\nhigh or highest: Prints the highest roll so far.\n")
    elif enter == 'q' or enter == 'quit':
        print("Thanks for playing the game. The Program is now quitting...")
        game = True

    elif enter == "roll all":
        print(list_of_die)
        new_set.roll_all()
        print(list_of_die)

    elif enter[0:3] == 'use':
        if enter[6] == " ":
            num1 = enter[4:6]
            if len(enter) > 8:
                num2 = enter[7:9]
            else:
                num2 = enter[7:8]
        else:
            num1 = enter[4:5]
            if len(enter) > 7:
                num2 = enter[6:8]
            else:
                num2 = enter[6:7]
        num1 = int(num1)
        num2 = int(num2)
        if num2 in range(2, 100) and num1 in range(4, 100):
            new_set = DiceSet(num1, num2)
            print("Descriptor for Dice Set: " + new_set.get_descriptor())
            i = 1
            count = 0
            list_of_die = {}
            for amount in range(0, num2):
                count += 1
                initial_value = 1
                new_die = Die(initial_value, num1)
                list_of_die[count] = initial_value, num1
            print(list_of_die)
        else:
            print("\nThose are not valid inputs!\n")
            i = 1

    elif enter == "high" or enter == "highest":
        max_num = 0
        for num in list_of_die:
            if int(list_of_die[num][0]) > max_num:
                max_num = int(list_of_die[num][0])
            else:
                pass
        print(max_num)

    elif enter[0:4] == "roll" and (len(enter) == 6 or len(enter) == 7):
        if len(enter) > 6:
            num3 = enter[5:7]
        else:
            num3 = enter[5:6]
        num3 = int(num3)
        new_set.roll_die(num3)
        print(list_of_die)

    else:
        print("I don't understand, type 'h' or 'help' for a list of commands.")