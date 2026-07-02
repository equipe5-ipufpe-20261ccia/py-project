import pygame
from utils.collision import check_collision, check_object_group_collision

# pygame.sprite.Sprite because of practicity of killing and grouping enemies
class Enemy(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.health = 5
        self.damage = 4
        self.fire = False

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.enemy_speed = 3

    def IsBurning(self):
        if self.fire:
            self.health -= 3

    # Centralizamos TODA a lógica de jogo no update
    def update(self, player, bullets):
        if not check_collision(player, self):
            vector_player = pygame.math.Vector2(player.rect.center)
            vector_enemy = pygame.math.Vector2(self.rect.center)
            direction_vector = vector_player - vector_enemy

            if direction_vector.length() > 0:
                vector_normalize = direction_vector.normalize()
                self.rect.x += vector_normalize.x * self.enemy_speed
                self.rect.y += vector_normalize.y * self.enemy_speed

        if check_collision(player, self):
            player.health -= self.damage
            player.get_health()
            print(f"Current health is: {player.health}")
            self.rect.x = 0
            self.rect.y = 0

        elif check_object_group_collision(self, bullets)[0]:
            while self.health > 0:
                self.health -= check_object_group_collision(self, bullets)[1].damage
                self.IsBurning()
                print(f"{self.health}")
            self.rect.x = 0
            self.rect.y = 0

    def get_position(self):
        return (self.rect.x, self.rect.y)

class MiniSpider(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.animations = {
            'down': self.load_spritesheet("assets/images/Spider_mini_down-Sheet.png"),
            'up': self.load_spritesheet("assets/images/Spider_mini_top-Sheet.png"),
            'left': self.load_spritesheet("assets/images/Spider_mini_left-Sheet.png"),
            'right': self.load_spritesheet("assets/images/Spider_mini_right-Sheet.png")
        }
        
        self.current_direction = 'down'
        self.current_frame = 0
        self.image = self.animations[self.current_direction][self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        
        self.speed = 3 
        self.animation_speed = 0.05 
        
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = 3000

    def load_spritesheet(self, filename, num_frames=3): 
        sheet = pygame.image.load(filename).convert_alpha()
        frame_width = sheet.get_width() // num_frames
        frame_height = sheet.get_height()
        
        frames = []
        for i in range(num_frames):
            frame = sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            frame = pygame.transform.scale(frame, (40, 40)) 
            frames.append(frame)
        return frames

    def update(self, player, current_time):
        
        if current_time - self.spawn_time > self.lifetime:
            self.kill() 
            return 

        vector_player = pygame.math.Vector2(player.rect.center)
        vector_spider = pygame.math.Vector2(self.rect.center)
        direction_vector = vector_player - vector_spider
        
        if direction_vector.length() > 0:
            vetor_normalize = direction_vector.normalize()
            self.rect.x += vetor_normalize.x * self.speed
            self.rect.y += vetor_normalize.y * self.speed
            
            if abs(vetor_normalize.x) > abs(vetor_normalize.y):
                if vetor_normalize.x > 0:
                    self.current_direction = 'right'
                else:
                    self.current_direction = 'left'
            else:
                if vetor_normalize.y > 0:
                    self.current_direction = 'down'
                else:
                    self.current_direction = 'up'

        self.current_frame += self.animation_speed
        if self.current_frame >= 3: 
            self.current_frame = 0
        self.image = self.animations[self.current_direction][int(self.current_frame)]

        if self.rect.colliderect(player.rect):
            player.health -= 2
            player.get_health()
            player.damage_sound.play()
            print(f"Current health is: {player.health}")
            self.kill()