# Pygame шаблон - скелет для нового проекта Pygame

import pygame
from sys import exit

WIDTH = 728
HEIGHT = 350
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#load and convert images
sky_surface = pygame.image.load('/home/ksenia/projects/py_game/pythongame/sky.PNG').convert()
ground_surface = pygame.image.load('/home/ksenia/projects/py_game/pythongame/ground.PNG').convert()

pit_surface = pygame.image.load('/home/ksenia/projects/py_game/pythongame/pit.PNG').convert_alpha()
pit_rect = pit_surface.get_rect(midbottom  = (350, 250))

cat_surf = pygame.image.load('/home/ksenia/projects/py_game/pythongame/cat.PNG').convert_alpha()

player_surf = pygame.transform.scale(cat_surf, (70, 70))
player_rect = player_surf.get_rect(midbottom = (100,250))
player_gravity = 0

pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Цикл игры

running = True

while running:

    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # ввод процесса (события)
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                player_gravity = -20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20

    screen.blit(sky_surface, (0,0)) #вывод на экран изображения неба
    screen.blit(ground_surface, (0, 250)) #вывод на экран изображения земли

    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 250: player_rect.bottom = 250
    screen.blit(player_surf, player_rect)

    pit_rect.x -= 5
    if pit_rect.right <= 0: pit_rect.left = 728
    screen.blit(pit_surface, pit_rect)

    mouse_pos = pygame.mouse.set_visible(True)

    #if player_rect.colliderect(pit_rect) == 1: 
     #   print("True")


    pygame.display.update()