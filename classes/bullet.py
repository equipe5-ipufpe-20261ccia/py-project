import pygame
from utils.helpers import Helpers
from utils.collision import check_object_group_collision
from utils.animation import Animation

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.damage = 5
        self.speed = -10
        self.cooldown = 0
        self.bullet_project = pygame.image.load("assets/images/bullet_animation-Sheet.png").convert_alpha()
        self.bullet_animation = Animation(image=self.bullet_project, screen=screen, minimium=0)
        self.bullet_animation.animation_sheet(steps=15, width=32, height=32)
                
        self.image = pygame.Surface((32, 32), pygame.SRCALPHA) 
        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.bottom = y

        self.state = "SPAWN"

    def update(self, enemies, current_time):
        if self.state != "IMPACT":
            self.rect.top += self.speed

            colidiu, inimigo_atingido = check_object_group_collision(self, enemies)
            if colidiu:
                self.state = "IMPACT"
                self.bullet_animation.frame = 6
                if hasattr(inimigo_atingido, 'health'):
                    inimigo_atingido.health -= self.damage

            elif self.rect.bottom < 0:
                self.kill()

        if self.state == "SPAWN":
            self.bullet_animation.update_and_draw(
                current_time, cooldown=100, width=64, height=64, 
                y=self.rect.y, x=self.rect.x, maximium=4, minimium=0
            )
            if int(self.bullet_animation.frame) >= 3:
                self.state = "LOOP"
                self.bullet_animation.frame = 4

        elif self.state == "LOOP":
            self.bullet_animation.update_and_draw(
                current_time, cooldown=100, width=64, height=64, 
                y=self.rect.y, x=self.rect.x, maximium=6, minimium=4
            )

        elif self.state == "IMPACT":
            self.bullet_animation.update_and_draw(
                current_time, cooldown=80, width=64, height=64, 
                y=self.rect.y, x=self.rect.x, maximium=15, minimium=6
            )
            if int(self.bullet_animation.frame) >= 14:
                self.kill()