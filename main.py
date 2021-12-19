from word import word_list
from art import hangman_pics
import random
# optional
import os


def display_word_generator(guess_word):
    display_word = []
    for num in range(len(guess_word)):
        display_word.append("__")
    return display_word


def new_word():
    return random.choice(word_list)


# init game
word_to_guess = ""
word_to_display = ""
life = 5
level = 1

# debug logs
print(word_to_display)
# print(word_to_guess)

# main game loop starts here
print("welcome to hangman")
playing = True
while(playing):
    os.system("clear")
    if(life == 0):
        if(input("would you like to play again\n 'y' for yes \n>") == "y"):
            word_to_guess = ""
            word_to_display = ""
            life = 5
            level = 1
        else:
            playing = False
            break

    elif("__" not in word_to_display):
        word_to_guess = new_word()
        word_to_display = display_word_generator(word_to_guess)
        level += 1
        life += 1 if life < 5 else 0
        print(f"good job, upto next lvl you go, you gained 1 more life, now life is {life} :>\n\n" if (
            level > 2) else "\n\n")
    print(word_to_guess)
    print(word_to_display)
    user_guess = input("what is your guess?\n>")

    if(user_guess in word_to_guess and user_guess not in word_to_display):

        for n in range(len(word_to_display)):
            if((word_to_guess[n]) == user_guess):
                word_to_display[n] = user_guess

    else:
        life -= 1
        print(f"you lost a life, you have {life} remaining")
        print(hangman_pics[life])
print(f"you had a good run, you were in lvl {level}")
