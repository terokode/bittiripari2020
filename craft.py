import pygame
from bullet import Bullet

class Craft:

    # Direction constants
    HALT = "HALT"
    LEFT = "LEFT",
    RIGHT = "RIGHT"

    def __init__(self, x = 0, y = 0, speed = 1):
        self.x = x
        self.y = y
        self.speed = speed
        self.img = pygame.image.load('craft.png')
        self.direction = Craft.HALT
        self.bullet = None

    def moveRight(self):
        self.x += self.speed  # self.x = self.x + self.speed

        # Don't let go outside
        if self.x >= 800 - 64:
            self.x = 800 - 64

    def moveLeft(self):
        self.x -= self.speed  # self.x = self.x - self.speed

        # Don't let go outside
        if self.x <= 0:
            self.x = 0

    def fire(self):
        # Don't fire if the bullet is visible
        if self.bullet is None:
            #  Init a new bullet
            self.bullet = Bullet(self.x + 16, self.y + 10, 10) 

    def draw(self, screen):

        if self.direction == Craft.LEFT:
            self.moveLeft()
        elif self.direction == Craft.RIGHT:
            self.moveRight()

        screen.blit(self.img, (self.x, self.y))

        # If the bullet is not visible (fired) we don't draw it on the screen
        if not self.bullet is None:
            self.bullet.draw(screen)
            # When the bullet reaches the top (y-coordinate 0) of the screen
            # set the bullet available for a new firing. 
            if self.bullet.y <= 0:
                self.bullet = None