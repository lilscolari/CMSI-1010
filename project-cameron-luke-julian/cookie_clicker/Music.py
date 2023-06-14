import pygame

'''
Names: Julian, Luke, Cameron
Date: 12/6/22
Description: Music class provides audio for game music and button sounds.
'''


class Music:
    def __init__(self, channels):  # Default constructor
        self.channels = channels
        pygame.mixer.set_num_channels(channels)  # Creates Channels, set to 3 in main

    def button_click(self):  # Plays button sound
        button_click = pygame.mixer.Sound("button_click.mp3")  # Assigns mp3 file to button_click()
        button_click.set_volume(0.5)  # Sets volume
        pygame.mixer.Channel(2).play(button_click)  # Loads sound in channel 2

    def backround_music(self):  # Backround game music
        background_music = pygame.mixer.Sound("background_music.mp3")  # Assigns mp3 file to backround_music()
        background_music.set_volume(0.07)  # Sets volume
        pygame.mixer.Channel(0).play(background_music, -1)  # Loads sound in channel 0 and loops when finished

    def cookie_noise(self):  # Sound when cookie is clicked
        cookie_noise = pygame.mixer.Sound("cookie_noise.mp3")  # Assigns mp3 file to cookie_noise()
        cookie_noise.set_volume(0.4)  # Sets volume
        pygame.mixer.Channel(1).play(cookie_noise)  # Loads sound in channel 1
