import imp


import pygame, os

working_path = os.path.dirname(os.path.join(os.path.dirname(__file__), "..", ".."))

class Sprite:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.position = (0, 0)
        self.image = pygame.image.load
    
    def draw_on(self, screen):
        screen.blit(self.image, self.position)
