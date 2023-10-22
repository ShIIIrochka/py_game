import pygame
from sys import exit
from random import randint
 
class Player(pygame.sprite.Sprite):
    """
    функции для игрока - спрайта кота
    """
    def __init__(self, player_file, size, pos):
                
        """
        :param player_file: имя файла
        :param size: размер игрока
        :param pos: расположение игрока
        :param gravity: скорось гравитации для кота
        """
        self.gravity = 0       
        self.player_surf = pygame.image.load(player_file).convert_alpha()
        self.player_surf = pygame.transform.scale(self.player_surf, size)
        self.player_rect = self.player_surf.get_rect(midbottom = pos)

    def jump(self):
        self.gravity += 1
        self.player_rect.y += self.gravity
        if self.player_rect.bottom >= 250:
            self.player_rect.bottom = 250
        screen.blit(self.player_surf, self.player_rect)

    def space_bottom(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.player_rect.bottom >= 250:
            self.gravity = -20

    def update(self):
        self.jump()
        self.space_bottom()


class NPS(pygame.sprite.Sprite):
    def __init__(self, file_name, scale, midbottom):
                
        """
        :param file_name: имя файла
        :param scale: размер спрайта
        :param midbottom: расположение спрайта
        :param score: счетчик рыбок
        """
                
        self.surf = pygame.image.load(file_name).convert_alpha()
        self.surf = pygame.transform.scale(self.surf, scale)
        self.rect = self.surf.get_rect(midbottom = midbottom)

    #def move(self, speed):

        """
        :param speed: скорость спрайта
        """

     #   self.rect.x -= speed
      #  if self.rect.right <= 0:
       #     self.rect.left = WIDTH

    def update(self):
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100: 
            self.kill()



def collision_sprite():
	if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
		obstacle_group.empty()
		return False
	else: return True

def score_play(): 
    global score
    if player.colliderect(fish):
        score += 1

    text = pygame.font.Font(None, 50)
    score_surf = text.render(f'Score: {score}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (364,50))

    screen.blit(score_surf,score_rect)
    return score

WIDTH = 728
HEIGHT = 350
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

score = 0

# Загрузка и конвертация изображений
sky_surface = pygame.image.load('sky.PNG').convert()
ground_surface = pygame.image.load('ground.PNG').convert()

player = Player('cat.PNG', (90, 90), (100, 250))

pit = NPS('pit.PNG', (45, 45), (728, 270))
start = NPS('cat.stand.PNG', (200, 200), (364, 230))
fish = NPS('fish.PNG', (50, 50), (728, 70))
 
obstacle_group = pygame.sprite.Group()
player = pygame.sprite.GroupSingle()

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
            print("hello")
        else:
            # Перезапуск игры, если игрок проиграл
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                score = 0
 
    if game_active:
        screen.blit(sky_surface, (0, 0))  # Вывод изображения неба на экран
        screen.blit(ground_surface, (0, 250))  # Вывод изображения земли на экран
        score = score_play()

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = collision_sprite()

        # Переключение видимости указателя мыши
        pygame.mouse.set_visible(True)

    else:
        # Если произошло столкновение кота с ямой
        screen.fill((123, 145, 123))  # Заполняем экран зеленым цветом
 
    pygame.display.update()




