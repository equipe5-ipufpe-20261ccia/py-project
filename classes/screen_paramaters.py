import pygame

class ScreenParameters:
    def __init__(self , screen_y , screen_x ):
        self.x = screen_x
        self.y = screen_y
    def get_screen_width(self):
        return (self.y , self.x)
