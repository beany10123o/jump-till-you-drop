import pygame

pygame.display.set_caption('hello')

screen=pygame.display.set_mode((100, 100))

while True:
    screen.fill((0, 255, 0))
    pygame.display.flip()