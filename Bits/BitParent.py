import pygame


class BitParent:
    def __init__(self):
        self.x
        self.y

    def draw(self):
        pygame.draw.circle()

    def doSetX(self, x):
        self.x = x

    def doSetY(self, y):
        self.y = y

    def doGetX(self):
        return self.x

    def doGetY(self):
        return self.y
