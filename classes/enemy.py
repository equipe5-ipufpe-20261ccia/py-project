import pygame
from classes.player import Player
from utils.collision import check_collision


class Enemy:
    def __init__(self):
        
        self.image_enemy = pygame.image.load("assets/images/Enemy_1.jpg")
        self.image_enemy = pygame.transform.scale(self.image_enemy , (100 , 100))

        self.rect = self.image_enemy.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.enemy_speed = 3
    def update(self , player):
        if check_collision(player, self)==False:
            vector_player = pygame.math.Vector2(player.rect.center)
            vector_enemy = pygame.math.Vector2(self.rect.center)

            direction_vector = vector_player - vector_enemy

            distance = direction_vector.length()

            vetor_normalize = direction_vector.normalize()

            self.rect.x += vetor_normalize.x * self.enemy_speed
            self.rect.y += vetor_normalize.y * self.enemy_speed

    def get_position(self):
        return (self.rect.x , self.rect.y)
    def draw(self, screen, player):
        if check_collision(player, self) == False:
            screen.blit(self.image_enemy , self.rect)
        else:
            player.vida -= 1
            print(f"diminuiram minha aura , aura atual {player.vida}")
            self.rect.x = 0
            self.rect.y = 0