import pygame

class Bullet:

    def __init__(self, x = 0, y = 0, speed = 0.75):
        self.x = x
        self.y = y
        self.speed = speed
        self.img = pygame.image.load('bullet.png')

    def draw(self, screen):
        self.y = self.y - self.speed
        screen.blit(self.img, (self.x, self.y))