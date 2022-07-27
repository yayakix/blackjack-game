import random

deck_of_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


def get_new_card(deck):
  new_card = random.choice(deck_of_cards)
  deck.append(new_card)

  
def calculate_deck(deck):
  deck_total = 0
  for card in deck:
    deck_total += card
  return deck_total
  
def check_status(user_deck, game_deck, first_round_check):
  if first_round_check:
    print(f'The computers first card is {game_deck}')
  else:
    print(f'The computers deck is {game_deck}')
  print(f'Your current deck is {user_deck}')
  
def check_totals(user_total, game_total, user_deck, game_deck):
  game_total = calculate_deck(game_deck)
  user_total = calculate_deck(user_deck)
  if game_total < 16:
    get_new_card(game_deck)
    calculate_deck(game_deck)
    check_totals(user_total, game_total, user_deck, game_deck)
  elif game_total > 21:
    print('computer lose they went over 21')
  elif game_total <= 21:
    if user_total > game_total:
      print('user wins, high num than game')
    elif game_total > user_total:
      print('computer wins, higher num than user')
    elif game_total == user_total:
      print('its a tie') 
  check_status(user_deck, game_deck, False)

def move_on(user_deck,game_deck):
  game_total = calculate_deck(game_deck)
  user_total = calculate_deck(user_deck)
  check_totals(user_total, game_total, user_deck, game_deck)
  
ask_game = input('do you want to play a game of blackjack?\n y or n \n')    
if ask_game == 'y':
  user_deck = []
  game_deck = []
  get_new_card(user_deck)
  get_new_card(user_deck)
  get_new_card(game_deck)
  check_status(user_deck, game_deck, True)

  more_cards = True
  while more_cards:
    ask_new_card = input('Would you like to draw another card? y or n \n')
    if ask_new_card == 'y':
      get_new_card(user_deck)
      check_status(user_deck, game_deck, True)
      user_total = calculate_deck(user_deck)
      if user_total > 21:
        if 11 in user_deck:
          for i in range(len(user_deck)):
            if user_deck[i] == 11:
              user_deck[i] = 1
          if calculate_deck(user_deck) < 21:
            print('ok u can continue')
            more_cards = True
        # check if 11 is in deck
        else:
          print('Game over you went over 21')
          more_cards = False

    elif ask_new_card == 'n':
      get_new_card(game_deck)
      more_cards = False
      move_on(user_deck, game_deck)
      