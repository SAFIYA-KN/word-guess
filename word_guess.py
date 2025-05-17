import random
word_bank=["helicopter","rajagiri","encyclopedia","watermelon","supervisor","sanctuary"]
word=random.choice(word_bank)

guessed=["_"]*len(word)
chance=12
while chance>0:
    print("\ncurrent word "+" ".join(guessed))
    guess=input("guess a letter:").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                guessed[i]=guess
        print("\nyou guessed it right!! ;)")
    else:
        chance-=1
        print("\noops!that wasn't right :( \n you have "+str(chance)+" left.\n")

    
    if '_' not in guessed:
        print("YAAY!! you guessed the word right "+word) 
        break

if "_" in guessed:
    print("oops! you ran out of attempts \nthe word was "+word)
        
    

