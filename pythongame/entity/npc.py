
class NPC(pygame.sprite.Sprite):

    def __init__(self, file_name, scale, speed, x_range, y_range):
        """
        :param file_name: имя файла
        :param scale: размер спрайта
        :param speed: скорость спрайта
        :param x_range: диапазон генерации случайной координаты по оси x
        :param y_range: диапазон генерации случайной координаты по оси y
        """
        super().__init__()
        self.image = pygame.image.load(file_name).convert_alpha()
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.x = randint(x_range[0], x_range[1])
        self.rect.y = randint(y_range[0], y_range[1])  # Генерация случайной координаты Y в указанном диапазоне
        self.speed = randint(speed[0], speed[1])

    def update(self):
        """
        движение спрайтов
        """
        self.rect.x -= self.speed
        if self.rect.x <= -100:
            self.kill()