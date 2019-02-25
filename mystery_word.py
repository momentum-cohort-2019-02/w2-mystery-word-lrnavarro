#get random module 
import random           

#import all words and separate them into easy, normal and hard lists
def import_words(filename, easy, normal, hard):
    #open file
    with open(filename) as file:
        text = file.read()
    for word in text.split("\n"):
        #check for empty and add words to the indivual lists by level
        if (word !='' and len(word) >= 4 and len(word) <=6):
            easy.append(word.casefold())
        if (word !='' and len(word) >= 6 and len(word) <=8):
            normal.append(word.casefold())
        if (word !='' and len(word) >= 8):
            hard.append(word.casefold())
        
#get level from user
def choose_level():
    level = input("Choose a level of difficulty, 1 for easy, 2 for normal, 3 for hard")
    return int(level)

#get random word from list
def get_random_word(word_list):
    return random.choice(word_list)

#get word from list based on the level
def get_word_from_list(level, easy, normal, hard):
    if level == 1:
        return get_random_word(easy)
    if level == 2:
        return get_random_word(normal)
    if level == 3:
        return get_random_word(hard)
    
#get guesses from user
def guess_word(mystery_word):
    word = list(mystery_word)
    guess_word = list("_" * len(word))
    print("Your word looks like this: " + str(guess_word))
    tries = 8
    previous_guesses = []
    while tries > 0:
        #ask user to pick a letter and define it to use later
        choice_letter = input("Pick one letter from the English alphabet: ").lower()
        while choice_letter.isalpha() != True or len(choice_letter) != 1:
            choice_letter = input("Please enter one valid letter from the English alphabet: ").lower()
        while choice_letter in previous_guesses:
                choice_letter = input("You've already guessed that one, please choose another letter: ").lower()
        #replace underscore with letters found in guess_word
        previous_guesses.append(choice_letter)
        if choice_letter in word:
            for i in range(0, len(word)):
                if word[i] == choice_letter:
                    guess_word[i] = choice_letter
            print("You've found a letter!  Your word looks like this: " + str(guess_word))
            if "_" not in guess_word:
                print("Congratulations!  You guessed the mystery word!: " + str(word)) 
                return
        else:
            print("Sorry, that letter is not in the mystery word")
            tries -= 1
    if tries == 0:
        print("Sorry, you didn't guess the mystery word: " + str(word)) 
        

#start game
def play_game(easy, normal, hard):
    play_again = True
    while play_again:
        #call function to ask user for level
        level = choose_level()
        #call function to get word
        word = get_word_from_list(level, easy, normal, hard)
        guess_word(word)
        another_game = int(input("Do you want to play again? enter 1 for yes, 2 for no"))
        if another_game == 2:
            play_again = False
    print("Thanks for playing, see ya next time!")


# create main function to start program
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Import list of words from a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    easy = []
    normal = []
    hard = []

    file = Path(args.file)
    if file.is_file():
       #load words from the file into the appropriate list
       import_words(file, easy, normal, hard)
    else:
        print(f"{file} does not exist!")
        exit(1)  #means terminate

    print("Welcome to Mystery Word Game.\n" +
    "You will have eight turns to pick the correct letters that make up the mystery word.\n" +
    "I will keep track of your turns.\n" +
    "You can pick the level of difficulty easy, normal or hard.\n" + 
    "Easy mode contains 4-6 letters, Normal 6-8 and Hard at least 8.")
    play_game(easy, normal, hard)
    
