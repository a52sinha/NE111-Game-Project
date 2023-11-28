

a=0
while a == 0:
    og_word = input("input one word: ")
    #def hangmanword(og_word):  # defines the chosen word           
    if og_word.isalpha(): # makes sure every variable entered is a letter 
       og_wordlist = list(og_word) # turns the entered word into a list 
       #return og_wordlist # returns the list with the letters of the inputed word 
       a+=1
    else:
        print("Your input is not a word! ") # informs the player what they have entered is not valid and tells them to enter a new one
        


 