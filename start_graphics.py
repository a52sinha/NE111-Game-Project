import pygame
import sys
pygame.init()


pygame.display.init
screen = pygame.display.set_mode([1920, 1080])
pygame.display.set_caption("Hangman Game")

stage1_path = 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    #draw things here
    pygame.display.flip()



pygame.quit()
sys.exit()


