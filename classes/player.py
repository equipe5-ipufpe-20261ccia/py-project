import pygame
from classes.screen_paramaters import ScreenParameters
from utils.helpers import Helpers
from classes.text import Text

class Player:
    def __init__(self):

        #declarando as imagens do jogador
        self.image_left = Helpers("assets/images/Low_tier_god.jpg" , 100 , 100).get_proporsion()
        self.image_right = Helpers("assets/images/Low_tier_god2.jpg" , 100 , 100).get_proporsion()
        self.image_high = Helpers("assets/images/Low_tier_god3.jpg" , 100 , 100).get_proporsion()
        self.image_down = Helpers("assets/images/Low_tier_god4.jfif" , 100 , 100).get_proporsion()

        #declarando a posição inicial e o tamanho do retangulo

        self.image_present = self.image_left
        self.rect = self.image_present.get_rect()
        self.rect.x = 200
        self.rect.y = 200
        self.speed = 5

        #status do personagem

        self.vida = 100

    def get_position(self):
        return (self.rect.x, self.rect.y)
    def movement(self , screen):

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
            self.image_present = self.image_high

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

        if self.rect.right > screen.x:
            self.rect.right = screen.x

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > screen.y:
            self.rect.bottom = screen.y
    def update(self , screen):
        self.movement(screen)
    def draw(self , screen):
        screen.blit(self.image_present, self.rect)


