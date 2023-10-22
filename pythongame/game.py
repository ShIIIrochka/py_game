import pygame
from sys import exit
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self, player_file, size, pos):
        super().__init__()
        self.gravity = 0
        self.player_surf = pygame.image.load(player_file).convert_alpha()
        self.player_surf = pygame.transform.scale(self.player_surf, size)
        self.player_rect = self.player_surf.get_rect(midbottom=pos)
        self.image = self.player_surf
        self.rect = self.image.get_rect(midbottom=pos)

    def jump(self):
        self.gravity += 1
        self.player_rect.y += self.gravity
        if self.player_rect.bottom >= 250:
            self.player_rect.bottom = 250

    def space_bottom(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.player_rect.bottom >= 250:
            self.gravity = -20

    def update(self):
        self.jump()
        self.space_bottom()
        self.score_play()

    def score_play(self):
        global score
        if self.player_rect.colliderect(fish.rect):  # Changed 'fish' to 'fish.rect'
            score += 1
        text = pygame.font.Font(None, 50)
        score_surf = text.render(f'Score: {score}', False, (64, 64, 64))
        score_rect = score_surf.get_rect(center=(364, 50))
        screen.blit(score_surf, score_rect)

class NPS(pygame.sprite.Sprite):
    def __init__(self, file_name, scale, midbottom):
        super().__init__()
        self.surf = pygame.image.load(file_name).convert_alpha()
        self.surf = pygame.transform.scale(self.surf, scale)
        self.rect = self.surf.get_rect(midbottom=midbottom)
        self.image = self.surf
        self.rect = self.image.get_rect(midbottom=midbottom)

    def update(self):
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

def collision_sprite():
    return not pygame.sprite.spritecollide(player, obstacle_group, False)  # Changed player.sprite to player

WIDTH = 728
HEIGHT = 350
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

score = 0

sky_surface = pygame.image.load('sky.PNG').convert()
ground_surface = pygame.image.load('ground.PNG').convert()

player = Player('cat.PNG', (90, 90), (100, 250))
obstacle_group = pygame.sprite.Group()
player_group = pygame.sprite.GroupSingle()  # Changed the variable name to 'player_group'

pit = NPS('pit.PNG', (45, 45), (728, 270))
start = Player('cat.stand.PNG', (200, 200), (364, 230))
fish = NPS('fish.PNG', (50, 50), (728, 70))

obstacle_group.add(pit, start, fish)
player_group.add(player)  # Added the player to the player_group

# Flags for game state
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
            print("hello")
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                score = 0

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 250))

        player_group.draw(screen)
        player_group.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = collision_sprite()

        pygame.mouse.set_visible(False)

    else:
        screen.fill((123, 145, 123))

    pygame.display.update()
