import pygame

def check_collision(object_a, object_b):
    if object_a.rect.colliderect(object_b.rect):
        return True
    return False

# Collision between an object and a group of objects
def check_object_group_collision(object_a, group_b):

    for object in group_b.sprites():

        if object_a.rect.colliderect(object.rect):
            return True, object
    return False, None
