import random
from art import logo

print(logo)

def deal_card():
   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   card = random.choice(cards)
   return card

def calculate_score(list):
    score = 0
    for index in list:
        score += index
        if score == 21 and len(list) == 2:
            return 0
    if score > 21 and 11 in list:
        print(list)
        list.remove(11)
        list.append(1)
        # score = sum(list)
        print(list)
        print(score)
    return score

def compare(user_score, computer_score):
  if user_score  == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "You Lose"
  elif user_score == 0:
    return "You win"
  elif user_score > 21:
    return "You Lose"
  elif computer_score > 21:
    return "You Win"  
  elif user_score > computer_score:
    return "You win"
  else:
    return "You Lose"
    

def play_game():
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    # print(user_cards, computer_cards)
     
  while not is_game_over:
    
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    if  user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_respond = input("Do You want to draw another card. 'Y' or 'N'\n").lower()
      if user_respond == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True 
  while  computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print(f"Your final hand: {user_cards}, final score: {user_score}") 
  print(f"Computer's final hand: {computer_cards} final score: {computer_score}")
  print(compare(user_score,computer_score))

final_respond = input("Do you want to paly? 'Y' or 'N'").lower()
while final_respond == 'y':
  play_game()

    
   
  




    
    