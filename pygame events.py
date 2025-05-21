import pygame
import time
import random

pygame.init() #Initialize a pygame class

#Set our screen size
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
bgrndcolour = (53,112,133) #Set background colour in RBG
image = pygame.image.load("crosshairs.png") #Load image
image = pygame.transform.scale(image, (30,30)) #Make image small
imagerect = image.get_rect()
imagespeed = [1,1] #Set the speed of the image
position = [width/2,height/2]

bomb = pygame.image.load("bomb.webp")
bomb = pygame.transform.scale(bomb, (35,40))
bombrect = bomb.get_rect()

pygame.display.set_caption("boom") #Name window
pygame.display.set_icon(image) #Add custom icon

#Main running loop
running = True
while running:
    screen.fill(bgrndcolour) #Colour the background of the window

    screen.blit(bomb,bombrect)

    screen.blit(image,imagerect) #Adds image to rectangle
    bombrect = bombrect.move(imagespeed) #Start moving the image

    #Create an event in pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #Close the game
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                position = (imagerect.center[0]-10,imagerect.center[1])
            if event.key == pygame.K_RIGHT:
                position = (imagerect.center[0]+10,imagerect.center[1])
            if event.key == pygame.K_UP:
                position = (imagerect.center[0],imagerect.center[1]-10)
            if event.key == pygame.K_DOWN:
                position = (imagerect.center[0],imagerect.center[1]+10)

    #Bound the image in the screen
    if bombrect.left < 0 or bombrect.right > width: #If the image hits the left or right side of the window
        imagespeed[0] = -imagespeed[0] #X-component of speed switches directions
    if bombrect.top < 0 or bombrect.bottom > height: #If the image hits the top or bottom
        imagespeed[1] = -imagespeed[1] #Y-component of speed switches directions
    if imagerect.center[0] <= 0:
        position = (399,imagerect.center[1])
    if imagerect.center[0] >= 400:
        position = (1,imagerect.center[1])
    if imagerect.center[1] <= 0:
        position = (imagerect.center[0],399)
    if imagerect.center[1] >= 400:
        position = (imagerect.center[0],1)
    
    if imagerect.colliderect(bombrect):
        screen.fill((255,0,0))

    imagerect.center = position

    pygame.display.flip() #Refreshes the screen
    time.sleep(10 / 1000) #Wait ten miliseconds so the image moves slower

pygame.quit() #Quits pygame properly