import pygame

class Score:
    def __init__(self, score=0):
        self.score = score
        self.x = 10
        self.y = 10
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def increase(self):
        self.score += 1  # self.score = self.score + 1

    def draw(self, screen):
        score_text = "Score: {}".format(self.score)
        rendered = self.font.render(score_text, False, (0,0,0), (255,255,255))
        screen.blit(rendered, (self.x, self.y))
