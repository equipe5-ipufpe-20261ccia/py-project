import pygame

def check_collision(object_a, object_b):
    if object_a.rect.colliderect(object_b.rect):
        return True
    return False
