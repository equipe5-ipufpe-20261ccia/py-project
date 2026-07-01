import pygame
import constants

class HUD:
    def __init__(self, screen):
        self.screen = screen
        
        self.font = pygame.font.SysFont(constants.FONT_STYLE, constants.FONT_SIZE)
        self.font_large = pygame.font.SysFont(constants.FONT_STYLE, constants.FONT_SIZE + 6)
        self.boss_font = pygame.font.SysFont(constants.FONT_STYLE, 30, bold=True)

        self.health_frames = self.load_spritesheet("assets/images/health_circle.png", num_frames=8)
        
        self.heart_icon = pygame.image.load("assets/images/heart_sprite_valido.png").convert_alpha()
        self.heart_icon = pygame.transform.scale(self.heart_icon, (30, 30))
        
        self.potion_icon = pygame.image.load("assets/images/green_potion_sprite.png").convert_alpha()
        self.potion_icon = pygame.transform.scale(self.potion_icon, (30, 30))
        
        self.coin_icon = pygame.image.load("assets/images/coin_test.png").convert_alpha()
        self.coin_icon = pygame.transform.scale(self.coin_icon, (30, 30))
        

    def load_spritesheet(self, filename, num_frames):
        sheet = pygame.image.load(filename).convert_alpha()
        frame_width = sheet.get_width() // num_frames
        frame_height = sheet.get_height()
        
        frames = []
        for i in range(num_frames):
            frame = sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            frame = pygame.transform.scale(frame, (80, 80))
            frames.append(frame)
        return frames

    def draw(self, player, boss):
        max_h = player.max_health if hasattr(player, 'max_health') else 80 
        percent_health = max(0, min(1, player.health / max_h))
        num_frames = len(self.health_frames)
        
        frame_index = int((1 - percent_health) * (num_frames - 1))
        frame_index = max(0, min(num_frames - 1, frame_index))
        
        self.screen.blit(self.health_frames[frame_index], (20, 20))


        health_text = self.font.render(f"Vida: {player.health}/{max_h}", True, constants.WHITE)
        self.screen.blit(health_text, (110, 45))

        heart_x = constants.SCREEN_X - 150
        self.screen.blit(self.heart_icon, (heart_x, 25))
        heart_text = self.font_large.render(f"x {player.collected_hearts}", True, constants.WHITE)
        self.screen.blit(heart_text, (heart_x + 40, 27))

        self.screen.blit(self.potion_icon, (heart_x, 65))
        potion_text = self.font_large.render(f"x {player.collected_potions}", True, constants.WHITE)
        self.screen.blit(potion_text, (heart_x + 40, 67))
        
        coins_collected = player.collected_coins if hasattr(player, 'collected_coins') else 0
        self.screen.blit(self.coin_icon, (heart_x, 105))
        coin_text = self.font_large.render(f"x {coins_collected}", True, constants.WHITE)
        self.screen.blit(coin_text, (heart_x + 40, 107))


        if boss.vida > 0:
            boss_text = self.boss_font.render(f"BOSS HP: {boss.vida}", True, (255, 0, 0))
            
            text_x = self.screen.get_width() // 2 - boss_text.get_width() // 2
            text_y = self.screen.get_height() - 120 
            
            self.screen.blit(boss_text, (text_x, text_y))