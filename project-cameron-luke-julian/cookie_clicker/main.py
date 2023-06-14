import pygame
import sys
from Music import Music
from Shop import Shop
from Counter import counterobj

'''
Names: Julian, Luke, Cameron
Date: 12/6/22
Description: Idle pygame, click the cookie to earn cookies, spend on upgrades to increase your cookie income. See README for more.
'''

'''
What to do:
- Add $ amount after shop items. (make each purchase cost more) done
- Add class for each shop item to reuse code? done
- button to pause and play music (maybe a slider to control volume)
- add controls information tab done
- add more idle shop items done
- make functions to condense code done
- add achievements
'''

pygame.init()

Music.backround_music(3)  # Plays backround music

size = width, height = 1550, 805  # Display variables
background = 0, 255, 100

screen = pygame.display.set_mode(size)  # Creating screen and window caption
pygame.display.set_caption("Cookie Clicker")
clock = pygame.time.Clock()

cookie = pygame.image.load('cookie.png')  # Creating rectangles for regular and big cookies
big_cookie = pygame.transform.rotozoom(cookie, 0, 1.1)
big_cookie_rect = big_cookie.get_rect()
big_cookie_rect.center = (210, 410)
cookie_rect = cookie.get_rect()
cookie_rect.x = 50
cookie_rect.y = 250

font = pygame.font.Font('freesansbold.ttf', 32)  # Initializing fonts
font2 = pygame.font.Font('freesansbold.ttf', 26)
font3 = pygame.font.Font('freesansbold.ttf', 54)

winner_text = font3.render('WINNER WINNER CHICKEN DINNER!', True, (0, 0, 0), background)  # Endscreen text1
winner_rect = winner_text.get_rect()
winner_rect.center = (775, 402.5)

extra_text = font2.render('(click to continue playing)', True, (0, 0, 0), (0, 255, 0))  # Endscreen text2
extraRect = extra_text.get_rect()
extraRect.center = (775, 475)

amount_text = font2.render('amount    cost', True, (0, 0, 0), background)  # Displays column headers
amountRect = amount_text.get_rect()
amountRect.topleft = (1000, 100)

pressed = False  # True if mouse is pressed on cookie
win = False  # False is player hasn't won

timer = 0  # Timer for idle income

item1 = Shop(100, 25, "click upgrade (+1 cookies)")  # Creating objects for upgrades
item2 = Shop(90, 100, "grandma (+5 idle cookies)")
item3 = Shop(80, 500, "cookie farm (+25 idle cookies)")
item4 = Shop(70, 2500, "cookie factory (+125 idle cookies)")
item5 = Shop(60, 12500, "cookie warehouse (+500 idle cookies)")
item6 = Shop(50, 50000, "cookie dispensary (+2500 idle cookies)")
item7 = Shop(40, 250000, "cookie plantation (+12500 idle cookies)")
item8 = Shop(30, 1000000, "cookie planet (+50000 idle cookies)")
item9 = Shop(20, 5000000, "cookie galaxy (+500000 idle cookies)")
item10 = Shop(10, 500000000, "cookie universe (+1000000 idle cookies)")
item11 = Shop(1, 10000000000, "THE FINAL COOKIE!!!")

