import pygame
from utils.animation import Animation
from utils import spritesheet
from classes.bullet import Bullet

class Player(pygame.sprite.Sprite):

    def __init__(self, bullets, screen):
        super().__init__()
        self.health = 80
        self.speed = 6
        self.energy = 0
        self.kill_count = 0
        
        self.max_health = 80       
        self.collected_hearts = 0  
        self.collected_potions = 0 

        # Direction positioned

        self.facing_up = False
        self.facing_right = False
        self.facing_left = False
        self.facing_down = True

        # Direction moving towards

        self.moving_up = False
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False


        # Idle animation

        self.player_sprite_idle_up = pygame.image.load("assets/images/player_idle_up.png").convert_alpha()
        self.player_idle_up = Animation(image=self.player_sprite_idle_up, screen=screen)
        self.player_idle_up.animation_sheet(steps=3, width=32, height=32)

        self.player_sprite_idle_right = pygame.image.load("assets/images/player_idle_right.png").convert_alpha()
        self.player_idle_right = Animation(image=self.player_sprite_idle_right, screen=screen)
        self.player_idle_right.animation_sheet(steps=3, width=32, height=32)

        self.player_sprite_idle_left = pygame.image.load("assets/images/player_idle_left.png").convert_alpha()
        self.player_idle_left = Animation(image=self.player_sprite_idle_left, screen=screen)
        self.player_idle_left.animation_sheet(steps=3, width=32, height=32)

        self.player_sprite_idle_down = pygame.image.load("assets/images/player_idle_down.png").convert_alpha()
        self.player_idle_down = Animation(image=self.player_sprite_idle_down, screen=screen)
        self.player_idle_down.animation_sheet(steps=3, width=32, height=32)

        # Running animation assets/images/player_left_run_spritesheet.png"

        self.player_sprite_up = pygame.image.load("assets/images/player_up_run_spritesheet.png").convert_alpha()
        self.player_up = Animation(image=self.player_sprite_up, screen=screen)
        self.player_up.animation_sheet(steps=11, width=32, height=32)

        # Confused left and right sheets, fix the names later

        self.sprite_right = pygame.image.load("assets/images/player_left_run_spritesheet.png").convert_alpha()
        self.player_right = Animation(image=self.sprite_right, screen=screen)
        self.player_right.animation_sheet(steps=9, width=32, height=32)

        self.player_sprite_left = pygame.image.load("assets/images/player_right_run_spritesheet.png").convert_alpha()
        self.player_left = Animation(image=self.player_sprite_left, screen=screen)
        self.player_left.animation_sheet(steps=9, width=32, height=32)

        self.player_sprite_down = pygame.image.load("assets/images/player_down_run_spritesheet.png").convert_alpha()
        self.player_down = Animation(image=self.player_sprite_down, screen=screen)
        self.player_down.animation_sheet(steps=10, width=32, height=32)

        self.image_present = pygame.Surface((32, 32))
        self.image_present.fill((0, 255, 0))

        self.rect = self.image_present.get_rect()
        self.rect.x = 200
        self.rect.y = 200

        self.bullets = bullets
        self.single_press = True
    def get_position(self):
        return (self.rect.x, self.rect.y)

    def get_health(self):
        self.health = min(self.health, 80)

    def get_speed(self):
        self.speed = max(4, min(self.speed, 8))

    def get_energy(self):
        self.speed = min(self.energy, 5)

    def movement(self, screen_params, current_time):

        # verifica se a tecla esta sendo pressionada
        # O comando .get_pressed() , verifica se a tecla esta precionada
        key = pygame.key.get_pressed()

        mov_x = 0
        mov_y = 0

        self.moving_down = False
        self.moving_up = False
        self.moving_right = False
        self.moving_left = False

        if key[pygame.K_a]:
            mov_x = -1
            self.moving_left = True
            self.facing_left = True

            self.facing_up = False
            self.facing_right = False
            self.facing_down = False

        if key[pygame.K_d]:
            mov_x = 1
            self.moving_right = True
            self.facing_right = True

            self.facing_up = False
            self.facing_left = False
            self.facing_down = False

        if key[pygame.K_w]:
            mov_y = -1
            self.moving_up = True
            self.facing_up = True

            self.facing_left = False
            self.facing_right = False
            self.facing_down = False
        if key[pygame.K_s]:
            mov_y = 1
            self.moving_down = True
            self.facing_down = True

            self.facing_up = False
            self.facing_right = False
            self.facing_left = False

        current_speed = self.speed
        if mov_x != 0 and mov_y != 0:
            current_speed = self.speed * 0.7

        self.rect.x += mov_x * current_speed
        self.rect.y += mov_y * current_speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_params.x:
            self.rect.right = screen_params.x
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_params.y:
            self.rect.bottom = screen_params.y
    # Creates a bullet when Space is pressed, only works one click at a time
    def shooting(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.single_press:
            bulllet = Bullet(self.rect.centerx, self.rect.top)
            self.bullets.add(bulllet)
            print("shot")
            self.single_press = False
        elif not key[pygame.K_SPACE]:
            self.single_press = True
            
    def collect_items(self, hearts, potions):
        # 1. Colisão com os Corações
        for heart in hearts[:]: 
            if self.rect.colliderect(heart.rect):
                self.collected_hearts += 1
                self.health += 20
                if self.health > self.max_health:
                    self.health = self.max_health 
                print(f"Apanhou um coração! Vida atual: {self.health}")
                hearts.remove(heart) 

        # 2. Colisão com as Poções
        for potion in potions[:]:
            if self.rect.colliderect(potion.rect):
                self.collected_potions += 1
                self.energy += 1
                print(f"Apanhou uma poção! Energia atual: {self.energy}")
                potions.remove(potion)

    def update(self, screen_params, current_time, hearts, potions):
        self.movement(screen_params, current_time)
        self.shooting()
        self.collect_items(hearts, potions)

    def draw(self, screen, current_time):
        if self.moving_down:
            self.player_down.update_and_draw(current_time, cooldown=100, width=64, height=64, y=self.rect.y,
                                             x=self.rect.x)
        elif self.moving_up:
            self.player_up.update_and_draw(current_time, cooldown=100, width=64, height=64, y=self.rect.y,
                                           x=self.rect.x)
        elif self.moving_left:
            self.player_left.update_and_draw(current_time, cooldown=100, width=64, height=64, y=self.rect.y,
                                             x=self.rect.x)
        elif self.moving_right:
            self.player_right.update_and_draw(current_time, cooldown=100, width=64, height=64, y=self.rect.y,
                                              x=self.rect.x)
        else:
            if self.facing_up:
                self.player_idle_up.update_and_draw(current_time,
                cooldown=100, width=64, height=64, y=self.rect.y,x=self.rect.x)
            elif self.facing_right:
                self.player_idle_right.update_and_draw(current_time,
                cooldown=100, width=64, height=64, y=self.rect.y,x=self.rect.x)
            elif self.facing_left:
                self.player_idle_left.update_and_draw(current_time,
                cooldown=100, width=64, height=64, y=self.rect.y,x=self.rect.x)
            elif self.facing_down:
                self.player_idle_down.update_and_draw(current_time,
                cooldown=100, width=64, height=64, y=self.rect.y,x=self.rect.x)

