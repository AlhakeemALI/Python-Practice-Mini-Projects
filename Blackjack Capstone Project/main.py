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

user_cards = []
computer_cards = []

for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())
  # print(user_cards, computer_cards)
   

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(user_score, computer_score)

    
   
  




    
    