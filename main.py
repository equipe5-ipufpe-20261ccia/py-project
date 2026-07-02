from cmath import rect
import random

import pygame
import constants
from utils import button
from utils.animation import Animation 
from utils.text import Draw_text
from classes.screen_paramaters import ScreenParameters
from classes.player import Player
from classes.enemy import Enemy
from classes.game_object import ItemManager
from classes.boss import Boss
from classes.hud import HUD

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("assets/music/title_music.mp3") 
pygame.mixer.music.set_volume(constants.VOLUME) 
pygame.mixer.music.play(-1) 

config_screen = ScreenParameters(constants.SCREEN_Y , constants.SCREEN_X)
screen = pygame.display.set_mode((constants.SCREEN_X, constants.SCREEN_Y))
pygame.display.set_caption("Main_menu")

clock = pygame.time.Clock()
fps = 60
deafh = False
font = pygame.font.SysFont("arialblack", 40)
font_text = pygame.font.SysFont("arial", 30)

bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player(bullets, screen)

item_manager = ItemManager()

boss = Boss(config_screen.get_screen_width()[0])
hud = HUD(screen)

resume_img = pygame.image.load("assets/images/Play.png").convert_alpha()
options_img = pygame.image.load("assets/images/Opitions.png").convert_alpha()
return_img = pygame.image.load("assets/images/Return.png").convert_alpha()
# Novas imagens adicionadas!
res_800_img = pygame.image.load("assets/images/800x800.png").convert_alpha()
res_1024_img = pygame.image.load("assets/images/1024x768.png").convert_alpha()
quit_img = pygame.image.load("assets/images/Quit.png").convert_alpha()

titulo_options = Draw_text("MENU DE OPÇÕES", screen=screen)
txt_volume = Draw_text(f"Volume: {int(constants.VOLUME * 100)}%", screen=screen)
txt_resolucao = Draw_text(f"Resolução: {constants.SCREEN_X}x{constants.SCREEN_Y}", screen=screen)

sprite_sheet_image = pygame.image.load("assets/images/Title-background.png").convert_alpha()
screen_animation = Animation(image=sprite_sheet_image, screen=screen , minimium=0) 
screen_animation.animation_sheet(steps=12 , width=800 , height=800) 

resume_button = button.Button(0, 0, resume_img, 1)
options_button = button.Button(0, 0, options_img, 1) 
quit_button = button.Button(0, 0, quit_img, 1) 

return_button = button.Button(0, 0, return_img, 1)
res_800_button = button.Button(0, 0, res_800_img, 1)
res_1024_button = button.Button(0, 0, res_1024_img, 1)

game_state = "menu"

