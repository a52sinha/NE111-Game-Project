


a=0
while a == 0:
    og_word = input("input one word: ")
    if og_word.isalpha(): # makes sure every variable entered is a letter 
       og_wordlist = list(og_word) # turns the entered word into a list 
       a+=1
    else:
        print("Your input is not a word! ") # informs the player what they have entered is not valid and tells them to enter a new one        

for i in range(len(og_wordlist)):
    print("Enter which letter place you wish to guess between 0-" + str(len(og_word)-1) + ": ")
    index_input = input()
    
    b=0
    while b == 0:
        if index_input.isnumeric(): # makes sure every variable entered is a letter 
            index_input = int(index_input)
            b+=1
        else:
            print("Your input is not valid. Please enter a number")
            index_input = input("Enter which letter place you wish to guess between 0-" + str(len(og_word)-1) + ": ")

    while (index_input < 0 or index_input > (len(og_word)-1)):
        print ("Please enter an integer from within the range")
        index_input = int(input("Enter which letter place you wish to guess between 0-" + str(len(og_word)-1) + ": "))
        
    temp = 0
    while temp > -6:
        if 0 <= index_input <=len(og_word)-1:
            c=0
            while c == 0:
                character_input = input ("Choose one letter to guess for this place: ")
                if character_input.isalpha() and len(character_input) == 1: # makes sure every variable entered is a letter 
                    c+=1
                else:
                    print("Your input is not valid ") # informs the player what they have entered is not valid and tells them to enter a new one        
            if character_input == og_wordlist[index_input]:
                print ("Correct!") # add graphics here like dashes etc...
                break 
            else:
                print ("Incorrect :(")
                temp-=1
    if temp <= -6:
        print ("Game over :(")  
        break

  
 
                
                
# to do:x
    # can't re guess for same plavce after correct 
    # kat graphics -= dasdhes and hangman 
      
    

      



