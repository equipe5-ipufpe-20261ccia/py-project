import pygame
from utils.helpers import Helpers
from utils.collision import check_object_group_collision
# pygame.sprite.Sprite because of practicity of kill() function for bullets
class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.damage = 5
        self.speed = -10
        self.cooldown = 0
        self.image = Helpers("assets/images/bullet_sprite_valido.png", 10, 20).get_proporsion()
        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.bottom = y


    def effect(self):
        pass

    def update(self, enemies):
        self.rect.top += self.speed

        if self.rect.bottom < 0 or (check_object_group_collision(self, enemies)[0]):
            self.kill()

# Subclass of bullet, will be used to make a special shot that costs player.energy
class SpecialBullet(Bullet):
    def __init__(self, x, y):
        super().__init__()
        self.damage = 20
        self.speed = -7
        self.cooldown = 2
        self.image = Helpers("assets/images/bullet_sprite_valido.png", 20, 40).get_proporsion()
        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.bottom = y

        self.speed = -7
    def effect(self, enemies):
        pass
        # Idea is to make a "burning" or "freezing" effect, making the boss
        # lose health for an amout of time, like a poison effect
    def update(self, enemies):
        self.rect.top += self.speed

        if self.rect.bottom < 0:
            self.kill()