while True:  # Game loop

    timer += 1  # Tick rate for idle cookies
    while timer > 15:
        counterobj.counter += counterobj.idle_multiplier
        timer -= 15

    if item11.amount == 1:  # Updates win condition
        win = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()  # Closes window if user exits

        if event.type == pygame.MOUSEBUTTONDOWN and cookie_rect.collidepoint(pygame.mouse.get_pos()):  # Incriments cookies when big cookie is pressed
            pressed = True
            counterobj.counter += 1 * counterobj.counter_multiplier

        item1.draw_rect((1100, 125), (1125, 125))  # Draws 2 colored rectangles that changes color conditionally for each upgrade
        item2.draw_rect((1100, 175), (1125, 175))
        item3.draw_rect((1100, 225), (1125, 225))
        item4.draw_rect((1100, 275), (1125, 275))
        item5.draw_rect((1100, 325), (1125, 325))
        item6.draw_rect((1100, 375), (1125, 375))
        item7.draw_rect((1100, 425), (1125, 425))
        item8.draw_rect((1100, 475), (1125, 475))
        item9.draw_rect((1100, 525), (1125, 525))
        item10.draw_rect((1100, 575), (1125, 575))
        item11.draw_rect((1100, 625), (1125, 625))

        if event.type == pygame.MOUSEBUTTONDOWN:  # Calls buy_update on all items
            item1.buy_update(1)
            item2.buy_update(5)
            item3.buy_update(25)
            item4.buy_update(125)
            item5.buy_update(500)
            item6.buy_update(2500)
            item7.buy_update(12500)
            item8.buy_update(50000)
            item9.buy_update(250000)
            item10.buy_update(1000000)
            item11.buy_update(0)

    counterobj.update_counter()  # Updates counter object with several variables

    pygame.mouse.set_cursor(*pygame.cursors.arrow)  # Sets your cursor to cool pixel cursor

    screen.fill(background)  # Fills the screen the color of backround (green)
    screen.blit(cookie, cookie_rect)  # Draws big cookie
    screen.blit(amount_text, amountRect)  # Draws amount and cost
    screen.blit(item1.text, item1.rect)  # Draws each upgrade, the amount you have, and the cost
    screen.blit(item1.text2, item1.rect2)
    screen.blit(item2.text, item2.rect)
    screen.blit(item2.text2, item2.rect2)
    screen.blit(item3.text, item3.rect)
    screen.blit(item3.text2, item3.rect2)
    screen.blit(item4.text, item4.rect)
    screen.blit(item4.text2, item4.rect2)
    screen.blit(item5.text, item5.rect)
    screen.blit(item5.text2, item5.rect2)
    screen.blit(item6.text2, item6.rect2)
    screen.blit(item6.text, item6.rect)
    screen.blit(item7.text2, item7.rect2)
    screen.blit(item7.text, item7.rect)
    screen.blit(item8.text2, item8.rect2)
    screen.blit(item8.text, item8.rect)
    screen.blit(item9.text2, item9.rect2)
    screen.blit(item9.text, item9.rect)
    screen.blit(item10.text2, item10.rect2)
    screen.blit(item10.text, item10.rect)
    screen.blit(item11.text2, item11.rect2)
    screen.blit(item11.text, item11.rect)
    screen.blit(counterobj.text, counterobj.TextRect)  # Draws how many cookies you have

    if pressed:
        screen.blit(big_cookie, big_cookie_rect)  # Makes cookie bigger when pressed
        Music.cookie_noise(3)  # Plays sound effect
        pressed = False

    if item11.amount == 1 and win:  # Displays end screen text if the player has won
        screen.fill(background)
        screen.blit(winner_text, winner_rect)
        screen.blit(extra_text, extraRect)

        if event.type == pygame.MOUSEBUTTONDOWN and extraRect.collidepoint(pygame.mouse.get_pos()):
            item11.amount = 0
            win = False  # If user continues playing, makes win = True unobtainable and brings them back to the game
            screen.fill(background)  # Redraws everything from above
            screen.blit(cookie, cookie_rect)
            screen.blit(amount_text, amountRect)
            screen.blit(item1.text, item1.rect)
            screen.blit(item1.text2, item1.rect2)
            screen.blit(item2.text, item2.rect)
            screen.blit(item2.text2, item2.rect2)
            screen.blit(item3.text, item3.rect)
            screen.blit(item3.text2, item3.rect2)
            screen.blit(item4.text, item4.rect)
            screen.blit(item4.text2, item4.rect2)
            screen.blit(item5.text, item5.rect)
            screen.blit(item5.text2, item5.rect2)
            screen.blit(item6.text2, item6.rect2)
            screen.blit(item6.text, item6.rect)
            screen.blit(item7.text2, item7.rect2)
            screen.blit(item7.text, item7.rect)
            screen.blit(item8.text2, item8.rect2)
            screen.blit(item8.text, item8.rect)
            screen.blit(item9.text2, item9.rect2)
            screen.blit(item9.text, item9.rect)
            screen.blit(item10.text2, item10.rect2)
            screen.blit(item10.text, item10.rect)
            screen.blit(item11.text2, item11.rect2)
            screen.blit(item11.text, item11.rect)
            screen.blit(counterobj.text, counterobj.TextRect)

    pygame.display.flip()  # Updates display surface to screen
    clock.tick(60)  # Sets fps to 60

    pygame.display.update()  # Updates display
