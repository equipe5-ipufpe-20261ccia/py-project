import pygame

class Boss:
    def __init__(self, screen_width):
        boss_width = 500
        start_x = (screen_width - boss_width) // 2
        
        head_width = 300
        head_height = 140
        head_x = start_x + 100
        head_y = 30
        
        hand_size = 100
        hand_y = 70
        
        self.left_hand = pygame.Rect(start_x, hand_y, hand_size, hand_size)
        self.head = pygame.Rect(head_x, head_y, head_width, head_height)
        self.right_hand = pygame.Rect(start_x + 400, hand_y, hand_size, hand_size)

        self.vida_left_hand = 50
        self.vida_head = 150
        self.vida_right_hand = 50

        self.cor_mao = (220, 50, 50)      
        self.cor_cabeca = (150, 40, 180)  

    def draw(self, screen):
        if self.vida_left_hand > 0:
            pygame.draw.rect(screen, self.cor_mao, self.left_hand)
        
        if self.vida_head > 0:
            pygame.draw.rect(screen, self.cor_cabeca, self.head)

        if self.vida_right_hand > 0:
            pygame.draw.rect(screen, self.cor_mao, self.right_hand)

    def is_dead(self):
        return self.vida_left_hand <= 0 and self.vida_head <= 0 and self.vida_right_hand <= 0