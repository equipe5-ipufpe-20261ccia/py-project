import pygame
from classes.screen_paramaters import ScreenParameters

class Player:
    def __init__(self):
        #declarando as imagens do jogador
        self.image_left = pygame.image.load("assets/images/Low_tier_god.jpg")
        self.image_right = pygame.image.load("assets/images/Low_tier_god2.jpg")
        self.image_high = pygame.image.load("assets/images/Low_tier_god3.jpg")
        self.image_down = pygame.image.load("assets/images/Low_tier_god4.jfif")
        #declarando a posição inicial e o tamanho do retangulo

        self.image_present = self.image_left
        self.rect = self.image_present.get_rect()
        self.rect.x = 200
        self.rect.y = 200
        self.speed = 5
    def get_position(self):
        return (self.rect.x, self.rect.y)
    def movement(self):

        # verifica se a tecla esta sendo pressionada
        # O comando .get_pressed() , verifica se a tecla esta precionada
        key = pygame.key.get_pressed()

        mov_x = 0
        mov_y = 0

        # verifica as teclas precionadas

        if key[pygame.K_LEFT]:
            mov_x = -1
            self.image_present = self.image_left

        if key[pygame.K_RIGHT]:
            mov_x = 1
            self.image_present = self.image_right

        if key[pygame.K_UP]:
            mov_y = -1
            self.image_present = self.image_down

        if key[pygame.K_DOWN]:
            mov_y = 1
            self.image_present = self.image_down

        # verificando se a pessoa quer andar na diagonal e a movimentação nao ficar esquisita

        current_speed = self.speed

        if mov_x != 0 and mov_y != 0:
            current_speed = self.speed * 0.7
            # atualiza a posição

        self.rect.x += mov_x * current_speed
        self.rect.y += mov_y * current_speed

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > 800:
            self.rect.right = 800

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > 600:
            self.rect.bottom = 600
    def update(self):
        self.movement()
    def draw(self , screen):
        screen.blit(self.image_present, self.rect)


