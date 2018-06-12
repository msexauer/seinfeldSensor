import pygame
import random
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

irIn = 17

GPIO.setup(irIn, GPIO.IN)

pygame.mixer.init()

while True:

    senActive = GPIO.input(irIn)

    if senActive:
        number = random.randint(1, 10)
        print(number)

        testSound = pygame.mixer.Sound('./audio/seinfeld' + str(number) + '.wav')
        testSound.play()

        time.sleep(7)
    else:
        print('nothing yet')

    #So our code isn't burning itself up in a quick loop
    time.sleep(.1)
