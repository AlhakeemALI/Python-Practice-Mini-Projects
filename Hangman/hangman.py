import random
import Hangman.hangman_words as hangman_words
import Hangman.hangman_art as hangman_art
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
display = []
lives = 6
for word in chosen_word:
   display.append("_")
print(chosen_word)
game_over = False
while not game_over:
    guess = input("Welcome to Hangman Game! Guess a letter.\n").lower()

    for i in range(len(chosen_word)):
              if chosen_word[i] == guess:
                display[i] = guess
    print(display)  
    if guess not in chosen_word:
         lives -= 1
         if lives == 0:
              game_over = True
              print("You lose.")
    if "_" not in display:
          game_over = True
          print("You Win")
    print(hangman_art.stages[lives])      
    


 

    





