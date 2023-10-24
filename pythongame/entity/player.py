
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