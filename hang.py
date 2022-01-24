import random
def hangman():
    word_list=("india","delhi","laptop","hangman")
    word=random.choice(word_list)
    turns=6
    guessmade=""
    valid_entry=set("abcdefghijklmnopqrstuvwxyz")
    # while len(word)>0:
    while True:
        main_word=""
        missed=0
        for letter in word:
            if letter in guessmade:
                main_word=main_word +letter
            else:
                main_word=main_word+"_"
        if main_word ==word:
            print("main_word")
            print("you won!!")
            break

        print("guess the words ",main_word)
        guess=input("enter the name!!!!")
        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print("enter the character")
            guess=input("enter the")
        if guess not in word:
            turns=turns-1
            if turns==9:
                print("9 turns left!!!")
                print("-----------------")
            if turns==8:
                print("8 turns left!!!")
                print("---------------")
                print("o")
            if turns==7:
                print("7 turns left!!!")
                print("-------------")
                print("o")
                print("|")
            if turns==6:
                print("6 turns left!!!")
                print("---------------")
                print("o")
                print("|")
                print("/ \ ")
            if turns==5:
                print("5 turns left!!!")
                print("-------------")
                print("  o")
                print("  |")
                print("  /\   ")
            if turns==4:               
                print("4 turns left!!!")
                print("  \o")
                print("   |   ")
                print("   /\ ")
            if turns==3:
                print("3 turns left!!!")
                print("   \o/ ")
                print("    |   ")
                print("    /|\ ")
            if turns==2:
                print("2 turns left!!!")
                print("  \o/--|")
                print("   |  ")
                print("   /|\   ")
            if turns==1:
                print("1 turns left!!!")
                print("|--\o/--|")
                print("     |")
                print("     /|\   ")
            if turns==0:
                print("you are loose")
                print("you let a good man die")
                break
name=input("enter the name")
print("welcome in hangmam")
print("you have only five")
hangman()