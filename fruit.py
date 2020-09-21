import pygame
import random


class Fruit(object):

    def __init__(self, game):

        self.game = game
        # coordinates of fruit
        self.x = 0
        self.y = 0
        self.w = game.snake.body_w
        self.h = game.snake.body_h
        self.fruit = pygame.Rect(self.x, self.y, self.w, self.h)
        self.apple = False  # False == there is no apple on screen, other function have to generate it

        self.fruit_skin = pygame.image.load('images/fruit.jpg').convert()
        self.fruit_skin = pygame.transform.scale(self.fruit_skin, (self.h, self.w))

    # put the fruit into a random coordinates and check if they aren't the same as snake position
    def put_fruit(self):

        if not self.apple:
            self.fruit.x = random.randrange(0 + self.w, self.game.width - self.w, self.w)
            self.fruit.y = random.randrange(0 + self.h, self.game.height - self.h, self.h)

            for i in range(len(self.game.snake.body) - 1, -1, -1):
                if self.game.snake.body[i].x == self.fruit.x and self.game.snake.body[i].y == self.fruit.y:
                    self.apple = False
                    break

            if self.game.snake.head.x == self.fruit.x and self.game.snake.head.y == self.fruit.y:
                self.apple = False

            elif self.fruit.y <= 40:
                self.apple = False
            else:
                self.apple = True

    def draw(self):
        self.game.screen.blit(self.fruit_skin, (self.fruit.x, self.fruit.y))