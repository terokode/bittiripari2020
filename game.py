import math
import random
import pygame
from craft import Craft
from meteor import Meteor
from score import Score

class Game():

    # States of game
    PLAYING = "PLAYING"
    GAMEOVER = "GAMEOVER"

    def __init__(self):
        # Intialize the pygame
        pygame.init()
        # create the screen
        self.screen = pygame.display.set_mode((800, 600))
        # Create an object to help track time
        self.clock = pygame.time.Clock()

        # Set window caption and icon
        pygame.display.set_caption("Meteors")
        icon = pygame.image.load('meteor.png')
        pygame.display.set_icon(icon)

        # Intialize the objects of the game
        self.init_game()
    
    def init_game(self, numMeteors=3):
        # Set a craft
        self.craft = Craft(0, 600-90, 5)
        # Initialize a score object
        self.score = Score()
        # Empty meteors list
        self.meteors = []

        for i in range(0, numMeteors):
            # Add Meteor object to meteors' list
            self.meteors.append(self.init_meteor())

        self.state = Game.PLAYING

    def init_meteor(self):
        # Create a new meteor obbject. Random position of meteor on x-axis (marginal 10 px) and random speed
        meteor = Meteor(random.randint(10, 790), 0, random.uniform(0.75, 2.50))
        return meteor

    def is_hit(self, meteor, bullet):
        # Calculate if the top of the bullet is in a meteor radious
        # Must to fix bullet coordinate to center of bullet (+16 px)
        distance = math.sqrt(math.pow(meteor.x - (bullet.x + 16), 2) + (math.pow(meteor.y - bullet.y, 2)))

        return distance <= meteor.r
        # is same as
        # if distance <= meteor.r:
        #    return True
        # else:
        #    return False

    def run(self):

        # Game Loop
        running = True
        while running:

            # RGB = Red, Green, Blue
            # Black background
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # if keystroke is pressed check it
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.craft.direction = Craft.LEFT
                    elif event.key == pygame.K_RIGHT:
                        self.craft.direction = Craft.RIGHT
                    elif event.key == pygame.K_SPACE:
                        self.craft.fire()
                    elif event.key == pygame.K_n:
                        # Quit
                        running = False
                    elif event.key == pygame.K_y:
                        # Start a new game
                        self.init_game()
                elif event.type == pygame.KEYUP:
                    # When narrow key is up again then stop the craft
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.craft.direction = Craft.HALT

            if self.state == Game.GAMEOVER:
                # Define GAME OVER text
                gameover_font = pygame.font.Font('freesansbold.ttf', 64)
                gameover_text = "GAME OVER"
                gameover = gameover_font.render(gameover_text, True, (255, 255, 255))

                # Define info text
                info_font = pygame.font.Font('freesansbold.ttf', 16)
                info_text = "Your score {}. Play again (press y/n)?".format(self.score.score)
                info = info_font.render(info_text, True, (255, 255, 255)) 

                # Display texts on the screen
                self.screen.blit(gameover, (200, 250))
                self.screen.blit(info, (200, 320))

            # Assume that state is PLAYING (if not GAMEOVER)
            else:
                # Draw and make checks for each meteor
                for index, meteor in enumerate(self.meteors):
                    meteor.y += meteor.speed  # mateor.y = mateor.y + meteor.speed
                    meteor.draw(self.screen)

                    # If the bullet is on the screen
                    if not self.craft.bullet is None:
                        # Is the bullet hit the meteor
                        if self.is_hit(meteor, self.craft.bullet):
                            # Exempt the bullet
                            self.craft.bullet = None
                            # Calculate a hit                            
                            self.score.increase()
                            # Replace a hitten meteor with a new one
                            self.meteors[index] = self.init_meteor()

                    # if a mateor goes over buttom board -> Game over
                    if meteor.y > 600 + meteor.r:
                        self.state = Game.GAMEOVER

                # Show the craft and the score display on the screen
                self.craft.draw(self.screen)
                self.score.draw(self.screen)

            # Draw objects on the screen
            pygame.display.update()
            # framerate: frames per second
            self.clock.tick(60)

game = Game()
game.run()