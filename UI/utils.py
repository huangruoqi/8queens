import pygame
from pygame.locals import *  # noqa
import os
import json
from .sound import Sound

def IMAGE(name, relative=True):
    return pygame.image.load(
        (os.path.join("assets/images/", name) if relative else name)
    )


def SOUND(name, channel):
    return Sound(os.path.join("assets/sounds/", name), channel)


def JSON(name, relative=True):
    with open(
        os.path.join("assets/data/", name) if relative else name,
        encoding="utf8",
    ) as f:
        return json.load(f)

def save_file(pathname, content):
    f = open(os.path.join(pathname), "w", encoding="utf8")
    f.write(content)
    f.close()

class vec(list):
    def __init__(self, x, y=0):
        if isinstance(x, list) or isinstance(x, tuple):
            super().__init__(x)
        else:
            super().__init__([x, y])

    def __getattr__(self, name: str):
        if name == "x":
            return self[0]
        elif name == "y":
            return self[1]

    def __setattr__(self, name: str, value):
        if name == "x":
            self[0] = value
        elif name == "y":
            self[1] = value

    def __str__(self):
        return f"<{self.x}, {self.y}>"

    def __add__(self, other):
        if isinstance(other, vec):
            return vec(self[0] + other[0], self[1] + other[1])
        return None

    def __sub__(self, other):
        if isinstance(other, vec):
            return vec(self[0] - other[0], self[1] - other[1])
        return None

    def __mul__(self, other):
        if isinstance(other, vec):
            return vec(self[0] * other[0], self[1] * other[1])
        else:
            # scalar
            return vec(self[0] * other, self[1] * other)

    # def __mod__(self, other):
    #     if isinstance(other, vec):
    #         # cross product
    #         return self.x*other.y - self.y*other.x
    #     return None

    def __truediv__(self, other):
        if isinstance(other, vec):
            if other[0] * other[1] == 0:
                return None
            return vec(self[0] / other[0], self[1] / other[1])
        else:
            # scalar
            return vec(self[0] / other, self[1] / other)

    def map(self, func):
        return vec(func(self[0]), func(self[1]))

    def unit(self):
        return self / self.length()

    def length(self):
        return (self[0] ** 2 + self[1] ** 2) ** 0.5


class Mouse:
    cursor_arrow = pygame.transform.scale(IMAGE("cursor.png"), (36, 54))
    cursor_hand = pygame.transform.scale(IMAGE("hand.png"), (48, 54))

    def draw(screen, mouse_pos, is_pointer):
        screen.blit(
            Mouse.cursor_hand if is_pointer else Mouse.cursor_arrow,
            mouse_pos - vec(10, 0) if is_pointer else mouse_pos,
        )
        pass
