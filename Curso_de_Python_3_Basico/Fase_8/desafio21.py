#from pygame import mixer

#mixer.init() 

#mixer.music.load('music.mp3')

#mixer.music.play()

#parar = input('Digite algo para parar...')

import pygame 

pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
pygame.event.wait()
