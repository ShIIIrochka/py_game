import pygame
from sys import exit
from random import randint
 
WIDTH = 728
HEIGHT = 350
FPS = 60
 
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
 
# Загрузка и конвертация изображений
sky_surface = pygame.image.load('sky.PNG').convert()
ground_surface = pygame.image.load('ground.PNG').convert()

pit1_surface = pygame.image.load('pit.PNG').convert_alpha()
pit_surf = pygame.transform.scale(pit1_surface, (45, 45))
pit_rect = pit_surf.get_rect(midbottom=(728, 270))
 
cat_surf = pygame.image.load('cat.PNG').convert_alpha()

cat_stand_surf = pygame.image.load('cat.stand.PNG').convert_alpha()
cat_stand_surf = pygame.transform.scale(cat_stand_surf, (200, 200))
cat_rect = cat_stand_surf.get_rect(midbottom = (364, 230))

bird_surf = pygame.image.load('fish.PNG').convert_alpha()
bird_surf = pygame.transform.scale(bird_surf, (50, 50))
bird_rect= bird_surf.get_rect(midbottom=(728, 70))

player_surf = pygame.transform.scale(cat_surf, (90, 90))
player_rect = player_surf.get_rect(midbottom=(100, 250))
player_gravity = 0
 
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
 
# Флаги для состояния игры
running = True
game_active = False
 
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Обработка ввода (событий)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.y >= 150:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
 
            if event.type == pygame.KEYDOWN and player_rect.y >= 150:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20
        else:
            # Перезапуск игры, если игрок проиграл
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                pit_rect.left = 728
 
    if game_active:
        screen.blit(sky_surface, (0, 0))  # Вывод изображения неба на экран
        screen.blit(ground_surface, (0, 250))  # Вывод изображения земли на экран
 
        player_gravity += 1  # Скорость гравитации для кота
        player_rect.y += player_gravity
        if player_rect.bottom >= 250:
            player_rect.bottom = 250
        screen.blit(player_surf, player_rect)
 
        pit_rect.x -= 5
        if pit_rect.right <= 0:
            pit_rect.left = 728
        screen.blit(pit_surf, pit_rect)


        bird_rect.x -= 4
        if bird_rect.right <0:
            bird_rect.left = 728
        screen.blit(bird_surf, bird_rect)

        # Переключение видимости указателя мыши
        pygame.mouse.set_visible(True)
 
        # Обработка столкновения
        if player_rect.colliderect(pit_rect):
            game_active = False
    else:
        # Если произошло столкновение кота с ямой
        screen.fill((123, 145, 123))  # Заполняем экран зеленым цветом
        screen.blit(cat_stand_surf, cat_rect)
        game_active = False
 
    pygame.display.update()