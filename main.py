import sys
import pygame
import random


# Initialize the pygame
pygame.init()

#create the screen (width, height)
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.jpg')

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
# change image size
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyImg = pygame.transform.scale(enemyImg, (64, 64))


enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.9
enemyY_change = 40

# Missile
missileImg = pygame.image.load('missile.png')
missileImg = pygame.transform.scale(missileImg, (32, 32))

# ready state means you can't see the bullet on the screen
# fire state means it is currently moving
missileX = 0
missileY = 480
missileX_change = 0
missileY_change = 10
missile_state = "ready"

def player(x, y):
    #blit means it will draw the player on the screen
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_missile(x, y):
    global missile_state
    missile_state = "fire"
    screen.blit(missileImg, (x + 16, y + 10))

# Game Loop, all game events happen in this loop
running = True
while running:

    # RGB - red, green, blue
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if a keystroke is pressed, check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_UP:
                playerY_change = -1
            if event.key == pygame.K_DOWN:
                playerY_change = 1
            if event.key == pygame.K_SPACE:
                if missile_state is "ready":
                    missileX = playerX
                    fire_missile(missileX, missileY)
                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
            


    # always call the player after the screen.fill method
    # checks if player hits out of bounds
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


    # Checking for boundaries of enemy so it doesn't go out of bounds
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.9
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.9
        enemyY += enemyY_change

    # missile movement
    if missileY <= 0 :
        missileY = 480
        missileY_state = "ready"
        
    if missile_state is "fire":
        fire_missile(missileX, missileY)
        missileY -= missileY_change

    playerY += playerY_change
    player(playerX, playerY)
    enemy(enemyX, enemyY)


    pygame.display.update()

