import pygame
import random

from pygame.math import Vector2


class Fruit():
    """This will be our fruit object"""
    
    def __init__(self, sg_game):
        
        self.screen = sg_game.screen
        self.screen_rect= self.screen.get_rect()
        self.settings = sg_game.settings
        
        self.randomize()
       
    def randomize(self):
        self.x = random.randint(0, self.settings.cell_number - 1)
        self.y = random.randint(0, self.settings.cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * self.settings.cell_size),
                                 int(self.pos.y * 
                                     self.settings.cell_size), 
                                 self.settings.cell_size,self.settings.cell_size)
        pygame.draw.rect(self.screen, (250,250,250), fruit_rect)
