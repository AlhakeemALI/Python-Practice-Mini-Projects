import random

#Step 1
display = []
word_list = ["aardvark", "baboon", "camel", "swallow", "bungee", "cheese", "famine", "death","quince"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)



# print(chosen_word)

# Ask the user to guess a letter and assign their answer to a variable called guess

guess = input("Welcome to Hangman Game! Guess a letter.\n").lower()

# print(guess)

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word

for letter in chosen_word:
      if letter == guess:
       print("Right")
      else:
       print("Wrong")

# Step 2
# Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.

for word in chosen_word:
   display.append("_")
  
print(display)



# Loop through each position in the chosen_word

for i in range(len(chosen_word)):
   
   if chosen_word[i] == guess:
      display[i] = guess

print(display)      

    





