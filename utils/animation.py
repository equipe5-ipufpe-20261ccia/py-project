import pygame
from utils.spritesheet import SpriteSheet

class Animation():
    def __init__(self, image, screen, minimium):
        self.image_sheet = image
        self.image_sprite_sheet = SpriteSheet(self.image_sheet)
        self.screen = screen

        self.title_animation = []
        self.frame = minimium
        self.last_update = 0

    def animation_sheet(self, steps, width, height):
        self.title_animation = []
        for x in range(steps):
            self.title_animation.append(self.image_sprite_sheet.get_image(x, width, height, 1))

    def update_and_draw(self, current_time, cooldown, width, height, x, y, maximium, minimium):
        if current_time - self.last_update >= cooldown:
            self.frame += 1
            self.last_update = current_time
            if self.frame >= maximium:
                self.frame = minimium

        if int(self.frame) >= len(self.title_animation):
            self.frame = minimium

        current_frame_image = self.title_animation[int(self.frame)]
        scaled_image = pygame.transform.scale(current_frame_image, (width, height))
        self.screen.blit(scaled_image, (x, y))