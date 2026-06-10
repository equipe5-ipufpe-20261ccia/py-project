import pygame

class Helpers:
    def __init__(self , ima , x , y):
        self.image = pygame.image.load(ima)
        self.image = pygame.transform.scale(self.image, (x, y))
    def get_proporsion(self):
        return self.image

