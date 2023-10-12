# Pygame шаблон - скелет для нового проекта Pygame

import pygame

WIDTH = 360
HEIGHT = 480
FPS = 30

# Задаем цвета

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окноls


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Цикл игры

running = True

while running:

    # Держим цикл на правильной скорости
    
    clock.tick(FPS)

    # Ввод процесса (события)

    for event in pygame.event.get():

        # check for closing window

        if event.type == pygame.QUIT:
            running = False


while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)

#создание спрайтов

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group() 

all_sprites.update()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.filShIIIrochkal(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)