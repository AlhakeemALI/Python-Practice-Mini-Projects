import random

#Step 1

word_list = ["aardvark", "baboon", "camel", "swallow", "bungee", "cheese", "famine", "death","quince"]


#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

# Ask the user to guess a letter and assign their answer to a variable called guess

guess = input("Welcome to hangman hame guess a letter").lower()

print(guess)

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word

if guess in chosen_word:
      print("The letter {} is in the chosen word.".format(guess))
else:
    print("The letter {} is not in the chosen word.".format(guess))

