import pygame
from sys import exit
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, player_file, size, pos):
        super().__init__()
        self.gravity = 0
        self.player_surf = pygame.image.load(player_file).convert_alpha()
        self.player_surf = pygame.transform.scale(self.player_surf, size)
        self.rect = self.player_surf.get_rect(midbottom=pos)
        self.image = self.player_surf

    def jump(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 250:
            self.gravity = 0
            self.rect.bottom = 250

    def space_bottom(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom == 250:
            self.gravity = -20

    def update(self):
        self.jump()
        self.space_bottom()

class NPS(pygame.sprite.Sprite):
    def __init__(self, file_name, scale):
        super().__init__()
        self.image = pygame.image.load(file_name).convert_alpha()
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(800, 1000)
        self.rect.y = random.randint(200, 270)

    def update(self):
        self.rect.x -= 6
        if self.rect.x <= -100:
            self.kill()

def collision_sprite():
    global score
    collisions = pygame.sprite.spritecollide(player, obstacle_group, False)
    for fish in collisions:
        fish.kill()
        score += 1
        return False
    return True

WIDTH = 728
HEIGHT = 350
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Моя игра")
clock = pygame.time.Clock()

score = 0

sky_surface = pygame.image.load('sky.PNG').convert()
ground_surface = pygame.image.load('ground.PNG').convert()

player = Player('cat.PNG', (90, 90), (100, 250))
player_group = pygame.sprite.GroupSingle(player)

obstacle_group = pygame.sprite.Group()

pit = NPS('pit.PNG', (45, 45))
fish = NPS('fish.PNG', (50, 50))
obstacle_group.add(pit, fish)

# Флаги для состояния игры
running = True
game_active = False

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if game_active:
                if event.key == pygame.K_SPACE:
                    player.space_bottom()
            else:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    score = 0

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 250))

        player_group.draw(screen)
        player_group.update()

        if not obstacle_group:
            pit = NPS('pit.PNG', (45, 45))
            fish = NPS('fish.PNG', (50, 50))
            obstacle_group.add(pit, fish)

        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = collision_sprite()
    else:
        screen.fill((123, 145, 123))

    pygame.display.update()
