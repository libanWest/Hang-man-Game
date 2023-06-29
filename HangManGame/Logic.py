from WordsGraphics import hangman_graphics


def ShowHangMan(guess):
    image = hangman_graphics[guess]
    print (image)
    return image 
def ShowRightWords(guess,word,copy):
    index = []
    for i in range(len(word)):
        if word[i] == guess:
            index.append(i)
    
    for i in index:
        copy[i] = guess
    
    return copy