import pygame 
import sys

from pygame.math import Vector2

from fruit import Fruit
from settingsg import Settings
from snake import Snake 

class SnakeGame:
    """this is the main game object"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.cell_size * self.settings.cell_number
                                               , self.settings.cell_size * self.settings.cell_number))
        
        pygame.display.set_caption("Snake Game ")
        
        self.fruit = Fruit(self)
        self.snake = Snake(self)
        self.bg_color = pygame.Color('Green')
        
        self.screen_update = pygame.USEREVENT
        pygame.time.set_timer(self.screen_update, 150)
        
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        
    def _check_keydown(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == self.screen_update:
                self.snake.move_snake()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if ai.snake.direction.y != 1:
                        self.snake.direction = Vector2(0, -1)
                
                if event.key == pygame.K_s:
                        if ai.snake.direction.y != -1:
                            self.snake.direction = Vector2(0, 1)
                
                if event.key == pygame.K_d:
                        if ai.snake.direction.x != -1:
                            self.snake.direction = Vector2(1, 0)
                
                if event.key == pygame.K_a:
                        if ai.snake.direction.x != 1:
                            self.snake.direction = Vector2(-1, 0)
                    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()     
            
    def game_over(self):
          pygame.quit()
          sys.exit()
          
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < self.settings.cell_number:
            self.game_over()
        elif not 0 <= self.snake.body[0].y < self.settings.cell_number:
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
            
    
    def run_game(self):
        while True:
            self._check_keydown()
            self.check_collision()
            self.check_fail()
            self.screen.fill(self.bg_color)
            self.draw_elements()
            pygame.display.update()
            
if __name__ == '__main__':
    ai = SnakeGame()
    ai.run_game() 
