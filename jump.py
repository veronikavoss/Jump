from setting import *
from controller import Controller

class Jump:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.controller = Controller(self.screen)
        
        self.loop()
    
    def loop(self):
        while self.running:
            self.event()
            self.update()
    
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self):
        self.controller.update()
        
        self.clock.tick(FPS)
        pygame.display.update()

if __name__ == '__main__':
    game = Jump()
    pygame.quit()