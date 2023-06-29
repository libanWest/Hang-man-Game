import random
from getpass import getpass
from WordsGraphics import hangman_graphics,congratulation,gameover,gameover2,welcome
from Logic import ShowRightWords,ShowHangMan

            
# num of guesses 
# set of wrong answers so user cant enter wrong ans twice
guesses = 0
guessed_letters = set()

print(welcome[0])

#Player 1 input word & hint

word = list(getpass('\tPlease enter a word: ').lower())
hint = input("\tPlease enter a hint:")
copy = ["-"] * len(word)

#print(word)

while guesses < 6:
    
    guessWord  = input("\tEnter your guess letter: ").lower()
  
    if guessWord in guessed_letters:
        print("\tYou already guessed that letter!. Please try again.")

    elif guessWord not in word:
        guesses += 1
        print("\n" *9)
        print("\t",ShowRightWords(guessWord,word,copy))
        print("\t Incorrect. You have", 6-guesses, "guesses remaining.")
        guessed_letters.add(guessWord)
        print("\t HINT\n","\t","'",hint,"'")
        ShowHangMan(guesses)
      
    else:
        print("\n" *9)
        print("\t",ShowRightWords(guessWord,word,copy))
        print("\t HINT\n","\t","'",hint,"'")
        ShowHangMan(guesses)
        print("\n\tWell done! continue.")
       
    if copy == word:
        print("\n" *9)
        print("\n",congratulation[0],"\n")
        print("\n\t\tPlayer 2 Won! \n\t\tYou guessed all the letters!\n\t\tThe word was:", ''.join(word),"\n", )
        break
         
if guesses >= 6:
    print(gameover2[0])
    print("\t\tSorry, you lost. Player 1 Won! \n\t\tThe word was:", "'",''.join(word),"'")
    #printImage(guesses)





    