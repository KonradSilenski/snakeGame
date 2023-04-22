import pygame
from Bits.SnakeHead import SnakeHead
from Bits.Food import Food
from Colors import Colors
import pygame.midi


# Handler class for dealing with game logic
class Handler:
    def __init__(self):
        # Set initial number of snake bits
        self.snakeBits = 1
        # Create new SnakeHead class instance
        self.snake = SnakeHead(90, 90)
        # Set array of snake bits; First bit to be stored is SnakeHead
        self.bitsList = [(self.snake.doGetX(), self.snake.doGetY())]
        # Create new Food
        self.food = Food(self)
        # Set boolean variable for handling game over states
        self.isGameOver = False
        # Set initial score
        self.score = 0

    # Draws defined objects on screen
    def draw(self, screen):
        # Go through list of snake bits in bitsList array and draw each one at their defined positions,
        # barring SnakeHead
        for index, bit in enumerate(self.bitsList, start=1):
            if len(self.bitsList) != 1:
                pygame.draw.rect(screen, Colors.getColor('GREEN'), ((bit[0] - 10, bit[1] - 10), (20, 20)), width=0)

        # Draw snake head
        self.snake.draw(screen)
        # Draw food
        self.food.draw(screen)

    # Checks for collisions with food; If true, generates new food and new snake bit, adds 10 points and speeds up snake
    def doCheckCollision(self):
        if self.food.doGetPosition() == (self.snake.doGetX(), self.snake.doGetY()):
            sound = pygame.mixer.Sound(file="food_get.ogg")
            sound.play()
            self.food.doGenerateNewFood(self)
            self.doCreateBit()
            self.score += 10
            if not self.snake.speed <= self.snake.MAX_SPEED:
                self.snake.speed -= 5
            else:
                pass

    # Updates in game objects
    def tick(self):
        # Check if defined amount of milliseconds have passed
        self.snake.doCheckTimer(self)
        # Check for collision with food
        self.doCheckCollision()

    # Returns SnakeHead instance
    def doGetSnake(self):
        return self.snake

    # Returns snakeBits array
    def doGetBitList(self):
        return self.bitsList

    # Returns game over state
    def isOver(self):
        return self.isGameOver

    # Creates new snake bit
    def doCreateBit(self):
        # Grab coordinates of last bit in bitsList
        newBit = self.bitsList[-1]
        newBit = (newBit[0], newBit[1])
        # Add new bit to bitsList
        self.bitsList.append(newBit)

    # Goes through bitsList in reversed order and passes coordinates from first bit to last
    def doUpdateBits(self):
        # If bitsList has only one bit, pass
        if len(self.bitsList) == 1:
            pass
        self.bitsList[0] = (self.snake.doGetX(), self.snake.doGetY())
        newIndex = len(self.bitsList) - 1
        for index, bit in enumerate(reversed(self.bitsList)):
            if index < len(self.bitsList) - 1:
                self.bitsList[newIndex] = self.bitsList[newIndex - 1]
                newIndex -= 1
            else:
                pass
