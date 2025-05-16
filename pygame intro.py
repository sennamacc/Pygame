import pygame
import time
import random

pygame.init() #Initialize a pygame class

#Set our screen size
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
bgrndcolour = (53,112,133) #Set background colour in RBG
image = pygame.image.load("thailand silhouette.png") #Load image
image = pygame.transform.scale(image, (30,54)) #Make image small
imagerect = image.get_rect()
imagespeed = [1,1] #Set the speed of the image

blackbox = pygame.image.load("blackbox.jfif")
blackbox = pygame.transform.scale(blackbox, (60,10))
boxrect = blackbox.get_rect()
boxspeed = 10

pygame.display.set_caption("Thailand") #Name window
pygame.display.set_icon(image) #Add custom icon

#Main running loop
running = True
while running:

    screen.fill(bgrndcolour) #Colour the background of the window

    screen.blit(image,imagerect) #Adds image to rectangle
    imagerect = imagerect.move(imagespeed) #Start moving the image
    
    screen.blit(blackbox,boxrect) #Adds image to rectangle
    boxrect.center = (width/2, height-2)

    #Create an event in pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #Close the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                boxrect.x += boxspeed
            elif event.key == pygame.K_LEFT:
                boxrect.x -= boxspeed


    """#Bound the image in the screen
    if imagerect.left < 0 or imagerect.right > width: #If the image hits the left or right side of the window
        imagespeed[0] = -imagespeed[0] #X-component of speed switches directions
    if imagerect.top < 0 or imagerect.bottom > height: #If the image hits the top or bottom
        imagespeed[1] = -imagespeed[1] #Y-component of speed switches directions
    if (imagerect.left < 0 or imagerect.right > width) and (imagerect.top < 0 or imagerect.bottom > height):
        imagespeed = [(imagespeed[0]*30),(imagespeed[1]*30)]"""
    
    if imagerect.left < 0 or imagerect.right > width:
        imagespeed[0] = -imagespeed[0]
    if imagerect.top < 0:
        imagespeed[1] = -imagespeed[1]
    if imagerect.bottom > height:
        bgrndcolour = (255,0,0)
    if imagerect.collidepoint(boxrect.x, boxrect.y):
        imagespeed[0] = -imagespeed[0]
        imagespeed[1] = -imagespeed[1]


    pygame.display.flip() #Refreshes the screen
    time.sleep(10 / 1000) #Wait ten miliseconds so the image moves slower

pygame.quit() #Quits pygame properly
