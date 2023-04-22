from Bits.BitParent import BitParent
from Colors import Colors
import pygame


# SnakeHead class for handling movement and game updates
class SnakeHead(BitParent):
    def __init__(self, x, y):
        self.sound = pygame.mixer.Sound(file="game_over.ogg")
        # Set direction
        self.dir = "RIGHT"
        # Set coordinates
        self.x = x
        self.y = y
        # Set initial timer
        self.timer = pygame.time.get_ticks()
        # Set input blocker variable
        self.newInputAllowed = True
        # Set current speed and max speed
        self.speed = 300
        self.MAX_SPEED = 100

    # Draws snake head in specified canvas
    def draw(self, screen):
        pygame.draw.rect(screen, Colors.getColor('LGREEN'), ((self.x-10, self.y-10), (20, 20)), width=0)

    # Sets new direction; Blocks new input
    def doSetDir(self, dir):
        if self.newInputAllowed:
            self.dir = dir
            self.newInputAllowed = False

    # Updates snake head position based on direction and defined distance
    def setPos(self, dist):
        # Unblock input
        if not self.newInputAllowed:
            self.newInputAllowed = True
        if self.dir == "RIGHT":
            super().doSetX(super().doGetX() + dist)
        elif self.dir == "LEFT":
            super().doSetX(super().doGetX() - dist)
        elif self.dir == "UP":
            super().doSetY(super().doGetY() - dist)
        elif self.dir == "DOWN":
            super().doSetY(super().doGetY() + dist)

    # Returns snake head's direction
    def doGetDir(self):
        return self.dir

    # Checks if set amount of milliseconds have passed;
    # If true, updates snake bits and set new position for snake head
    def doCheckTimer(self, handler):
        newTimer = pygame.time.get_ticks()
        if newTimer - self.timer >= self.speed:
            self.timer = pygame.time.get_ticks()
            handler.doUpdateBits()
            self.setPos(20)
            # Check if snake head is out of bounds;
            # If true, go to game over screen
            if self.doGetX() < 0 or self.doGetX() > 320:
                handler.isGameOver = True
                self.sound.play()
            elif self.doGetY() < 0 or self.doGetY() > 220:
                handler.isGameOver = True
                self.sound.play()
            # Check if snake head collides with snake bit;
            # If true, go to game over screen
            for ind, col in enumerate(handler.bitsList):
                if col == (self.doGetX(), self.doGetY()) and ind != 0:
                    self.sound.play()
                    handler.isGameOver = True
