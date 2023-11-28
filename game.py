
# ***************************************************************************************************************************************
#                                                                                                                                       *
#                           This is the initial prompt for player 1 (entering the word to be guessed in the game)                       *
#                                                                                                                                       *
#                                                             Tulelle                                                                   *
#                                                                                                                                       *
# ***************************************************************************************************************************************

a=0
while a == 0:
    og_word = input("input one word: ")
    if og_word.isalpha(): # makes sure every variable entered is a letter 
       og_wordlist = list(og_word) # turns the entered word into a list 
       a+=1
    else:
        print("Your input is not a word! ") # informs the player what they have entered is not valid and tells them to enter a new one        

<<<<<<< HEAD
=======

>>>>>>> a4615acab4cf82c21465d30bf921dccd3950f689
# ***************************************************************************************************************************************
#                                                                                                                                       *
#                      This is the main body of the game program which allows player 2 to choose a letter place                         *
#                               to guess and then guess the letter within a limited number of guesses.                                  *
#                                                                                                                                       *
#                                                     - Aashita and Harriet                                                             *
#                                                                                                                                       *
# ***************************************************************************************************************************************

for i in range(len(og_wordlist)):
    print("Enter which letter place you wish to guess between 0-" + str(len(og_word)-1) + ": ") # prompts player to choose a letter place to guess between the calcualted range 
    index_input = input()

<<<<<<< HEAD

# ***************************************************************************************************************************************
#                      The while loop below makes sure the inputted value is numeric and within the acceptable range                    *
=======
# ***************************************************************************************************************************************
#                                    The while loop below makes sure the inputted value is numeric                                      *
>>>>>>> a4615acab4cf82c21465d30bf921dccd3950f689
# ***************************************************************************************************************************************

    b=0
    while b == 0:
<<<<<<< HEAD
        if index_input.isnumeric(): # makes sure every variable entered is a letter 
            index_input = int(index_input) # if inputted value is a number, this line converts numeric value into an integer
            if (index_input >= 0 and index_input <= (len(og_word)-1)): #checks to make sure that the inputted number is within the range of acceptable values 
                b+=1  # ends loop because above condition is no longer met (b != 0)
            else: 
                print("Your input is not valid. Please enter a number") # if input is not numeric, tells user to enter a number and try again
                index_input = input("Enter which letter place you wish to guess between 0-" + str(len(og_word)-1) + ": ")
=======
        if index_input.isnumeric(): # makes sure every variable entered is a number, 
            index_input = int(index_input) # if inputted value is a number, this line converts numeric value into an integer
            b+=1 # ends loop if above condition is met 
>>>>>>> a4615acab4cf82c21465d30bf921dccd3950f689
        else: 
            print("Your input is not valid. Please enter a number") # if input is not numeric, tells user to enter a number and try again
            index_input = input("Enter which letter place you wish to guess between 0-" + str(len(og_word)-1) + ": ")
            

# ***************************************************************************************************************************************
#                      The while loop below allows the player 6 tries to guess the correct letter for the place                         *
#                                and displays a "Correct" or "Incorrect" based on the users input                                       *
# ***************************************************************************************************************************************

<<<<<<< HEAD
=======
# ***************************************************************************************************************************************
#                          The while loop below makes sure the inputted place vlaue is within the given range                           *
# ***************************************************************************************************************************************


    while (index_input < 0 or index_input > (len(og_word)-1)): # loop will run if the inputed place value is outside the range of the length of the word
        print ("Please enter an integer from within the range")
        index_input = int(input("Enter which letter place you wish to guess between 0-" + str(len(og_word)-1) + ": ")) # prompts userr to re-input a value within the range

# ***************************************************************************************************************************************
#                      The while loop below allows the player 6 tries to guess the correct letter for the place                         *
#                                and displays a "Correct" or "Incorrect" based on the users input                                       *
# ***************************************************************************************************************************************

>>>>>>> a4615acab4cf82c21465d30bf921dccd3950f689
    temp = 0
    while temp > -6:
        if 0 <= index_input <=len(og_word)-1: # if the inputted letter place is within the range
            c=0
            while c == 0:
                character_input = input ("Choose one letter to guess for this place: ")
                if character_input.isalpha() and len(character_input) == 1: # makes sure every variable entered is a singular letter (can't be a word)
<<<<<<< HEAD
                    c+=1   # ends loop because above condition is no longer met (c != 0)
=======
                    c+=1
>>>>>>> a4615acab4cf82c21465d30bf921dccd3950f689
                else:
                    print("Your input is not valid ") # informs the player what they have entered is not valid and tells them to enter a new one        
            if character_input == og_wordlist[index_input]:
                print ("Correct!") # if the guessed letter is correct, terminal displays "Correct!"
                break # loop break fi correct so that code can restart from the start of the for loop
            else:
<<<<<<< HEAD
                print ("Incorrect :(")
=======
                print ("Incorrect :(") 
>>>>>>> a4615acab4cf82c21465d30bf921dccd3950f689
                temp-=1 # if guess is incorrect, the current while loop runs for 5 more tries to allow the player to guess again
    if temp <= -6: # if the player doesn't guess the right letter after the 6th guess, the game is over and the loop breaks 
        print ("Game over :(")  
        break