import pygame
import sys
pygame.init()
pygame.font.init()
pygame.display.init()
screen = pygame.display.set_mode([1920, 1080])
pygame.display.set_caption("Hangman Game")

stage1_path = r"C:\Users\kater\Downloads\stage1.png"


constant = pygame.image.load(stage1_path)




og_word = 'HEBDB'
word_length = len(og_word)



clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    black = (0, 0, 0)
    white = (255, 255, 255)
    
    screen.fill(white) 

    
    font = pygame.font.SysFont("Times New Roman", 72)
    invalid_input_text = font.render("Too Many Letters!", True, black)
    invalid_input_text_rect = invalid_input_text.get_rect()
    invalid_input_text_rect.center = (1920 / 2, 700)


   
    screen.blit(constant, (806.5, 300))
    
    for i in range(word_length):
        if i > 0:
          rr = word_length * 96
          if word_length < 11:
              pygame.draw.line(screen, black, (480, 800), (rr + 480, 800))
              pygame.display.flip()
          else:
              pass
        
        else:
            pass    

    for i in range(word_length):
     if word_length == 0: 
         screen.blit(invalid_input_text, invalid_input_text_rect)
         pygame.display.flip()

     
     elif word_length <= 10:
          n = i * 96
          pygame.draw.line(screen, white, (560 + n, 800), ((576 + n), 800))
          pygame.display.flip()

     elif i == word_length:
        pass
     
     else:
          screen.blit(invalid_input_text, invalid_input_text_rect)
          pygame.display.flip()


            
    
    pygame.display.flip()
    clock.tick(1)

    
pygame.font.quit()
pygame.quit()
sys.exit()


