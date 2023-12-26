import random
from art import logo

def clear():  # Prints 50 blank lines
    print("\n" * 50)

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user1_score, user2_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user1_score > 21 and user2_score > 21:
    return "user1 went over. user1 lose 😤"
  if user1_score == user2_score:
    return "Draw 🙃"
  elif user2_score == 0:
    return "Lose, user2 has Blackjack -user2 win 😱"
  elif user1_score == 0:
    return "user1 Win with a Blackjack 😎"
  elif user1_score > 21:
    return "user1 went over. user1 lose  😭"
  elif user2_score > 21:
    return "user2 went over. user1 win 😁"
  elif user1_score > user2_score:
    return "user1 win 😃"
  else:
    return "user2 win 😃 "

def play_game():

  print(logo)

  #Hint 5: Deal the user and computer 2 cards each using deal_card()
  user1_cards = []
  user2_cards = []
  is_game_over = False
  is_game_over1 = False

  for _ in range(2):
    user1_cards.append(deal_card())
    user2_cards.append(deal_card())

  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

  while not is_game_over:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user1_score = calculate_score(user1_cards)
    user2_score = calculate_score(user2_cards)
    print(f"   user1 cards: {user1_cards}, current score: {user1_score}")
    print(f"   user2's first card: {user2_cards[0]}")

    if user1_score == 0 or user2_score == 0 or user1_score > 21:
      is_game_over = True
    else:
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user1_cards.append(deal_card())
        # user2_cards.append(deal_card())
      else:
        is_game_over = True
  clear()
  while not is_game_over1:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user1_score = calculate_score(user1_cards)
    user2_score = calculate_score(user2_cards)
    print(f"   user1's cards: {user1_cards[0]}")
    print(f"   user2's first card: {user2_cards}, current score: {user2_score}")

    if user1_score == 0 or user2_score == 0 or user2_score > 21:
      is_game_over1 = True
    else:
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        # user1_cards.append(deal_card())
        user2_cards.append(deal_card())
      else:
        is_game_over1 = True

  print(f"   user1's final hand: {user1_cards}, final score: {user1_score}")
  print(f"   user2's final hand: {user2_cards}, final score: {user2_score}")
  print(compare(user1_score, user2_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
