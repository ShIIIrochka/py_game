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




class Player:
    """
    функции для игрока - спрайта кота
    """
    def __init__(self, player_file, size, pos, gravity):
                
        """
        :param player_file: имя файла
        :param size: размер игрока
        :param pos: расположение игрока
        :param gravity: скорось гравитации для кота
        """

        self.gravity = gravity
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
        if keys[pygame.K_SPACE] and self.player_rect.bottom >= 300:
            self.gravity = -20

    def update(self):
        self.jump()
        self.space_bottom()





class NPS:
    def __init__(self, file_name, scale, midbottom, score):
                
        """
        :param file_name: имя файла
        :param scale: размер спрайта
        :param midbottom: расположение спрайта
        :param score: счетчик рыбок
        """
                
        self.player_surf = pygame.image.load(file_name).convert_alpha()
        self.player_surf = pygame.transform.scale(self.surf, scale)
        self.player_rect = self.surf.get_rect(midbottom = midbottom)

        self.score = score
        self.score = 0

    def move(self, speed):

        """
        :param speed: скорость спрайта

        """

        self.rect.x -= speed
        if self.rect.right <= 0:
            self.rect.left = 728
        screen.blit(self.surf, self.rect)

    def score_play(self): 

        if self.player_rect.colliderect(self.rect) == True:
            self.score += 1
            

        text = pygame.font.Font(None, 50)
        score_surf = text.render(f'Score: {score}',False,(64,64,64))
        score_rect = score_surf.get_rect(center = (364,50))

        screen.blit(score_surf,score_rect)
        return score
        





pit = NPS('pit.PNG', (45, 45), (728, 270))
start = NPS('cat.stand.PNG', (200, 200), (364, 230))
fish = NPS('fish.PNG', (50, 50), (728, 70))
player = Player('cat.PNG', (90, 90), (100, 250))

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
 


        # Переключение видимости указателя мыши
        pygame.mouse.set_visible(True)

        score = score_play()

        # Обработка столкновения
        if player_rect.colliderect(pit_rect):
            game_active = False
    else:
        # Если произошло столкновение кота с ямой
        screen.fill((123, 145, 123))  # Заполняем экран зеленым цветом
        screen.blit(cat_stand_surf, cat_rect)
        game_active = False
 
    pygame.display.update()