run = True 
while run:
    current_time = pygame.time.get_ticks()
    screen.fill((0, 0, 0)) 
    
    pos_mouse = pygame.mouse.get_pos()
    centro_x = constants.SCREEN_X // 2

    if game_state == "menu":  
        screen_animation.update_and_draw(current_time, cooldown=100, width=constants.SCREEN_X, height=constants.SCREEN_Y , x=0 , y=0 , maximium=12  , minimium=0 )
        
        largura_play = resume_img.get_width()
        largura_options = options_img.get_width()
        largura_quit = quit_img.get_width()
        
        resume_button.rect.x = constants.SCREEN_X - largura_play - 50
        resume_button.rect.y = (constants.SCREEN_Y // 2) - 300
        
        options_button.rect.x = constants.SCREEN_X - largura_options - 50
        options_button.rect.y = (constants.SCREEN_Y // 2) - 200
        
        quit_button.rect.x = constants.SCREEN_X - largura_quit - 50
        quit_button.rect.y = (constants.SCREEN_Y // 2) - 100
        
        if resume_button.draw(screen):
            game_state = "playing"
            
        if options_button.draw(screen):
            game_state = "options"
            
        if quit_button.draw(screen):
            run = False 
            
    elif game_state == "playing":
        pygame.mixer.music.stop()
        current_time = pygame.time.get_ticks()
        clock.tick(fps)
        screen.fill((19,9,134))
        
        player.update(config_screen, current_time, screen)    
        item_manager.update(current_time, screen.get_width(), screen.get_height(), player)
        bullets.update(enemies, current_time)
        enemies.update(player, bullets)
        boss.update(current_time, player, bullets)

        # Drawing on screen
        boss.draw(screen)
        player.draw(screen, current_time)
        item_manager.draw(screen)   
        enemies.draw(screen)
        bullets.draw(screen)
        hud.draw(player, boss)

        largura_return = return_img.get_width()
        return_button.rect.x = centro_x - (largura_return //10)
        return_button.rect.y = 0
        
        if return_button.draw(screen):
            game_state = "menu"
            pygame.mixer.music.play(-1)

    elif game_state == "options":
        screen_animation.update_and_draw(current_time, cooldown=100, width=constants.SCREEN_X, height=constants.SCREEN_Y , x=0 , y=0 , maximium=12 , minimium=0)
        
        titulo_options.draw_and_update(font, (255, 255, 255), centro_x - 180, 50, current_time, 0)
        
        txt_volume.draw_and_update(font_text, (255, 255, 0), centro_x - 70, 180, current_time, 0)
        
        btn_vol_menos = pygame.Rect(centro_x - 70, 230, 50, 40)
        btn_vol_mais = pygame.Rect(centro_x + 20, 230, 50, 40)
        
        pygame.draw.rect(screen, (220, 50, 50), btn_vol_menos)
        pygame.draw.rect(screen, (50, 220, 50), btn_vol_mais)
        
        Draw_text("-", screen).draw_and_update(font_text, (255, 255, 255), centro_x - 52, 232, current_time, 0)
        Draw_text("+", screen).draw_and_update(font_text, (255, 255, 255), centro_x + 36, 232, current_time, 0)

        txt_resolucao.draw_and_update(font_text, (255, 255, 0), centro_x - 130, 340, current_time, 0)
        
        largura_800 = res_800_img.get_width()
        largura_1024 = res_1024_img.get_width()
        
        res_800_button.rect.x = centro_x - largura_800 - 10
        res_800_button.rect.y = 390
        
        res_1024_button.rect.x = centro_x + 10
        res_1024_button.rect.y = 390
        
        if res_800_button.draw(screen):
            constants.SCREEN_X, constants.SCREEN_Y = 800, 800
            screen = pygame.display.set_mode((constants.SCREEN_X, constants.SCREEN_Y))
            txt_resolucao = Draw_text(f"Resolução: {constants.SCREEN_X}x{constants.SCREEN_Y}", screen=screen)
            txt_resolucao.current_word = len(txt_resolucao.text)
            
        if res_1024_button.draw(screen):
            constants.SCREEN_X, constants.SCREEN_Y = 1024, 768
            screen = pygame.display.set_mode((constants.SCREEN_X, constants.SCREEN_Y))
            txt_resolucao = Draw_text(f"Resolução: {constants.SCREEN_X}x{constants.SCREEN_Y}", screen=screen)
            txt_resolucao.current_word = len(txt_resolucao.text)

        # --- BOTÃO RETORNO NA TELA DE OPÇÕES ---
        largura_return = return_img.get_width()
        return_button.rect.x = centro_x - (largura_return // 2)
        return_button.rect.y = constants.SCREEN_Y - 120
        
        if return_button.draw(screen):
            game_state = "menu"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                if game_state == "options":
                    if btn_vol_menos.collidepoint(pos_mouse):
                        constants.VOLUME = max(0.0, constants.VOLUME - 0.1)
                        pygame.mixer.music.set_volume(constants.VOLUME)
                        txt_volume = Draw_text(f"Volume: {int(constants.VOLUME * 100)}%", screen=screen)
                        txt_volume.current_word = len(txt_volume.text)
                        
                    if btn_vol_mais.collidepoint(pos_mouse):
                        constants.VOLUME = min(1.0, constants.VOLUME + 0.1)
                        pygame.mixer.music.set_volume(constants.VOLUME)
                        txt_volume = Draw_text(f"Volume: {int(constants.VOLUME * 100)}%", screen=screen)
                        txt_volume.current_word = len(txt_volume.text)
            
    pygame.display.update()

pygame.quit()