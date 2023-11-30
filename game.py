



#                                                        HANGMAN EXTREME 


# ***************************************************************************************************************************************
#                                                                                                                                       *
#                           This is the initial prompt for player 1 (entering the word to be guessed in the game)                       *
#                                                                                                                                       *
#                                                             Tulell                                                                    *
#                                                                                                                                       *
# ***************************************************************************************************************************************

a = 0
while a == 0: # while loop that continues until a word that meets the requirements is chosen
    og_word = input("\nInput one word:\n")# querys the user to input there chosen word 
    topic_input = input ("\nInput a topic to help the guesser: \n ")# querys the user to input a hint to aid the player 
    print ("\nThe topic for your word is: " + topic_input + "\n" ) # displays the users hint to the player
    if og_word.isalpha():  # assures every variable entered is a letter 
        og_word = og_word.lower()# switches every letter of the inputed word to lowercase 
        og_wordlist = list(og_word)  # turns the entered word into a list 
        a += 1
    else:
        print("\nYour input is not a word!\n" )  # informs the player what they have entered is not valid and tells them to enter a new one        

# Initialize a list to keep track of guessed indices
guessed_indices = []

# ***************************************************************************************************************************************
#                                                                                                                                       *
#                      This is the main body of the game program which allows player 2 to choose a letter place                         *
#                               to guess and then guess the letter within a limited number of guesses.                                  *
#                                                                                                                                       *
#                                                     - Aashita and Harriet                                                             *
#                                                                                                                                       *
# ***************************************************************************************************************************************

for i in range(len(og_wordlist)):
    print(f"\nEnter which letter place you wish to guess between 0-{len(og_word) - 1}: \n")  # prompts player to choose a letter place to guess between the calculated range
    index_input = input()

# ***************************************************************************************************************************************
#                        The while loop below makes sure the inputted value is numeric and within acceptable range                      *
# ***************************************************************************************************************************************

    b = 0
    while b == 0:
        if index_input.isnumeric():  # makes sure every variable entered is a number,
            index_input = int(index_input)  # if inputted value is a number, this line converts numeric value into an integer
            if (index_input >= 0 and index_input <= (len(og_word) - 1)):  # checks to make sure that the inputted number is within the range of acceptable values
                if index_input in guessed_indices:  # Check if the index has already been guessed
                    print("\nYou've already guessed this place. Please enter a different number.\n")
                    index_input = input(f"\nEnter which letter place you wish to guess between 0-{len(og_word) - 1}:\n")
                else:
                    guessed_indices.append(index_input)  # Add the guessed index to the list of guessed indices
                    b += 1  # ends loop because above condition is no longer met (b!=0)
            else:
                print("\nYour input is not valid. Please enter a number between 0 and " + str(len(og_word) - 1) + "\n")
                index_input = input(f"\nEnter which letter place you wish to guess between 0-{len(og_word) - 1}: \n ")
        else:
            print("\nYour input is not valid. Please enter a number.\n")
            index_input = input(f"\nEnter which letter place you wish to guess between 0-{len(og_word) - 1}:\n ")

# ***************************************************************************************************************************************
#                      The while loop below allows the player 6 tries to guess the correct letter for the place                         *
#                                and displays a "Correct" or "Incorrect" based on the users input                                       *
# ***************************************************************************************************************************************

    c = 0
    while c > -6:
        if 0 <= index_input <= len(og_word) - 1:  # if the inputted letter place is within the range
            d = 0
            while d == 0:
                character_input = input("\nChoose one letter to guess for this place: \n")
                if character_input.isalpha() and len(character_input) == 1:  # makes sure every variable entered is a singular letter (can't be a word)
                    character_input = character_input.lower()  # makes user's guess lowercase, so game isn't case sensitive
                    d += 1
                else:
                    print("\nYour input is not valid \n")  # informs the player what they have entered is not valid and tells them to enter a new one        
            if character_input == og_wordlist[index_input]:
                print("\nCorrect!\n")  # if the guessed letter is correct, terminal displays "Correct!"
                break  # loop break if correct so that code can restart from the start of the for loop
            else:
                print("\nIncorrect :(\n")
                c -= 1  # if guess is incorrect, the current while loop runs for 5 more tries to allow the player to guess again

    if c <= -6:  # if the player doesn't guess the right letter after the 6th guess, the game is over and the loop breaks 
        print("\nGame over :( The correct word was: " + og_word + "\n")
        break
if c == -1:
        print("\t------------------")
        print("\t|\t\t |")
        print("\t|\t        ---")
        print("\t|\t       |   |")
        print("\t|\t        ---")
        print("\t|\t        ")
        print("\t|\t       ")
        print("\t|\t        ")
        print("\t|\t        ")
        print("\t|\t        ")
        print("\t|\t       ")
        print("\t|")
        print("   =====|====================")
elif c == -2: 
    print("\t------------------")
    print("\t|\t\t |")
    print("\t|\t        ---")
    print("\t|\t       |o o|")
    print("\t|\t        ---")
    print("\t|\t        ")
    print("\t|\t       ")
    print("\t|\t        ")
    print("\t|\t        ")
    print("\t|\t        ")
    print("\t|\t       ")
    print("\t|")
    print("   =====|====================")


    # Check for win condition
    if i == len(og_wordlist) - 1:
        print("\nCongratulations! You guessed the entire word correctly! The correct word was: " + og_word + "\n") 
