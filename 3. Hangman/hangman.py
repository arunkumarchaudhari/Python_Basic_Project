import random
def hangman():
    word =random.choice(['arun','prabin','sumit','megha','jyotsna','Python'])
    validletters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    turns = 5
    temp_word=""
    for i in word:
        temp_word=temp_word+"0"
    flag=False
    while turns>0:
        if "0" not in temp_word:
            print("Congratulation! You have successfully guessed the word.")
            print("Word was: ",word)
            flag=True
            break   
        print("Guess the word: ",end="")
        for j in range(len(temp_word)):
            if(temp_word[j]=="0"):
                print("_",end=" ")
            else:
                print(temp_word[j],end=" ")
        guessed = input("\n")
        print(guessed)
        if guessed in validletters:
            print("valid letter")
            if guessed in word:
                ind = word.find(guessed)
                temp_word = temp_word[:ind] + guessed + temp_word[ind+1:]
            else:
                turns=turns-1
                print("Turns remaining: ",turns)
        else:
            print('Enter valid letters only')
    
    if not flag:
        print("You lost the game, Please try again.")


name = input('Enter your name: ')
print("\n")
print("Welcome",name)
print("---------------------")
print("Try to guess the word in less than 5 attempts")
hangman()


#NOTE: There are some bugs in Program which I will be solving very soon, else this is working perfectily fine
# bugs is for the word naman -> as it has repeating character.