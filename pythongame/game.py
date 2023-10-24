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
        :param size: размер спрайта
        :param pos: расположение спрайта
        """

        super().__init__()
        self.gravity = 0
        self.player_surf = pygame.image.load(player_file).convert_alpha()
        self.player_surf = pygame.transform.scale(self.player_surf, size)
        self.rect = self.player_surf.get_rect(midbottom=pos)
        self.image = self.player_surf

    def jump(self):
        """
        описание прыжка игрока
        """
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 250:
            self.gravity = 0
            self.rect.bottom = 250

    def space_bottom(self):
        """
        если нажат пробел, спрайт игрока прыгает
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom == 250:
            self.gravity = -20


    def update(self):
        self.jump()
        self.space_bottom()


class NPS(pygame.sprite.Sprite):

    def __init__(self, file_name, scale, speed, y_range):
        """
        :param file_name: имя файла
        :param scale: размер спрайта
        :param speed: скорость спрайта
        :param y_range: диапазон генерации случайной координаты по оси y
        """
        super().__init__()
        self.image = pygame.image.load(file_name).convert_alpha()
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.x = randint(728, 1100)
        self.rect.y = randint(y_range[0], y_range[1])  # Генерация случайной координаты Y в указанном диапазоне
        self.speed = randint(speed[0], speed[1])

    def update(self):
        """
        движение спрайтов
        """
        self.rect.x -= self.speed
        if self.rect.x <= -100:
            self.kill()


def collision_sprite() -> bool:
    """
    функция для подсчета score и проверок столкновений спрайтов
    """

    global score

    collisions = pygame.sprite.spritecollide(player, obstacle_group, True)

    for sprite in collisions:
        if sprite in fish_instances:
            fish_instances.remove(sprite)
            score += 1

        elif sprite in pit_instances:
            obstacle_group.empty()
            return False 

    score_surf = test_font.render(f'Score: {score}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)

    return True

def obstaclegroup() -> None:
        
        global pit_instances, fish_instances
        
        fish_instances = [NPS('graphics/fish.PNG', (50, 50), (5, 7), (70, 110)) for i in range(4)]
        pit_instances = [NPS('graphics/pit.PNG', (45, 45), (4, 6), (230, 230)) for i in range(2)]   
        obstacle_group.add(*fish_instances, *pit_instances)


#параметры игрового окна
WIDTH = 800
HEIGHT = 400
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #создание окна игры
pygame.display.set_caption("My Game") #название игры
clock = pygame.time.Clock()

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

score = 0

# Загрузка и конвертация изображений
sky_surface = pygame.image.load('graphics/sky.PNG').convert() #размер изображения 1700 на 289
sky_surface = pygame.transform.scale(sky_surface, (WIDTH, 289))
ground_surface = pygame.image.load('graphics/ground.PNG').convert() #размер изображения 2015 на 816
ground_surface = pygame.transform.scale(ground_surface, (WIDTH, HEIGHT//2))

player = Player('graphics/cat.PNG', (90, 90), (100, 250))



start_surf = pygame.image.load('graphics/cat.stand.PNG').convert_alpha()
start_surf = pygame.transform.scale(start_surf, (200, 200))
start_rect = start_surf.get_rect(center = (400,200))

#группы
player_group = pygame.sprite.GroupSingle(player)

obstacle_group = pygame.sprite.Group()
obstaclegroup()

# Флаги для состояния игры
running = True
game_active = False

game_message = test_font.render('Press space to run',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,330))

while running:
    #держим цикл на правильной скорости
    clock.tick(FPS)

    for event in pygame.event.get():
        #обработка события закрытия окна
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

            obstaclegroup()

            
        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = collision_sprite()
    else:
        screen.fill((123, 145, 123))
        screen.blit(start_surf, start_rect)
        screen.blit(game_message,game_message_rect)

    score_surf = test_font.render(f'Score: {score}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)




    pygame.display.update()
