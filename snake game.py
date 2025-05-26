import pygame
pygame.init()
width,height = 720,480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colours
purple = (45, 37, 75)
green = (97, 181, 91)
red = (170, 20, 20)

# Snake info
snakeposition = [width/2,height/2]
snakespeed = 10
direction = 'RIGHT'
snakebody = [[360,240],[350,240],[340,240],[330,240]]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'

    screen.fill(purple)

    # Put the snake on the screen
    for pos in snakebody:
        pygame.draw.rect(screen,green,pygame.Rect(pos[0],pos[1],10,10))
    
    # Moving the snake
    if direction == 'RIGHT':
        snakeposition[0] += 10
    if direction == 'LEFT':
        snakeposition[0] -= 10
    if direction == 'UP':
        snakeposition[1] -= 10
    if direction == 'DOWN':
        snakeposition[1] += 10

    snakebody.insert(0,list(snakeposition))
    snakebody.pop()

    # Create a clock
    clock = pygame.time.Clock()
    clock.tick(snakespeed)

    pygame.display.flip()

pygame.quit()