from Handler import Handler
from Colors import Colors
import pygame
import sys


#  Game setup and control class
class GameInit:

    def __init__(self, width, height):
        # Define window size and create canvas
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game')
        # Setup animation time counter
        self.timer = pygame.time.get_ticks()
        # Define initial program mode ("MENU", "GAME", "GOVER")
        self.mode = "MENU"
        # Set boolean variable for animating menu prompt
        self.menuPromptShow = True
        # Create new Handler class instance; Create two new snake bits
        self.handler = Handler()
        self.handler.doCreateBit()
        self.handler.doCreateBit()
        # Setup game fonts
        self.font = pygame.font.Font('gbfont.ttf', 19)
        self.menufnt = pygame.font.Font('gbfont.ttf', 32)
        # Set text to be displayed on screen
        self.text = self.font.render('Score: ' + str(self.handler.score), True, Colors.getColor('LGREEN'))
        self.menutxt = self.menufnt.render('Snake Game', True, Colors.getColor('GREEN'))
        self.menutxtPrompt = self.font.render('Press space', True, Colors.getColor('GREEN'))
        self.menutxtPrompt2 = self.font.render('to continue', True, Colors.getColor('GREEN'))
        hs = open("highscore", "r")
        OLDHS = hs.read()
        self.menuHighscore = self.font.render('Highscore:', True, Colors.getColor('GREEN'))
        self.Highscore = self.font.render(OLDHS, True, Colors.getColor('GREEN'))
        self.gameOverPrompt = self.font.render('Press space', True, Colors.getColor('GREEN'))
        self.gameOverPrompt2 = self.font.render('to restart', True, Colors.getColor('GREEN'))

    # Returns screen width
    def getWidth(self):
        return self.width

    # Returns screen height
    def getHeight(self):
        return self.height

    # Draws defined objects on screen
    def draw(self):
        # Game mode; Draws snake and score
        if self.mode == "GAME":
            # Screen refresh
            self.window.fill(Colors.getColor('DGREEN'))
            # Draw score box and score
            self.window.fill(Colors.getColor('GREEN'), ((0, 220), (320, 20)))
            self.window.blit(self.text, ((5, 218), (320, 20)))
            # Draw snake and food
            self.handler.draw(self.window)
        # Menu mode; Draws Title and prompt
        elif self.mode == "MENU":
            # Screen refresh
            self.window.fill(Colors.getColor('DGREEN'))
            # Draw title
            self.window.blit(self.menutxt, ((10, 80), (320, 32)))
            self.window.blit(self.menuHighscore, (75, 10))
            self.window.blit(self.Highscore, (135, 30))
            # Draw prompt
            if self.menuPromptShow:
                self.window.blit(self.menutxtPrompt, ((65, 130), (320, 32)))
                self.window.blit(self.menutxtPrompt2, ((65, 150), (320, 32)))
        # Game over mode; Draws Score and prompt
        elif self.mode == "GOVER":
            # Screen refresh
            self.window.fill(Colors.getColor('DGREEN'))
            # Draw Score
            self.window.fill(Colors.getColor('GREEN'), ((0, 220), (320, 20)))
            self.window.blit(self.text, ((5, 218), (320, 20)))
            # Draw prompt
            if self.menuPromptShow:
                self.window.blit(self.gameOverPrompt, ((65, 90), (320, 32)))
                self.window.blit(self.gameOverPrompt2, ((70, 110), (320, 32)))

    # Updates game
    def tick(self):
        # When in menu or game over screen update menuPromptShow variable to animate prompt
        if self.mode == "MENU" or self.mode == "GOVER":
            # Get current runtime in milliseconds
            newTimer = pygame.time.get_ticks()
            # If 1000 milliseconds have passed, update menuPromptShow variable to either true or false
            if newTimer - self.timer >= 1000:
                if not self.menuPromptShow:
                    self.timer = pygame.time.get_ticks()
                    self.menuPromptShow = True
                else:
                    self.timer = pygame.time.get_ticks()
                    self.menuPromptShow = False

        # Update game objects; When in game, update score; Checks if the game is over
        elif self.mode == "GAME":
            # Update game objects
            self.handler.tick()
            # Update score
            self.text = self.font.render('Score: ' + str(self.handler.score), True, Colors.getColor('LGREEN'))
            # If game is over, set game mode to "GOVER"; Reset menuPromptShow variable
            if self.handler.isOver():
                hs = open("highscore", "r")
                OLDHS = hs.read()
                if self.handler.score > int(OLDHS):
                    hs = open("highscore", "w")
                    hs.write(str(self.handler.score))
                hs.close()
                self.mode = "GOVER"
                self.timer = pygame.time.get_ticks()
                self.menuPromptShow = True


running = True

if __name__ == "__main__":
    # Initialize pygame
    pygame.init()
    # Initialize game
    game = GameInit(320, 240)
    # Game loop
    while running:

        # Pygame event loop
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            # Keyboard input
            if event.type == pygame.KEYDOWN:
                # Escape button
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                # Game mode inputs
                if game.mode == "GAME":
                    # Set snake directions
                    # Left direction key
                    if event.key == pygame.K_LEFT and game.handler.doGetSnake().doGetDir() != "RIGHT":
                        game.handler.doGetSnake().doSetDir("LEFT")
                    # Right direction key
                    if event.key == pygame.K_RIGHT and game.handler.doGetSnake().doGetDir() != "LEFT":
                        game.handler.doGetSnake().doSetDir("RIGHT")
                    # Down direction key
                    if event.key == pygame.K_DOWN and game.handler.doGetSnake().doGetDir() != "UP":
                        game.handler.doGetSnake().doSetDir("DOWN")
                    # Up direction key
                    if event.key == pygame.K_UP and game.handler.doGetSnake().doGetDir() != "DOWN":
                        game.handler.doGetSnake().doSetDir("UP")
                # Menu mode inputs
                elif game.mode == "MENU":
                    # Spacebar, begin game
                    if event.key == pygame.K_SPACE:
                        game.mode = "GAME"
                # Game over mode inputs
                elif game.mode == "GOVER":
                    # Spacebar, restart game
                    if event.key == pygame.K_SPACE:
                        game.handler = Handler()
                        game.handler.doCreateBit()
                        game.handler.doCreateBit()
                        game.mode = "GAME"

        game.tick()
        game.draw()
        pygame.display.update()
