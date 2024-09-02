import nltk
import random
#nltk.download('words')
from nltk.corpus import words

word_list = words.words()

hangman_art = {0: ("   ","   ","   "),1: (" o ","   ","   "),2: (" o "," | ","   "),3: (" o ","/| ","   "),
               4: (" o ","/|\\","   "),5: (" o ","/|\\","/  "),6: (" o ","/|\\","/ \\")}



def dysplay_man (Wrong_gueeses):
    for line in hangman_art[Wrong_gueeses]:
        print (line)

def dysplay_hint(hint):
    print(" ".join(hint))
def dysplay_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(word_list).lower()
    hint = ["_"]*len(answer)
    print (hint)
    wrong_gueeses = 0
    gueeses_letter = set()
    is_running = True

    while is_running:
        dysplay_man(wrong_gueeses)
        dysplay_hint(hint)
        guess = input("enter a letter: ").lower()
        gueeses_letter.add(guess)

        if len(guess) !=1 or not guess.isalpha():
            print("Invalid input")
            continue
        if guess in gueeses_letter:
            print(f"{guess} is already guessed")
            continue    
        if guess in answer:
            for i in range (len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_gueeses += 1
        if "_" not in hint:
            dysplay_man(wrong_gueeses)
            dysplay_answer(answer)
            print("YOU WIN")
            is_running = False
        elif wrong_gueeses >= len(hangman_art)-1:
            dysplay_man(wrong_gueeses)
            dysplay_answer(answer)
            print ("YOU LOSE")
            is_running =False
        

if __name__ == "__main__":
    main()
