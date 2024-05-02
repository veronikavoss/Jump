from setting import *
from map import Map
from player import Player

class Controller:
    def __init__(self, screen):
        self.screen = screen
        self.game_status = 'ready'
        self.level = 1
        self.key_pressed = False
        self.mouse_pressed = False
        self.set_font()
        # self.reset_map()
        self.load_map()
        self.edit_mode = False
        self.map_element = pygame.sprite.GroupSingle()
        self.map_element_selected = ''
    
    def key_status(self):
        if self.key_input.count(1) == 0:
            self.key_pressed = False
        else:
            self.key_pressed = True
        if self.mouse_input[0]:
            self.mouse_pressed = True
        else:
            self.mouse_pressed = False
    
    def set_font(self):
        self.logo = pygame.font.Font(None, 180).render('JUMP', True, 'blue')
        self.logo_rect = self.logo.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//3))
        self.press_key = pygame.font.Font(None, 80).render('Press SPACE Key', True, 'blue')
        self.press_key_rect = self.press_key.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
    
    # map setting
    def reset_map(self):
        self.map_datum = {
            f'{self.level}':[['_' for _ in range(STAGE_WIDTH // TILE_X)] for _ in range(STAGE_HEIGHT // TILE_Y)]}
        self.write_map(self.map_datum[str(self.level)])
    
    def write_map(self, data):
        with open(os.path.join(MAP_PATH, f'level-{self.level}.txt'), 'w') as w:
            for line in data:
                formatted_line = ''.join(line) + '\n'  # 내부 문자열을 하나의 문자열로 변환
                w.write(formatted_line)  # 형식이 지정된 줄을 파일에 씁니다
    
    def load_map(self):
        self.map = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.map_data = []
        
        with open(os.path.join(MAP_PATH, f'level-{self.level}.txt'), 'r') as f:
            for line in f:
                self.map_data.append(list(line.strip()))
        self.draw_map()
    
    def draw_map(self):
        self.map.empty()
        self.player.empty()
        for row, data_list in enumerate(self.map_data):
            for column, data in enumerate(data_list):
                if data == '1':
                    self.map.add(Map(1, (column * TILE_X, row * TILE_Y)))
                elif data == '2':
                    self.map.add(Map(2, (column * TILE_X, row * TILE_Y)))
                elif data == 'P':
                    self.player.add(Player((column * TILE_X, row * TILE_Y)))
    
    # key settings
    def set_ready_key_input(self):
        if self.game_status == 'ready':
            if self.key_input[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]:
                self.game_status = 'playing'
    
    def set_player_key_input(self):
        if not self.edit_mode and self.key_input[pygame.K_e]:
            self.edit_mode = True
        if self.player:
            if self.key_input[pygame.K_RIGHT]:
                if self.player.sprite.rect.right <= (SCREEN_WIDTH // 2) + (CHARACTER_X // 2):
                    self.player.sprite.direction_x = 1
                else:
                    self.player.sprite.direction_x = 0
                    self.set_map_movement(-1)
            elif self.key_input[pygame.K_LEFT]:
                if self.player.sprite.rect.left >= (SCREEN_WIDTH // 2) + (CHARACTER_X // 2):
                    self.player.sprite.direction_x = -1
                else:
                    self.player.sprite.direction_x = 0
                    self.set_map_movement(1)
            else:
                self.player.sprite.direction_x = 0
    
    def set_map_movement(self, direction):
        if self.map:
            for map in self.map:
                map.rect.x += 3 * direction
    
    def edit_map_key_input(self):
        if self.key_input[pygame.K_ESCAPE]:
            self.edit_mode = False
            self.map_element.empty()
        elif self.key_input[pygame.K_RIGHT]:
            self.edit_map_movement(1)
        elif self.key_input[pygame.K_LEFT]:
            self.edit_map_movement(-1)
        elif self.key_input[pygame.K_p]:
            self.map_element_selected = 'P'
            self.map_element.add(Player(self.mouse))
        elif self.key_input[pygame.K_1]:
            self.map_element_selected = '1'
            self.map_element.add(Map(1, self.mouse))
        elif self.key_input[pygame.K_2]:
            self.map_element_selected = '2'
            self.map_element.add(Map(2, self.mouse))
        elif self.key_input[pygame.K_r]:
            self.reset_map()
            self.load_map()
        elif self.key_input[pygame.K_s]:
            self.write_map(self.map_data)
    
    def edit_map_movement(self, direction):
        if self.map:
            for map in self.map:
                map.rect.x += TILE_X * direction
    
    def edit_map_mouse_input(self):
        if self.map_element:
            mouse_x, mouse_y = self.mouse
            x = mouse_x // TILE_X
            y = mouse_y // TILE_Y
            self.map_element.sprite.rect.topleft = x * TILE_X, y * TILE_Y
        
            if self.mouse_input[0]:
                print(x,y,':',self.map_data[y][x])
                if self.map_data[y][x] != '_':
                    self.map_data[y][x] = '_'
                    pygame.time.delay(100)
                else:
                    if self.map_element_selected == 'P':
                        self.map_data[y][x] = 'P'
                    elif self.map_element_selected == '1':
                        self.map_data[y][x] = '1'
                    elif self.map_element_selected == '2':
                        self.map_data[y][x] = '2'
                self.draw_map()
    
    # set game mode
    def set_ready(self):
        self.screen.fill('yellow')
        self.screen.blit(self.logo, self.logo_rect)
        if pygame.time.get_ticks() // 1000 % 2 == 0:
            self.screen.blit(self.press_key, self.press_key_rect)
        
        self.set_ready_key_input()
    
    def set_playing(self):
        self.screen.fill('white')
        if not self.edit_mode:
            self.set_player_key_input()
            # self.map.update()
        elif self.edit_mode:
            for row in range(SCREEN_HEIGHT // TILE_X):
                for column in range(SCREEN_WIDTH // TILE_Y):
                    pygame.draw.rect(self.screen, 'gray', (column * TILE_X, row * TILE_Y, TILE_X, TILE_Y),1)
            self.edit_map_key_input()
            self.edit_map_mouse_input()
            self.map_element.draw(self.screen)
        self.map.draw(self.screen)
        self.player.update()
        self.player.draw(self.screen)
    
    # update run
    def update(self):
        self.key_input = pygame.key.get_pressed()
        self.mouse_input = pygame.mouse.get_pressed()
        self.key_status()
        self.mouse = pygame.mouse.get_pos()
        # game mode
        if self.game_status == 'ready':
            self.set_ready()
        elif self.game_status == 'playing':
            self.set_playing()
        # print(self.key_pressed, self.mouse_pressed)