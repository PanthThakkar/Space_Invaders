import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

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
alienX = 370
alienY = 50
alienX_changed = 0

def player(x, y):
    screen.blit(playerChar, (x, y))

def enemy(x, y):
    screen.blit(enemyChar, (x, y))


running = True
while running:
    #Fills it with Red Blue Green
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #If key stroke is pressed check what it does 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_changed = -0.25
            if event.key == pygame.K_RIGHT:
                playerX_changed = 0.25
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_changed = 0

    playerX += playerX_changed
    
    if playerX <= 0:
        playerX = 740
    elif playerX >= 750:
        playerX = 0

    player(playerX, playerY)
    enemy(alienX, alienY)
    pygame.display.update()