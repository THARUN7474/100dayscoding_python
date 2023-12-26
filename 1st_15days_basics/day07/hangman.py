import random
from hangmanwords import word_list
from hangmanart import logo,stages
lives=6
gameend=False
print(logo)
a=6
chosen_word=random.choice(word_list)
print("chosenword is"+chosen_word)
output=[]
for i in range(len(chosen_word)):
    output+='_'
print(output)
while gameend==False:
    guess=input("guess the letter: ").lower()
    if guess in output:
        print(f"you already guessed {guess}\n")

    for pos in range(len(chosen_word)):
        # print(chosen_word[pos])
        if chosen_word[pos]==guess:
            print("you guessed the letter correct\n")
            output[pos]=guess
    # print(output)
    # l=chosen_word.split( )
    # print(l)
    if guess not in chosen_word:
        print("You guessed {guess} that's not in the word. You lose a life.")
        lives-=1
        if lives==0:
            gameend=True
            print("game completed, you lose!!\n")
    
    print(f"{' '.join(output)}")
    if '_' not in output:
        gameend=True
        print("game completed,you won!!")
    print(stages[lives])


    
    

