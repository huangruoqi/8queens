from UI.components.container import Container

import pygame
from pygame.locals import *  # noqa
from UI.utils import IMAGE

class Block(Container):
    # static code
    images = {
        "empty": pygame.Surface([1, 1], pygame.SRCALPHA),
        "red": pygame.Surface([1,1]),
        "blue": pygame.Surface([1,1]),
        "green": pygame.Surface([1,1]),
        "queen": IMAGE("white_queen.png"),
        "queen_win": IMAGE("queen_win.png"),
    }
    images["red"].fill((255, 100, 100))
    images["blue"].fill((100, 255, 100))
    images["green"].fill((100, 100, 255))

    def __init__(self, width, height, x, y):
        super().__init__(self.images["empty"], width=width, height=height, x=x, y=y)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    def change(self, name):
        self.set_temp_image(self.images[name], width=self.width, height = self.height).set_pos(self.x, self.y)

