from cmath import rect

import pygame
import constants
from classes.screen_paramaters import ScreenParameters
from classes.player import Player
from classes.enemy import Enemy
from classes.game_object import Heart, Potion
from classes.boss import Boss

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
    heart = Heart()
    potion = Potion()
    boss = Boss(config_screen.get_screen_width()[0])

    running = True

    while running:
        current_time = pygame.time.get_ticks()
        clock.tick(fps)
        screen.fill((14, 219, 248))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Updating stats/position

        player.update(config_screen, current_time)
        bullets.update(enemies)
        enemies.update(player, bullets)
        boss.update(current_time, player, bullets)

        # Drawing on screen a(and a few other things)

        boss.draw(screen)
        player.draw(screen, current_time)
        heart.draw(screen, player)
        potion.draw(screen, player)
        enemies.draw(screen)
        bullets.draw(screen)

        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
