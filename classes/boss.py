import pygame
from classes.enemy import MiniSpider  

class Boss(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        
        self.sprites = self.load_spritesheet("assets/images/spider_boss_idle.png", num_frames=3)
        self.current_frame = 0
        self.animation_speed = 0.05
        
        self.image = self.sprites[self.current_frame]
        self.rect = self.image.get_rect()
        
        self.rect.centerx = screen_width // 2
        self.rect.top = 20

        self.vida = 300
        
        self.screen_width = screen_width
        self.direction = 1 
        self.boss_speed = 2 
        
        self.mini_spiders = pygame.sprite.Group()
        self.last_attack_time = 0
        self.attack_cooldown = 4000

    def load_spritesheet(self, filename, num_frames=3):
        sheet = pygame.image.load(filename).convert_alpha()
        frame_width = sheet.get_width() // num_frames
        frame_height = sheet.get_height()
        
        frames = []
        for i in range(num_frames):
            frame = sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            frame = pygame.transform.scale(frame, (250, 250)) 
            frames.append(frame)
            
        return frames

    def update(self, current_time, player, bullets): 
        
        if self.vida <= 0:
            return 

        self.current_frame += self.animation_speed
        if self.current_frame >= 3:
            self.current_frame = 0
        self.image = self.sprites[int(self.current_frame)]

        self.rect.x += self.boss_speed * self.direction
        if self.rect.right >= self.screen_width - 20: 
            self.direction = -1
        elif self.rect.left <= 20: 
            self.direction = 1

        balas_que_bateram = pygame.sprite.spritecollide(self, bullets, False)
        
        for bala in balas_que_bateram:
            if bala.state != "IMPACT":
                self.vida -= bala.damage 
                bala.state = "IMPACT" # Ativa o impacto na bala
                bala.bullet_animation.frame = 6 # Pula para o frame 6
                print(f"Boss tomou dano! Vida restante: {self.vida}")

        if self.vida <= 0:
            print("VITÓRIA! O Boss foi derrotado!")
            self.kill() 
            
            for spider in self.mini_spiders:
                spider.kill()

        if current_time - self.last_attack_time > self.attack_cooldown:
            self.spawn_mini_spiders()
            self.last_attack_time = current_time
            
        self.mini_spiders.update(player, current_time)

    def spawn_mini_spiders(self):
        positions = [
            (self.rect.left, self.rect.centery),
            (self.rect.right, self.rect.centery),
            (self.rect.centerx - 50, self.rect.bottom),
            (self.rect.centerx + 50, self.rect.bottom)
        ]
        
        for pos in positions:
            nova_aranha = MiniSpider(pos[0], pos[1])
            self.mini_spiders.add(nova_aranha)

    def draw(self, screen):
        if self.vida > 0:
            screen.blit(self.image, self.rect)
        self.mini_spiders.draw(screen)