import random

def dealer_draw():
    dealer_cards = []
    initial_card = random.randrange(2, 12)
    second_initial_card = random.randrange(2, 12)
    dealer_cards.append(initial_card)
    dealer_cards.append(second_initial_card)
    exit = False
    while exit == False:
        random_card = random.randrange(2, 12)
        if random_card == 11 and (sum(dealer_cards) + 11) > 21:
            random_card = 1
        dealer_cards.append(random_card)
        if sum(dealer_cards) < 17:
            continue
        elif sum(dealer_cards) >= 17:
            exit = True
    return dealer_cards

def print_score(win_count, lose_count):
    print("Games Won: ", win_count)
    print("Games Lost: ", lose_count)

def blackjack():
    win_count = 0
    lose_count = 0
    exit = False
    while exit == False:
        cards = []
        if win_count == 0 and lose_count == 0:
          print('Want to play?')
        if win_count != 0 or lose_count != 0:
          print('Want to play again?')
        print('Type y for yes')
        print('Type n for no')
        y = input()
        print('\n' * 2)
        if y.lower() in ['yes', 'y']:
            initial_card = random.randrange(2, 12)
            second_initial_card = random.randrange(2, 12)
            cards.append(initial_card)
            cards.append(second_initial_card)
            dealer_cards = dealer_draw()
            exit2 = False
            while exit2 == False:
                print('\n' * 100)
                print("Your cards value: ", sum(cards))
                if sum(cards) == 21:
                  print("BlackJack!")
                print("Your cards: ", cards)
                print("Dealer's Showing Card: ", dealer_cards[0])
                print('\n' * 2)
                print('Want to hit?')
                print('Type y for yes')
                print('Type n for no')
                x = input()
                print('\n' * 2)
                if x.lower() in ['yes', 'y']:
                    print('\n' * 100)
                    random_card = random.randrange(2, 12)
                    if random_card == 11 and (sum(cards) + 11) > 21:
                        random_card = 1
                    cards.append(random_card)
                    if sum(cards) == 21:
                        print("You got blackjack!")
                        print('\n' * 2)
                        print("Your cards: ", cards)
                        print("Dealer got: ", dealer_cards)
                        if sum(dealer_cards) > 21:
                            print("Dealer Busted. You win!")
                            win_count += 1
                        if sum(dealer_cards) >= sum(cards) and sum(dealer_cards) <= 21:
                            print("You lose.")
                            lose_count += 1
                        if sum(dealer_cards) < sum(cards):
                            print("You win!")
                            win_count += 1
                        print('\n' * 2)
                        print_score(win_count, lose_count)
                        print('\n' * 2)
                        exit2 = True
                    elif sum(cards) > 21:
                        print("Bust!")
                        print("Your final cards value: ", sum(cards))
                        lose_count += 1
                        print('\n' * 2)
                        print_score(win_count, lose_count)
                        exit2 = True
                        print('\n' * 2)
                else:
                    print('\n' * 100)
                    print("Your final cards value: ", sum(cards))
                    print("Dealer got: ", sum(dealer_cards))
                    if sum(dealer_cards) > 21:
                        print("Dealer Busted. You win!")
                        win_count += 1
                    if sum(dealer_cards) >= sum(cards) and sum(dealer_cards) <= 21:
                        print("You lose.")
                        lose_count += 1
                    if sum(dealer_cards) < sum(cards):
                        print("You win!")
                        win_count += 1
                    print('\n' * 2)
                    print_score(win_count, lose_count)
                    exit2 = True
                    print('\n' * 2)
        else:
            print('\n' * 100)
            print("Thanks for playing!")
            print_score(win_count, lose_count)
            exit = True
            break

blackjack()
