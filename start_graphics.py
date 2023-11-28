import pygame
import sys

pygame.init()
pygame.font.init()
pygame.display.init()

screen = pygame.display.set_mode([1920, 1080])
pygame.display.set_caption("Hangman Game")

stage1_path = r"C:\Users\kater\Downloads\stage1.png"
    #stage2_path = 'stage2.png'
    #stage3_path = 'stage3.png'
    #stage4_path = 'stage4.png'
    #stage5_path = 'stage5.png'
    #stage6_path = 'stage6.png'
    #stage7_path = 'stage7.png'

constant = pygame.image.load(stage1_path)
#mistake1 = pygame.image.load(stage2_path)
#mistake2 = pygame.image.load(stage3_path)
#mistake3 = pygame.image.load(stage4_path)
#mistake4 = pygame.image.load(stage5_path)
#mistake5 = pygame.image.load(stage6_path)
#mistake6 = pygame.image.load(stage7_path)


clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    black = (0, 0, 0)
    white = (255, 255, 255)
    
    screen.fill(white) #this is screen of the game

    #setting up text to display on the screen
    font = pygame.font.SysFont("Times New Roman", 72)
    invalid_input_text = font.render("Too Many Letters!", True, black)
    invalid_input_text_rect = invalid_input_text.get_rect()
    invalid_input_text_rect.center = (1920 // 2, 700)


    # this is the constant image displayed (remember to add conditions where it stops being displayed)
    screen.blit(constant, (806.5, 300))


    #this is where the letters will be displayed
    og_wordlist = set(og_word)
    letter1 = font.render(og_wordlist[0], True, black)
    letter1_rect = letter1.get_rect()
    letter1_rect.center = (528, 848)
    # to print: screen.blit(letter1, letter1_rect)

    letter2 = font.render(og_wordlist[1], True, black)
    letter2_rect = letter2.get_rect()
    letter2_rect.center = (624, 848)

    letter3 = font.render(og_wordlist[2], True, black)
    letter3_rect = letter3.get_rect()
    letter3_rect.center = (720, 848)

    letter4 = font.render(og_wordlist[3], True, black)
    letter4_rect = letter4.get_rect()
    letter4_rect.center = (816, 848)

    letter5 = font.render(og_wordlist[4], True, black)
    letter5_rect = letter5.get_rect()
    letter5_rect.center = (912, 848)

    letter6 = font.render(og_wordlist[5], True, black)
    letter6_rect = letter6.get_rect()
    letter6_rect.center = (1008, 848)

    letter7 = font.render(og_wordlist[6], True, black)
    letter7_rect = letter7.get_rect()
    letter7_rect.center = (1104, 848)

    letter8 = font.render(og_wordlist[7], True, black)
    letter8_rect = letter8.get_rect()
    letter8_rect.center = (1200, 848)

    letter9 = font.render(og_wordlist[8], True, black)
    letter9_rect = letter9.get_rect()
    letter9_rect.center = (1296, 848)

    letter10 = font.render(og_wordlist[9], True, black)
    letter10_rect = letter10.get_rect()
    letter10_rect.center = (1392, 848)


    #this is where you add conditions: if they did one mistake
    # screen.blit(mistake1, (806.5, 300)) and so on...


    #the following lines of code will be in relation to the dashed line
   
    og_word = 'wateryutuut'
    word_length = len(og_word)
    
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
     if word_length == 0: #if they imput nothing
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


            
    #this updates code with screen
    pygame.display.flip()
    clock.tick(1)

    
pygame.font.quit()
pygame.quit()
sys.exit()


