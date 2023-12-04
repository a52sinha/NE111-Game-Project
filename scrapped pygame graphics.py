import pygame
import sys

pygame.init() #initials modules
pygame.font.init()
pygame.display.init()

screen = pygame.display.set_mode([1920, 1080]) #initialize a screen
pygame.display.set_caption("Hangman Game") #name the game

stage1_path = r"C:\Users\katerina\Downloads\stage1.png" #change - need to insert real path, this is just the temporary file paths
    #stage2_path = 'stage2.png'
    #stage3_path = 'stage3.png'
    #stage4_path = 'stage4.png'
    #stage5_path = 'stage5.png'
    #stage6_path = 'stage6.png'
    #stage7_path = 'stage7.png'

constant = pygame.image.load(stage1_path) # images when no mistakes made
#mistake1 = pygame.image.load(stage2_path)
#mistake2 = pygame.image.load(stage3_path)
#mistake3 = pygame.image.load(stage4_path)
#mistake4 = pygame.image.load(stage5_path)
#mistake5 = pygame.image.load(stage6_path)
#mistake6 = pygame.image.load(stage7_path)

#about the word
og_word = '' #initializes this as a str
word_length = len(og_word)


clock = pygame.time.Clock() #initializes the counting of frames


#main code below
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #exit the game

        
    
#next are defintions of constants
    black = (0, 0, 0)
    white = (255, 255, 255)

    screen.fill(white) #this is screen of the game

    font = pygame.font.SysFont("Times New Roman", 72) #font of the game

#done defining constants


#setting up text to display on the screen
    
    invalid_input_text = font.render("Too Many Letters!", True, black)
    invalid_input_text_rect = invalid_input_text.get_rect()
    invalid_input_text_rect.center = (1920 // 2, 700)

# done setting up text

#this defines where the letters will be displayed, change - to correlate correct guesses to trigger the letter to display on screen.
    og_wordlist = set(og_word)
    letter1 = font.render(og_wordlist[0], True, black)
    letter1_rect = letter1.get_rect()
    letter1_rect.center = (528, 848) #in the middle of the first dash
    # to print: screen.blit(letter1, letter1_rect)

    letter2 = font.render(og_wordlist[1], True, black)
    letter2_rect = letter2.get_rect()
    letter2_rect.center = (624, 848) #in the middle of the second dash, and so on...

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


    # this is the constant image displayed. change - to add conditions where it stops being displayed)
    screen.blit(constant, (806.5, 300))




    #change - this is where you add conditions to trigger other images of the hangman being displayed.
    # screen.blit(mistake1, (806.5, 300)) and so on...


    #the following lines of code will be in relation to the dashed line
   
    for i in range(word_length):
        if i > 0: 
          rr = word_length * 96 #space allocated for each dash + gap 
          if word_length < 11: #max length is 10 
              pygame.draw.line(screen, black, (480, 800), (rr + 480, 800)) #to only draw the black line from a quarter of the screen to right until the dashes end
              pygame.display.flip() #update code for screen, so that the black line appears
          else:
              pass
        
        else: 
            pass    

    for i in range(word_length):
     if word_length == 0: #if they imput nothing
         screen.blit(invalid_input_text, invalid_input_text_rect) #tells program where to display text
         pygame.display.flip() #update screen

     
     elif word_length <= 10:
          n = i * 96
          pygame.draw.line(screen, white, (560 + n, 800), ((576 + n), 800)) #periodically, by a period of 96 px, to draw a white line (gap) 
          pygame.display.flip()

     elif i == word_length:
        pass #once the loop finishes, stop drawing dashes. This insures that dashes = characters of word
     
     else:
          screen.blit(invalid_input_text, invalid_input_text_rect)
          pygame.display.flip()


            
    #this updates code with screen
    pygame.display.flip()
    clock.tick(1) #minimizes flashing of the dashes


#We split up tasks of graphics and code, and once we finished, we were unable to integrate it, and so this code ended up being unused.
# to integrate the code, we needed to create input boxes, trigger letters being displayed when user guessed correctly, and to trigger new images to be displayed when a user makes a mistake.
#So, although we never used this code, we still wanted to submit it because it took some time and effort to learn pygame.


pygame.font.quit() #exit
pygame.quit()
sys.exit()


