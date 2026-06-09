import pygame
from classes.player import Player

class Enemy:
    def __init__(self):
        self.image_enemy = pygame.image.load("assets/images/Enemy_1.jpg")

        self.enemy_rect = self.image_enemy.get_rect()
        self.enemy_rect.x = 0
        self.enemy_rect.y = 0
        self.enemy_speed = 3
    def update(self , player):

        vector_player = pygame.math.Vector2(player.rect.center)
        vector_enemy = pygame.math.Vector2(self.enemy_rect.center)

        direction_vector = vector_player - vector_enemy

        distance = direction_vector.length()

        if distance > 200:

            vetor_normalize = direction_vector.normalize()

            self.enemy_rect.x += vetor_normalize.x * self.enemy_speed
            self.enemy_rect.y += vetor_normalize.y * self.enemy_speed
        else:
            print("Colision")
    def draw(self, screen):
        screen.blit(self.image_enemy , self.enemy_rect)

