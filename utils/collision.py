import pygame


def check_collision(object_a, object_b):
    rect_a = pygame.Rect(object_a.get_rect())
    rect_b = pygame.Rect(object_b.get_rect())

    return rect_a.colliderect(rect_b)
