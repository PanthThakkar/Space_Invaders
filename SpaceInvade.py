import pygame
import random
import cv2
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

#For the background
background = pygame.image.load('space.png')

#For Background Sounds
mixer.music.load('Fearless First.mp3')
mixer.music.play(-1)

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
enemyChar = []
alienX = []
alienY = []
alienX_changed = []
alienY_changed = []
num_of_enemies = 5

for enemy in range(num_of_enemies):

    enemyChar.append(pygame.image.load('alien.png'))
    alienX.append(random.randint(0, 735))
    alienY.append(random.randint(50, 150))
    alienX_changed.append(5)
    alienY_changed.append(40)

#Talk about the bullet
bulletChar = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_changed = 10

#States of the Bullet
#Ready = You can't see the bullet on the screen
#Fire = The bullet is currently moving
bullet_state = "ready"


#Score

score_val = 0
font = pygame.font.Font('Skate Brand.otf', 32)
textX = 10
textY = 10

over_font = pygame.font.Font('Skate Brand.otf', 64)

def show_score(x, y):
    score = font.render("Score: " + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_test():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerChar, (x, y))

def enemy(x, y, i):
    screen.blit(enemyChar[i], (x, y))

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

                    #If wanted sound for shooting
                    #bulletSound = mixer.Sound("Laser Sound Effect.mp3")
                    #bulletSound.play()
                    
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
    for alienM in range(num_of_enemies):
        alienX[alienM] += alienX_changed[alienM]
        
        if alienY[alienM] > 250:
            for alienN in range(num_of_enemies):
                alienX[alienN] = 2000

            game_over_test()
            break

        if alienX[alienM] <= 0:
            alienX[alienM] = 740
            alienY[alienM] += alienY_changed[alienM]
        elif alienX[alienM] >= 750:
            alienX[alienM] = 0
            alienY[alienM] += alienY_changed[alienM]

        collison = isCollision(alienX[alienM], alienY[alienM], bulletX, bulletY)
        if collison:

            # If wanted sound effects for killing monster
            #explosionSound = mixer.Sound("explosion.mp3")
            #explosionSound.play()

            bulletY = 480
            bullet_state = "ready"
            score_val += 1
            alienX[alienM] = random.randint(0, 735)
            alienY[alienM] = random.randint(50, 150)

        enemy(alienX[alienM], alienY[alienM], alienM)

    #Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_changed

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
