from setting import *

class Map(pygame.sprite.Sprite):
    def __init__(self, number, position):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE))
        self.image.fill(self.map_element(number))
        self.rect = self.image.get_rect(topleft=position)
    
    def map_element(self, number):
        self.element = {'color':['brown', 'black']}
        return self.element['color'][number-1]
    
    def set_movement(self, speed):
        self.rect.x += speed
    
    def update(self):
        self.set_movement()