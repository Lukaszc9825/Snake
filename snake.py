import pygame
import datetime


class Snake(object):

    def __init__(self, game):

        self.game = game
        # body params
        self.pos_x = int(game.width / 2)
        self.pos_y = int(game.height / 2)
        self.body_h = 20
        self.body_w = 20
        self.head = pygame.Rect(self.pos_x, self.pos_y, self.body_h, self.body_w)
        self.body = [pygame.Rect(self.pos_x - self.body_w, self.pos_y, self.body_h, self.body_w),
                     pygame.Rect(self.pos_x - 2 * self.body_w, self.pos_y, self.body_h, self.body_w)]

        # direction o movement
        self.dir_x = self.body_w
        self.dir_y = 0

        # count part of body (head is not part of a body)
        self.body_count = 2

        # loading snake textures
        self.head_skin = pygame.image.load('head.jpg').convert()
        self.head_skin = pygame.transform.scale(self.head_skin, (self.body_h, self.body_w))
        self.body_skin = pygame.image.load('skin.jpg').convert()
        self.body_skin = pygame.transform.scale(self.body_skin, (self.body_h, self.body_w))

    def get_body_h(self):
        return self.body_h

    def get_body_w(self):
        return self.body_w

    # check if head coordinates == fruit coordinates
    def eat(self, food, score):
        if self.head.x == food.fruit.x and self.head.y == food.fruit.y:
            food.apple = False
            score.score += 10
            self.grow()

    # add body part after eat fruit
    def grow(self):
        self.body.append(pygame.Rect(self.body[self.body_count - 1].x, self.body[self.body_count - 1].y, self.body_h, self.body_w))
        self.body_count += 1

    # check if snake coordinates == end of the screen or his body
    def crush(self, food, score):
        if self.head.x <= 0 - self.body_w or self.head.x >= 1280 or self.head.y <= 40 - self.body_h or self.head.y >= 720:
            self.head = pygame.Rect(self.pos_x, self.pos_y, self.body_h, self.body_w)
            self.body = [pygame.Rect(self.pos_x - self.body_w, self.pos_y, self.body_h, self.body_w),
                         pygame.Rect(self.pos_x - 2 * self.body_w, self.pos_y, self.body_h, self.body_w)]
            food.apple = False
            score.score = 0
            score.start = datetime.datetime.now()
            self.body_count = 2
            if self.dir_x == - self.body_w:
                self.dir_x = self.body_w

        for i in range(len(self.body), 0, -1):

            if self.head.x == self.body[i-1].x and self.head.y == self.body[i-1].y:
                self.head = pygame.Rect(self.pos_x, self.pos_y, self.body_h, self.body_w)
                self.body = [pygame.Rect(self.pos_x - self.body_w, self.pos_y, self.body_h, self.body_w),
                             pygame.Rect(self.pos_x - 2 * self.body_w, self.pos_y, self.body_h, self.body_w)]
                food.apple = False
                self.body_count = 2
                score.score = 0
                score.start = datetime.datetime.now()
                if self.dir_x == - self.body_w:
                    self.dir_x = self.body_w
                break

    def draw(self):
        # Drawing
        self.game.screen.blit(self.head_skin, (self.head.x, self.head.y))
        for i in range(len(self.body) - 1, -1, -1):
            self.game.screen.blit(self.body_skin, (self.body[i].x, self.body[i].y))