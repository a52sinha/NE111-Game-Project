import pygame
import sys

pygame.init()
pygame.font.init()
pygame.display.init()

screen = pygame.display.set_mode([1920, 1080])
pygame.display.set_caption("Hangman Game")

# Loading hangman stage images
stage1_path = r"C:\Users\kater\Downloads\stage1.png"
constant = pygame.image.load(stage1_path)

clock = pygame.time.Clock()

# Hangman Game Logic
a = 0
topic_input = ""
og_word = ""
og_wordlist = []
guessed_indices = []

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
    invalid_input_text_rect.center = (1920 // 2, 700)
    screen.blit(invalid_input_text, invalid_input_text_rect)

    # Display Hangman stage image
    screen.blit(constant, (806.5, 300))

    if a == 0:
        if og_word == "":
            og_word = input("\nInput one word:\n")
            topic_input = input("\nInput a topic to help the guesser: \n ")
            print("\nThe topic for your word is: " + topic_input + "\n")

            if og_word.isalpha():
                og_word = og_word.lower()
                og_wordlist = list(og_word)
                a += 1
            else:
                print("\nYour input is not a word!\n")
        else:
            for i in range(len(og_wordlist)):
                print(f"\nEnter which letter place you wish to guess between 0-{len(og_word) - 1}: \n")
                index_input = input()

                b = 0
                while b == 0:
                    if index_input.isnumeric():
                        index_input = int(index_input)
                        if 0 <= index_input <= (len(og_word) - 1):
                            if index_input in guessed_indices:
                                print("\nYou've already guessed this place. Please enter a different number.\n")
                                index_input = input(f"\nEnter which letter place you wish to guess between 0-{len(og_word) - 1}:\n")
                            else:
                                guessed_indices.append(index_input)
                                b += 1
                        else:
                            print("\nYour input is not valid. Please enter a number between 0 and " + str(len(og_word) - 1) + "\n")
                            index_input = input(f"\nEnter which letter place you wish to guess between 0-{len(og_word) - 1}: \n ")
                    else:
                        print("\nYour input is not valid. Please enter a number.\n")
                        index_input = input(f"\nEnter which letter place you wish to guess between 0-{len(og_word) - 1}:\n ")

                c = 0
                while c > -6:
                    if 0 <= index_input <= len(og_word) - 1:
                        d = 0
                        while d == 0:
                            character_input = input("\nChoose one letter to guess for this place: \n")
                            if character_input.isalpha() and len(character_input) == 1:
                                character_input = character_input.lower()
                                d += 1
                            else:
                                print("\nYour input is not valid \n")
                        if character_input == og_wordlist[index_input]:
                            print("\nCorrect!\n")
                            break
                        else:
                            print("\nIncorrect :(\n")
                            c -= 1

                    if c <= -6:
                        print("\nGame over :( The correct word was: " + og_word + "\n")
                        break

                    if i == len(og_wordlist) - 1:
                        print("\nCongratulations! You guessed the entire word correctly! The correct word was: " + og_word + "\n")

    pygame.display.flip()
    clock.tick(1)

pygame.font.quit()
pygame.quit()
sys.exit()
