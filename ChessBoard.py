#so what we need to do is to move this into our other project
import pygame
import sys

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
pygame.font.init()
unistr = "♛"
f = pygame.font.Font("segoe-ui-symbol.ttf", 60)
pygame.display.flip()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    size = 80
    center = 40
    y = center
    color = 'grey'
    for i in range(8):
        x = center
        for j in range(8):
            current_square = pygame.draw.rect(screen, color, pygame.Rect(x, y, size, size))
            #screen.blit(f.render(unistr,current_square,(255,0,0)), current_square)
            screen.blit(f.render(unistr,current_square,('black')),(x + 10, y - 3))
            x += size
            if color == 'white':
                color = 'grey'
            elif color == 'grey':
                color = 'white'
        if color == 'white':
            color = 'grey'
        elif color == 'grey':
            color = 'white'
        y += size

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

