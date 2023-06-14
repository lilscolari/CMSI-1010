import pygame
import time
from Music import Music
from Counter import counterobj

'''
Names: Julian, Luke, Cameron
Date: 12/6/22
Description: Shop class used for creating shop objects. Contains methods to update the color of rectangles,
and updates variables like cost and amount for each object.
'''

pygame.init()

size = width, height = 1550, 805  # Displays screen
screen = pygame.display.set_mode(size)

green = (0, 100, 25)  # Color variables
red = (200, 0, 0)
black = (0, 0, 0)


class Shop:
    def __init__(self, limit, cost, name):  # Default constructor, used to create shop objects.
        self.limit = limit
        self.cost = cost
        self.amount = 0
        self.font2 = pygame.font.Font('freesansbold.ttf', 26)  # Font for display
        self.name = name
        self.display = str(name + '                  ' + str(self.amount))  # Parses name and amount to string for display
        self.display2 = str(self.cost)  #  Parses cost to display

    def draw_rect(self, pos, pos2):  # Draws rectangles for cost and amount at different positions declared in main
        self.pos = pos
        self.pos2 = pos2
        if counterobj.counter >= self.cost and self.amount < self.limit:  # If you can purchase upgrade it is green
            self.text = self.font2.render(self.display, True, black, green)
            self.rect = self.text.get_rect()
            self.rect.topright = (self.pos)
            self.text2 = self.font2.render(self.display2, True, black, green)
            self.rect2 = self.text.get_rect()
            self.rect2.topleft = (self.pos2)
        else:
            self.text = self.font2.render(self.display, True, black, red)  # If you don't have enough cookies the upgrade is red
            self.rect = self.text.get_rect()
            self.rect.topright = (self.pos)
            self.text2 = self.font2.render(self.display2, True, black, red)
            self.rect2 = self.text.get_rect()
            self.rect2.topleft = (self.pos2)

    def buy_update(self, multiplier):  # Updates variables for click upgrade
        self.display = str(self.name + '                  ' + str(self.amount))  # Displays name and amount
        self.multiplier = multiplier
        if self.rect.collidepoint(pygame.mouse.get_pos()) and self.amount < self.limit:  # If upgrade is clicked
            if counterobj.counter >= self.cost:  # If more cookies than upgrade, you will purchase it
                counterobj.counter -= self.cost  # Subtracts cookies from total
                if self.limit == 100:
                    counterobj.counter_multiplier += self.multiplier  # Updates amount per click
                else:
                    counterobj.idle_multiplier += self.multiplier  # Updates idle income
                self.amount += 1  # Increments amount by 1
                self.display = str(self.name + '                  ' + str(self.amount))  # Displays name and new amount
                Music.button_click(3)  # Calls button_click()
                time.sleep(0.01)
                self.cost += int(((1 / 9) * self.cost) + 1)  # Linear function, increments cost of upgrade after each purchase
                self.display2 = str(self.cost)  # displays cost of upgrade
