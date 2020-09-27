import os
import pygame
from maze_generator import maze
from random import randint

pygame.init()


class Maze:
    def __init__(self, width=10, height=10):
        m = maze(width, height)
        north = 1
        east = 2
        south = 4
        west = 8
        self.width = width
        self.height = height
        self.matrix = []
        path_width = 3
        for _ in range((path_width + 1) * height + 1):
            self.matrix.append([1] * ((path_width + 1) * width + 1))
        for i in range(height):

            if m[i][0] & west:
                for mi in range(path_width):
                    self.matrix[(path_width + 1) * i + mi + 1][0] = 0

            for j in range(width):
                for mi in range(path_width):
                    for mj in range(path_width):
                        self.matrix[(path_width + 1) * i + mi + 1][(path_width + 1) * j + mj + 1] = 0
                if m[i][j] & east:
                    for mi in range(path_width):
                        self.matrix[(path_width + 1) * i + mi + 1][(path_width + 1) * j + path_width + 1] = 0
                if m[i][j] & north:
                    for mj in range(path_width):
                        self.matrix[(path_width + 1) * i][(path_width + 1) * j + mj + 1] = 0

        # for i in self.matrix:
        #   print(*i)
        self.width = (path_width + 1) * width + 1
        self.height = (path_width + 1) * height + 1

    def draw(self):
        cell_width = display_height // self.height
        self.md = pygame.Surface([display_height, display_height], pygame.SRCALPHA, 32)
        self.md = self.md.convert_alpha()
        """
        for i in range(self.height):
            for j in range(self.width):
                if self.matrix[i][j]:
                    x = pygame.Rect(cell_width*j, cell_width*i, cell_width, cell_width)
                    pygame.draw.rect(self.md, (0, 0, 0), x)
        """
        wall = pygame.image.load("img/wall.png")
        wall = pygame.transform.scale(wall, (cell_width, cell_width))
        for i in range(self.height):
            for j in range(self.width):
                if self.matrix[i][j]:
                    self.md.blit(wall, (cell_width * j, cell_width * i))

    def display(self):
        x = (display_width - display_height) // 2
        y = 0
        screen.blit(self.md, (x, y))


class Player:
    def __init__(self):
        self.size = (40, int(40 * 1.33))
        self.character = pygame.image.load("img/characters/" + characters[randint(0, len(characters) - 1)])
        self.character = pygame.transform.scale(self.character, self.size)
        self.x = 0
        self.y = 0

    def show(self):
        screen.blit(self.character, (self.x, self.y))

    def move(self, x_change, y_change):
        self.x += x_change
        self.y += y_change
        if self.x < 0:
            self.x = 0
        elif self.x > display_width - self.size[0]:
            self.x = display_width - self.size[0]
        if self.y < 0:
            self.y = 0
        elif self.y > display_height - self.size[1]:
            self.y = display_height - self.size[1]


#########colors
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

characters = [c for c in os.listdir('img/characters')]
print(characters)

display_height = 1080
display_width = 1920
fps = 60

screen = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
pygame.display.set_caption('Maze Master')
icon = pygame.transform.scale(pygame.image.load('img/icon.png'), (32, 32))
pygame.display.set_icon(icon)
clock = pygame.time.Clock()


def game_intro():
    def drawintro():
        screen.fill(black)
        screen.blit(introtext, introtextrect)
        screen.blit(introtext2, introtextrect2)

    def fade_intro(width=display_width, height=display_height):  # fade out screen - intro
        fade = pygame.Surface((width, height))
        fade.fill(black)
        for alpha in range(300):
            fade.set_alpha(alpha)
            drawintro()
            screen.blit(fade, (0, 0))
            pygame.display.update()
            pygame.time.delay(5)

    intro = True
    introfont = pygame.font.Font('freesansbold.ttf', 120)
    introtext = introfont.render('Maze Master', True, green)
    introtextrect = introtext.get_rect()
    introtextrect.center = (display_width // 2, display_height // 2 - 60)
    introtext2 = introfont.render('by Cristian Grecu', True, green)
    introtextrect2 = introtext2.get_rect()
    introtextrect2.center = (display_width // 2, display_height // 2 + 60)
    drawintro()
    pygame.time.delay(10)
    fade_intro()
    pygame.display.update()

    button_size = (100, 25)
    pygame.draw.rect(screen, green, ((display_width-button_size[0])//2,(display_width-button_size[1])//2,(display_width+button_size[0])//2,(display_width+button_size[1])//2))
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()


def game_loop():
    player = Player()
    x_change = y_change = 0
    running = True
    m = Maze(10, 10)
    m.draw()

    # background image
    background = pygame.image.load("img/ground.jpg")
    background = pygame.transform.scale(background, (display_width, display_height))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        player.move(x_change, y_change)
        screen.blit(background, (0, 0))
        player.show()
        m.display()
        pygame.display.update()
        clock.tick(fps)


game_intro()
game_loop()
pygame.quit()
