from cmath import rect
import random

import pygame
import constants
from classes.screen_paramaters import ScreenParameters
from classes.player import Player
from classes.enemy import Enemy
from classes.game_object import Heart, Potion
from classes.boss import Boss
from classes.hud import HUD

def main():

    # Initial setup

    pygame.init()

    pygame.mixer.init()
    pygame.mixer.music.load("assets/music/spider_battle_music.mp3")
    pygame.mixer_music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    config_screen = ScreenParameters(constants.SCREEN_Y , constants.SCREEN_X)
    screen = pygame.display.set_mode(config_screen.get_screen_width())
    fps = 60
    pygame.display.set_caption("DreamHell")
    icon = pygame.image.load("assets/images/menu_01.png").convert_alpha()
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()

    # Initializing all important objects

    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    player = Player(bullets, screen)
    hearts = []  
    potions = [] 

    # Cria um alarme que apita a cada 5000 milissegundos (5 segundos)
    SPAWN_ITEM_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_ITEM_EVENT, 5000)
    
    boss = Boss(config_screen.get_screen_width()[0])
    hud = HUD(screen)

    running = True

    while running:
        current_time = pygame.time.get_ticks()
        clock.tick(fps)
        screen.fill((14, 219, 248))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            # --- QUANDO O ALARME APITAR (a cada 5 segundos) ---
            if event.type == SPAWN_ITEM_EVENT:
                # 50% de chance de ser coração ou poção
                if random.choice(["heart", "potion"]) == "heart":
                    new_heart = Heart()
                    # Define posição X e Y aleatória dentro dos limites da tela
                    new_heart.rect.x = random.randint(50, screen.get_width() - 50)
                    new_heart.rect.y = random.randint(50, screen.get_height() - 50)
                    hearts.append(new_heart) 
                else:
                    new_potion = Potion()
                    new_potion.rect.x = random.randint(50, screen.get_width() - 50)
                    new_potion.rect.y = random.randint(50, screen.get_height() - 50)
                    potions.append(new_potion) 

        # Updating stats/position

        player.update(config_screen, current_time, hearts, potions,screen) 
        
        bullets.update(enemies, current_time)
        enemies.update(player, bullets)
        boss.update(current_time, player, bullets)

        # Drawing on screen
        boss.draw(screen)
        player.draw(screen, current_time)
        
        for h in hearts:
            h.draw(screen, player)
        for p in potions:
            p.draw(screen, player)
            
        enemies.draw(screen)
        bullets.draw(screen)
        hud.draw(player, boss)

        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()