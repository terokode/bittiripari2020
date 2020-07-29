import random
import pygame

class Meteor:

    def __init__(self, x = 0, y = 0, speed = 1, r = None, color = None):
        self.x = x
        self.y = y
        self.speed = speed
        # Random a circle radios if not set
        self.r = r or random.randint(20, 100)
        # Tuple of RGB color. Random if not set
        self.color = color or (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, round(self.y)), self.r)

