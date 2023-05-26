import pygame

from pygame.math import Vector2


class Snake:
    """This class will be for the snake in the game"""
    def __init__(self, sg_game):
        """This is the attributes for the snake"""
        self.screen = sg_game.screen
        self.settings = sg_game.settings
        
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * self.settings.cell_size)
            y_pos = int(block.y * self.settings.cell_size)
            snake_rect =  pygame.Rect(x_pos,y_pos, self.settings.cell_size,
                                      self.settings.cell_size)
            pygame.draw.rect(self.screen, (180,140,150), snake_rect)
        
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
        
    def add_block(self):
         self.new_block = True