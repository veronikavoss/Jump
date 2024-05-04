from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((CHARACTER_SIZE))
        self.image.fill('blue')
        self.direction_x, self.direction_y = pygame.Vector2(0,0)
        self.rect = self.image.get_rect(topleft=position)
        self.status = 'standby'
        self.move_speed = 0
        self.jump_speed = 10
    
    def set_status(self):
        if self.direction_x != 0:
            self.status = 'move'
        else:
            self.status = 'standby'
    
    def set_jump(self):
        self.direction_y += self.jump_speed
    
    def update(self):
        self.set_status()
        self.rect.x += self.direction_x * self.move_speed
        self.direction_y += self.jump_speed
        print(self.status, self.direction_x)