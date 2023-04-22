import random
from Colors import Colors
import pygame


# Food class for handling food generation
class Food:
    def __init__(self, handler):
        # Set new random coordinates
        self.randX = random.randint(1, 16) * 20
        self.randY = random.randint(1, 11) * 20
        # Assign coordinates to a tuple
        self.position = (self.randX-10, self.randY-10)
        # If current coordinates collide with any snake bit, generate new coordinates
        for bit in handler.doGetBitList():
            if bit == self.position:
                self.doGenerateNewFood(handler)

    # Draws food
    def draw(self, screen):
        pygame.draw.rect(screen, Colors.getColor('GREEN'), ((self.position[0]-8, self.position[1]-8), (16, 16)), width=0)

    # Generates new random coordinates
    def doGenerateNewFood(self, handler):
        self.randX = random.randint(1, 16) * 20
        self.randY = random.randint(1, 11) * 20
        self.position = (self.randX-10, self.randY-10)

        # If coordinates collide with any snake bit, generate new coordinates
        for bit in handler.doGetBitList():
            if bit == self.position:
                self.doGenerateNewFood(handler)

    # Returns food coordinates
    def doGetPosition(self):
        return self.position
