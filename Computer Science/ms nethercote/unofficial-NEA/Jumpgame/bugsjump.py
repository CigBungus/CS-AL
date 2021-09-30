# game inspired by jump king 

import pygame
pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("jump game")

# walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
# walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
# bg = pygame.image.load('bg.jpg')
# char = pygame.image.load('standing.png')

width = 64
height = 80
x = (SCREEN_WIDTH/2)-(width/2)
y = SCREEN_HEIGHT-height

vel = 10

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

run = True

while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > 0:
        x -= vel
    if keys[pygame.K_d] and x < SCREEN_WIDTH - width:
        x += vel
    if not(isJump):
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
    pygame.draw.rect(win, (104, 117, 94), (x, y, width, height))
    pygame.display.update()

class level:
    def __init__(self, layout):
        self.layout = layout

    def levelMaker(self, layout):
        print(self)

level1 = level([
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    '                    ',
    'XXX              XXX',])





pygame.quit()





