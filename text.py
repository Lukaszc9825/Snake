import pygame

class Text(object):

    def __init__(self, game):
        self.game = game
        self.font1 = pygame.font.SysFont('Arial.ttf', 45)
        self.font2 = pygame.font.SysFont('Arial.ttf', 30)
        self.score_info = "Actual score: "
        self.time_info = "Time alive: "
        self.text2 = self.font1.render(self.score_info, 1, (0, 0, 0))
        self.text3 = self.font1.render(self.time_info, 1, (0, 0, 0))

    def draw(self, score, time):
        # Drawing
        self.text1 = self.font1.render(str(score), 1, (0, 0, 0))
        self.text4 = self.font1.render(str(time), 1, (0, 0, 0))
        self.game.screen.blit(self.text1, (210, 6))
        self.game.screen.blit(self.text2, (5, 5))
        self.game.screen.blit(self.text3, (400, 5))
        self.game.screen.blit(self.text4, (600, 5))