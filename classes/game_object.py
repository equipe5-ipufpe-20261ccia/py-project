import pygame
import random
from utils.collision import check_collision

# General class of collectables. can be collected and are stored in the player class
class Collectable():
    def __init__(self, image, width=30, height=30):
        self.limit = None
        self.range_x = (50, 750)
        self.range_y = (200, 500)
        self.image_collectable = pygame.image.load(image)
        self.image_collectable = pygame.transform.scale(self.image_collectable, (width, height))

        self.x = random.randint(self.range_x[0], self.range_x[1])
        self.y = random.randint(self.range_y[0], self.range_y[1])

        self.rect = self.image_collectable.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def get_position(self):
        return (self.rect.x , self.rect.y)

    # Differents effects for differemts collectables

    def effect(self, player):
        pass

    def draw(self, screen, player):
        if not check_collision(player, self):
            screen.blit(self.image_collectable, self.rect)
        else:
            self.effect(player)

            # have to put an if to stop object from respawning in the same place

            self.rect.x = random.randint(self.range_x[0], self.range_x[1])
            self.rect.y = random.randint(self.range_x[0], self.range_x[1])

# Types of collectibles
class Heart(Collectable):
    def __init__(self):
        super().__init__("assets/images/heart_sprite_valido.png")
        self.range_x = (30, 750)
        self.range_y = (100, 400)
    def effect(self, player):
        player.health += 10
        player.get_health()
        print(f"Voce coletou 10 de vida, vida atual: {player.health}")

class Potion(Collectable):
    def __init__(self):
        super().__init__("assets/images/green_potion_sprite.png")
        self.range_x = (30, 750)
        self.range_y = (100, 400)
    def effect(self, player):
        player.speed += 1
        player.get_speed()
        print(f"Voce coletou 1 de speed, speed atual: {player.speed}")


# Battery will work as a charge attack, when full will release a BIG SHOT
class Battery(Collectable):
    def __init__(self):
        super().__init__("assets/images/coin_test.png")
        self.range_x = (30, 750)
        self.range_y = (100, 400)
    def effect(self, player):
        player.energy += 1
        player.get_energy()
