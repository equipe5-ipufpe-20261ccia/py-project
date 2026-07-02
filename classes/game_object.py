import pygame
import random
from utils.collision import check_collision

# General class of collectables. can be collected and are stored in the player class
class Collectable(pygame.sprite.Sprite):
    def __init__(self, image, width=30, height=30):
        super().__init__()
        self.image_collectable = pygame.image.load(image).convert_alpha()
        self.image_collectable = pygame.transform.scale(self.image_collectable, (width, height))
        
        self.rect = self.image_collectable.get_rect()
        self.rect.x = random.randint(50, 750)
        self.rect.y = random.randint(300, 500)
        
        self.spawn_time = pygame.time.get_ticks()  
        self.lifetime = 7000  
        
    #retorna se o coletavel ja passou do tempo de vida, para ser removido da tela
    def is_expired(self, current_time):
        return current_time - self.spawn_time > self.lifetime

# Differents effects for differemts collectables

    def effect(self, player):
        pass

    def draw(self, screen):
        screen.blit(self.image_collectable, self.rect)

# have to put an if to stop object from respawning in the same place
# Types of collectibles
class Heart(Collectable):
    def __init__(self):
        super().__init__("assets/images/heart_sprite_valido.png")
        
    def effect(self, player):
        max_h = player.max_health if hasattr(player, 'max_health') else 80
        player.health = min(max_h, player.health + 10)
        player.collected_hearts += 1  
        print(f"Voce coletou 10 de vida, vida atual: {player.health}, Total: {player.collected_hearts}")

class Potion(Collectable):
    def __init__(self):
        super().__init__("assets/images/green_potion_sprite.png")
        
    def effect(self, player):
        player.speed += 1
        player.collected_potions += 1  
        print(f"Voce coletou 1 de speed, speed atual: {player.speed}, Total: {player.collected_potions}")

# Battery will work as a charge attack, when full will release a BIG SHOT
class Battery(Collectable):
    def __init__(self):
        super().__init__("assets/images/coin_test.png")
        
    def effect(self, player):
        if not hasattr(player, 'energy'):
            player.energy = 0
        player.energy += 1
        
        if not hasattr(player, 'collected_coins'):
            player.collected_coins = 0
        player.collected_coins += 1
        
        print(f"Coletou Bateria! Energia para o Big Shot: {player.energy}")

class ItemManager:
    def __init__(self):
        self.items_list = []
        self.last_spawn_time = 0
        self.spawn_cooldown = 5000  
        self.collect_sound = pygame.mixer.Sound("assets/music/item_collect_sound_effect.flac")
        self.collect_sound.set_volume(0.2)
        self.heart_sound = pygame.mixer.Sound("assets/music/heart_collect_sound_effect.wav")

    def update(self, current_time, screen_width, screen_height, player):
        if current_time - self.last_spawn_time > self.spawn_cooldown:
            escolha = random.choice(["heart", "potion", "battery"])
            if escolha == "heart":
                new_item = Heart()
            elif escolha == "potion":
                new_item = Potion()
            else:
                new_item = Battery() 
            
            new_item.rect.x = random.randint(50, screen_width - 50)
            new_item.rect.y = random.randint(300, screen_height - 50)
            self.items_list.append(new_item)
            self.last_spawn_time = current_time

        for item in self.items_list[:]:
            if player.rect.colliderect(item.rect):
                if type(item).__name__ == "Heart":
                    self.heart_sound.play()
                else:
                    self.collect_sound.play()
                item.effect(player)
                self.items_list.remove(item)

            elif item.is_expired(current_time):
                self.items_list.remove(item)

    def draw(self, screen):
        for item in self.items_list:
            item.draw(screen)