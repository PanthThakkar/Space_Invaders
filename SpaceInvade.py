import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

#Used for the icon and title of the page
pygame.display.set_caption("Spcae Invaders")
icon = pygame.image.load('UFO.png')
pygame.display.set_icon(icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    pygame.display.update()