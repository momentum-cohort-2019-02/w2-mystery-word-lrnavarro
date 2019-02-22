#need random module 
import random

#words = ["cool", "indubitably", "Tehran", 
        # "pineapple", "axolotl", "hamburger", "squat"]

#[
    #word                                 # collection
    #for word in words                    # iteration
     # selection
#]

with open("words.txt") as words_file:
     
    print ([word.strip()
            for word in words_file.readlines() 
            if len(word) >= 6 and len(word) <= 8])

