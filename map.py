from setting import *

class Map(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((GROUND_SIZE))
        self.image.fill('brown')
        self.rect = self.image.get_rect(topleft=position)