import pygame

'''
Names: Julian, Luke, Cameron
Date: 12/6/22
Description: Counter class to keep track of variables as the game progresses.
'''

pygame.init()

background = 0, 255, 100  # Backround color
size = width, height = 1550, 805  # Size variable
screen = pygame.display.set_mode(size)  # Screen variable


class Counter:

    def __init__(self, counter, counter_multiplier, idle_multiplier, font):  # Constructor, initializes variables
        self.counter = counter
        self.counter_multiplier = counter_multiplier
        self.idle_multiplier = idle_multiplier
        self.font = font

    def update_counter(self):  # Shortens notation by using M/Millions, B/ Billions, etc... until scientific notation
        counter = str(self.counter)  # parses to string
        if len(counter) < 7:
            new_counter = counter[0:len(counter)]  # If digits < 7 no notation
            counter_display = str('cookie count: ' + str(new_counter))
            self.text = self.font.render(counter_display, True, (255, 255, 255), background)
            self.TextRect = self.text.get_rect()
            self.TextRect.center = (200, 600)
        elif 6 < len(counter) < 10:
            new_counter = counter[0:len(counter) % 6] + 'M'  # Adds M if in millions
            counter_display = str('cookie count: ' + str(new_counter))
            self.text = self.font.render(counter_display, True, (255, 255, 255), background)
            self.TextRect = self.text.get_rect()
            self.TextRect.center = (200, 600)
        elif 9 < len(counter) < 13:
            new_counter = counter[0:len(counter) % 9] + 'B'  # Adds B if in billions
            counter_display = str('cookie count: ' + str(new_counter))
            self.text = self.font.render(counter_display, True, (255, 255, 255), background)
            self.TextRect = self.text.get_rect()
            self.TextRect.center = (200, 600)
        elif 12 < len(counter) < 16:
            new_counter = counter[0:len(counter) % 12] + 'T'  # Adds T if in trillions
            counter_display = str('cookie count: ' + str(new_counter))
            self.text = self.font.render(counter_display, True, (255, 255, 255), background)
            self.TextRect = self.text.get_rect()
            self.TextRect.center = (200, 600)
        elif 15 < len(counter) < 19:
            new_counter = counter[0:len(counter) % 15] + 'Q'  # Adds Q if in quadrillions
            counter_display = str('cookie count: ' + str(new_counter))
            self.text = self.font.render(counter_display, True, (255, 255, 255), background)
            self.TextRect = self.text.get_rect()
            self.TextRect.center = (200, 600)
        else:
            new_counter = counter[0:len(counter) % 19 + 1] + 'aa'  # Adds aa after quadrillions
            counter_display = str('cookie count: ' + str(new_counter))
            self.text = self.font.render(counter_display, True, (255, 255, 255), background)
            self.TextRect = self.text.get_rect()
            self.TextRect.center = (200, 600)

        self.counter = int(counter)
        screen.blit(self.text, self.TextRect)


counterobj = Counter(0, 1, 0, pygame.font.Font('freesansbold.ttf', 32))
