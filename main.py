import pygame

from classes import enemy
from classes.screen_paramaters import ScreenParameters
from classes.player import Player
from classes.enemy import Enemy

def main():
    pygame.init()

    pygame.mixer.init()
    pygame.mixer.music.load("assets/music/Low_tier_god.mp3")
    pygame.mixer_music.set_volume(0.2)
    pygame.mixer.music.play(loops=0)

    config_screen = ScreenParameters(800 , 600)
    screen = pygame.display.set_mode(config_screen.get_screen_width())
    fps = 60
    pygame.display.set_caption("dogo_adventure")

    clock = pygame.time.Clock()

    player = Player()
    enemy = Enemy()

    running = True

    while running:
        clock.tick(fps)
        screen.fill((14 , 219 , 248))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        player.update()
        enemy.update(player)
        player.draw(screen)
        enemy.draw(screen)

        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
