import pygame
from utils.collision import check_collision, check_object_group_collision

# pygame.sprite.Sprite because of practicity of killing and grouping enemies
class Enemy(pygame.sprite.Sprite):

    def __init__(self, image):
        super().__init__()
        self.health = 5
        self.damage = 4
        self.fire = False

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.enemy_speed = 3

    def IsBurning(self):
        if self.fire:
            self.health -= 3

    # Centralizamos TODA a lógica de jogo no update
    def update(self, player, bullets):
        if not check_collision(player, self):
            vector_player = pygame.math.Vector2(player.rect.center)
            vector_enemy = pygame.math.Vector2(self.rect.center)
            direction_vector = vector_player - vector_enemy

            if direction_vector.length() > 0:
                vector_normalize = direction_vector.normalize()
                self.rect.x += vector_normalize.x * self.enemy_speed
                self.rect.y += vector_normalize.y * self.enemy_speed

        if check_collision(player, self):
            player.health -= self.damage
            player.get_health()
            print(f"Current health is: {player.health}")
            self.rect.x = 0
            self.rect.y = 0

        elif check_object_group_collision(self, bullets)[0]:
            while self.health > 0:
                self.health -= check_object_group_collision(self, bullets)[1].damage
                self.IsBurning()
                print(f"{self.health}")
            self.rect.x = 0
            self.rect.y = 0

    def get_position(self):
        return (self.rect.x, self.rect.y)