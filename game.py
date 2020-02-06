import pygame
import sys
from snake import Snake
from fruit import Fruit
from text import Text
import datetime




class Game(object):

    def __init__(self):
        pygame.init()

        # screen size
        self.height = 720
        self.width = 1280
        self.arena_h = 680
        self.arena_w = 1280

        # crating screen and loading textures
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake by Lukasz Ciesluk")
        self.background = pygame.image.load("background.jpg").convert()

        # ticking variables
        self.clock = pygame.time.Clock()
        self.dt = 0.0

        self.start = datetime.datetime.now()
        self.dt1 = 0.0

        # score counter
        self.score = 0

        # speed of the snake
        self.v = 14.0

        self.snake = Snake(self)
        self.food = Fruit(self)
        self.text = Text(self)

        # game loop
        while True:
            self.events()
            self.ticking()
            self.snake.eat(self.food, self)
            self.food.put_fruit()
            self.snake.crush(self.food, self)
            self.screen.fill((0, 0, 0))
            self.draw()
            self.food.draw()
            self.snake.draw()
            self.text.draw(self.score, self.dt1)
            pygame.display.flip()

    # handle events
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                if self.snake.dir_x != - self.snake.body_w:
                    self.snake.dir_x = self.snake.body_w
                    self.snake.dir_y = 0

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                if self.snake.dir_x != self.snake.body_w:
                    self.snake.dir_x = -self.snake.body_w
                    self.snake.dir_y = 0

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                if self.snake.dir_y != self.snake.body_h:
                    self.snake.dir_x = 0
                    self.snake.dir_y = -self.snake.body_h

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                if self.snake.dir_y != -self.snake.body_h:
                    self.snake.dir_x = 0
                    self.snake.dir_y = self.snake.body_h

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.snake.grow()

    def ticking(self):

        self.dt += self.clock.tick() / 1000.0
        self.dt1 = (datetime.datetime.now() - self.start).seconds
        while self.dt > 1 / self.v:

            for i in range(len(self.snake.body) - 1, -1, -1):
                if i == 0:
                    self.snake.body[i].x = self.snake.head.x
                    self.snake.body[i].y = self.snake.head.y
                    break
                self.snake.body[i].x = self.snake.body[i - 1].x
                self.snake.body[i].y = self.snake.body[i - 1].y

            # Changing direction
            if self.snake.dir_x == self.snake.body_w:
                self.snake.head.x += self.snake.body_w
            elif self.snake.dir_x == -self.snake.body_w:
                self.snake.head.x += -self.snake.body_w
            elif self.snake.dir_y == -self.snake.body_h:
                self.snake.head.y += -self.snake.body_h
            elif self.snake.dir_y == self.snake.body_h:
                self.snake.head.y += self.snake.body_h

            self.dt -= 1 / self.v

    def draw(self):
        # Drawing
        self.screen.blit(self.background, [0, 0])


Game()

