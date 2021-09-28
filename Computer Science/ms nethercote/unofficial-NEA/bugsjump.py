# game inspired by jump king

import pygame
import time
import math
pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("jump game")


width = 64
height = 64
x = (SCREEN_WIDTH/2)-(width/2)
y = (SCREEN_HEIGHT/2)-(height/2)

vel = 0.5

isJump = False
jumpCount = 10

run = True



while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > 0:
        x -= vel
    if keys[pygame.K_d] and x < SCREEN_WIDTH - width:
        x += vel
    if not(isJump):
        if keys[pygame.K_w] and y > 0:
            y -= vel
        if keys[pygame.K_s] and y < SCREEN_HEIGHT - height:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((245, 231, 218))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()


