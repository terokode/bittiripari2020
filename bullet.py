import pygame

class Bullet:

    def __init__(self, x = 0, y = 0, speed = 1):
        # Position on the screen (coordinates)
        self.x = x
        self.y = y
        self.speed = speed  # Move px
        self.img = pygame.image.load('bullet.png')

    def draw(self, screen):
        self.y = self.y - self.speed  # Bullet goes up
        screen.blit(self.img, (self.x, self.y))