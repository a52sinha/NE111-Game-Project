def hangmanword(og_word):            
    if og_word.isalpha(): 
        og_wordlist = list(og_word)
        return og_wordlist
    else:
            return"input new word "

og_word = input("input one word")
result_list = hangmanword(og_word)
print(result_list)




 
            
            
    