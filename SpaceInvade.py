import pygame
import random
import cv2
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

#For the background
background = pygame.image.load('space.png')

#Used for the icon and title of the page
pygame.display.set_caption("Spcae Invaders")
icon = pygame.image.load('UFO.png')
pygame.display.set_icon(icon)

#Talk about the player
playerChar = pygame.image.load('Player_model.png')
playerX = 370
playerY = 450
playerX_changed = 0

#Talk about the enemy
enemyChar = pygame.image.load('alien.png')
alienX = random.randint(0, 735)
alienY = random.randint(50, 150)
alienX_changed = 5
alienY_changed = 40

#Talk about the bullet
bulletChar = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_changed = 10

#States of the Bullet
#Ready = You can't see the bullet on the screen
#Fire = The bullet is currently moving
bullet_state = "ready"

score = 0

def player(x, y):
    screen.blit(playerChar, (x, y))

def enemy(x, y):
    screen.blit(enemyChar, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletChar, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    sqX = math.pow(enemyX - bulletX, 2)
    sqY = math.pow(enemyY - bulletY, 2)
    distance = math.sqrt(sqX + sqY)

    if distance < 27:
        return True
    else:
        return False

running = True
while running:
    #Fills it with Red Blue Green
    screen.fill((0, 0, 0))

    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #If key stroke is pressed check what it does 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_changed = -5
            if event.key == pygame.K_RIGHT:
                playerX_changed = 5
            if  event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(playerX, playerY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_changed = 0

    playerX += playerX_changed
    
    if playerX <= 0:
        playerX = 740
    elif playerX >= 750:
        playerX = 0

    #Enemy Movement
    alienX += alienX_changed
    
    if alienX <= 0:
        alienX = 740
        alienY += alienY_changed
    elif alienX >= 750:
        alienX = 0
        alienY += alienY_changed

    #Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_changed
    
    collison = isCollision(alienX, alienY, bulletX, bulletY)
    if collison:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        alienX = random.randint(0, 735)
        alienY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(alienX, alienY)
    pygame.display.update()