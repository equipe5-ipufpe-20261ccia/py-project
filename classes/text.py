import pygame

from constants import FONT_SIZE, FONT_STYLE, WHITE


# Used in the making of Menu and Hud
class Text():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = FONT_SIZE
        self.color = WHITE
        self.style = FONT_STYLE
    
    def display(self, screen, content):
        font = pygame.font.SysFont(self.style, self.size)

        text_surface = font.render(content, False, self.color)
        screen.blit(text_surface, (self.x, self.y))
