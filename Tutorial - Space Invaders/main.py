from pygame import *
from random import randint
from math import sqrt

# initialize pygame
init()

# create screen
screenx = 800
screeny = 600
screen = display.set_mode((screenx, screeny))

# background
background = image.load("background.png")

# title and icon
display.set_caption("Space Invaders")
icon = image.load("icon.png")
display.set_icon(icon)

# Player
playerimg = image.load("spaceship.png")
playerx = 370
playery = 480
xspeed = 1
yspeed = 0.3
shoot = False
up = down = left = right = False
enemy_xspeed = 0.6
enemy_yspeed = 0.03


def player():
    screen.blit(playerimg, (int(playerx), int(playery)))


# Enemies

enemies = []
def enemyimg():
    return image.load("enemy"+str(randint(1,4))+".png")
enemyspawnspeed = 300
enemyspawn = 299

# bullets

bullets = []
bulletspeed = 1
bulletunloadspeed = 50
bulletunload = 0

# GAME LOOP
running = True
direction = 1
while running:

    # background
    screen.blit(background, (0, 0))

    for ev in event.get():
        if ev.type == QUIT:
            running = False
    if ev.type == KEYDOWN:
        if ev.key == K_LEFT:
            left = True
        if ev.key == K_RIGHT:
            right = True
        if ev.key == K_UP:
            up = True
        if ev.key == K_DOWN:
            down = True
        if ev.key == K_SPACE:
            shoot = not shoot

    if ev.type == KEYUP:
        if ev.key == K_LEFT:
            left = False
        if ev.key == K_RIGHT:
            right = False
        if ev.key == K_UP:
            up = False
        if ev.key == K_DOWN:
            down = False

    if left and playerx > 0:
        playerx -= xspeed
    if right and playerx < screenx - 64:
        playerx += xspeed
    if up and playery > 0:
        playery -= yspeed
    if down and playery < screeny - 64:
        playery += yspeed

    enemyspawn += 1
    if enemyspawn % enemyspawnspeed == 0:
        enemies.append([randint(0, screenx - 64), 0, enemyimg()])

    for enemy in enemies:
        enemy[0] += enemy_xspeed
        enemy[1] += enemy_yspeed
        if enemy[0] >= screenx - 64:
            enemy[0] = screenx - 64
            enemy_xspeed *= -1
        elif enemy[0] <= 0:
            enemy[0] = 0
            enemy_xspeed *= -1
        screen.blit(enemy[2], (int(enemy[0]), int(enemy[1])))

    if shoot:
        bulletunload += 1
        if bulletunload % bulletunloadspeed == 0:
            bullets.append(((randint(0, 255), randint(0, 255), randint(0, 255)), [int(playerx) + 32, int(playery)]))

    for bullet in bullets:
        bullet[1][1] -= bulletspeed
        draw.circle(screen, bullet[0], bullet[1], 8)
        for enemy in enemies:
            if sqrt((bullet[1][0] - enemy[0]) ** 2 + (bullet[1][1] - enemy[1]) ** 2) <= 40:
                bullets.remove(bullet)
                enemies.remove(enemy)

    player()
    display.update()
