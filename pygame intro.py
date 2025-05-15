import pygame

pygame.init() #Initialize a pygame class

#Set our screen size
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
bgrndcolour = (53,112,133) #Set background colour in RBG
image = pygame.image.load("thailand silhouette.png") #Load image
image = pygame.transform.scale(image, (30,54)) #Make image small
image_rect = image.get_rect()

pygame.display.set_caption("Snatched Thailand") #Name window
pygame.display.set_icon(image) #Add custom icon

#Main running loop
running = True
while running:
    #Create an event in pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #Close the game

    screen.fill(bgrndcolour)

    screen.blit(image,image_rect)

    pygame.display.flip() #Refreshes the screen

pygame.quit() #Quits pygame properly