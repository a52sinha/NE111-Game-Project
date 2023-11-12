og_word = "Hello"
og_wordlist= list(og_word)


for i in range(len(og_wordlist)):
    print("Enter which letter place you wish to guess between 0-" + str(len(og_word)-1) + ": ")
    index_input = int(input())
   
    while (index_input < 0 or index_input > (len(og_word)-1)):
        print ("Please enter an integer from within the range")
        index_input = int(input("Enter which letter place you wish to guess between 0-" + str(len(og_word)-1) + ": "))

    if 0 <= index_input <=len(og_word)-1:
        character_input = input ("Choose your guess for this place: ")
        if character_input == og_wordlist[index_input]:
            print ("Correct!") # add graphics here like dashes etc...
        else:
            print ("incorrect")
# to do:
    #error trap for str and flopat
    # if character input is not str
    # limit gueses for each place + character 
    # can't re guess for same plavce after correct 
    # kat graphics -= dasdhes and hangman 