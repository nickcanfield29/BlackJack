import random

def dealer_draw():
    cards = []
    initial_card = random.randrange(1, 12)
    second_initial_card = random.randrange(1, 12)
    cards.append(initial_card)
    cards.append(second_initial_card)
    exit = False
    while exit == False:
        random_card = random.randrange(1, 12)
        if random_card == 11 and (sum(cards) + 11) > 21:
            random_card = 1
        cards.append(random_card)
        if sum(cards) < 17:
            continue
        elif sum(cards) >= 17:
            exit = True
    return sum(cards)

def print_score(win_count, lose_count):
    print("Games Won: ", win_count)
    print("Games Lost: ", lose_count)

def blackjack():
    win_count = 0
    lose_count = 0
    exit = False
    while exit == False:
        cards = []
        y = input("Want to play?\n")
        if y.lower() in ['yes', 'y']:
            initial_card = random.randrange(1, 12)
            second_initial_card = random.randrange(1, 12)
            cards.append(initial_card)
            cards.append(second_initial_card)
            exit2 = False
            while exit2 == False:
                print("Your cards value: ", sum(cards))
                print(cards)
                x = input("Want to hit?\n")
                if x.lower() in ['yes', 'y']:
                    random_card = random.randrange(1, 12)
                    if random_card == 11 and (sum(cards) + 11) > 21:
                        random_card = 1
                    cards.append(random_card)
                    if sum(cards) == 21:
                        print("You got blackjack!")
                        print("Your cards: ", cards)
                        dealer_value = dealer_draw()
                        print("Dealer got: ", dealer_value)
                        if dealer_value > 21:
                            print("Dealer Busted. You win!")
                            win_count += 1
                        if dealer_value >= sum(cards) and dealer_value < 21:
                            print("You lose.")
                            lose_count += 1
                        if dealer_value < sum(cards):
                            print("You win!")
                            win_count += 1
                        print_score(win_count, lose_count)
                        exit2 = True
                    elif sum(cards) > 21:
                        print("Bust!")
                        print("Your final cards value: ", sum(cards))
                        lose_count += 1
                        print("Thanks for playing!")
                        print_score(win_count, lose_count)
                        exit2 = True
                else:
                    print("Your final cards value: ", sum(cards))
                    dealer_value = dealer_draw()
                    print("Dealer got: ", dealer_value)
                    if dealer_value > 21:
                        print("Dealer Busted. You win!")
                        win_count += 1
                    if dealer_value >= sum(cards) and dealer_value < 21:
                        print("You lose.")
                        lose_count += 1
                    if dealer_value < sum(cards):
                        print("You win!")
                        win_count += 1
                    print_score(win_count, lose_count)
                    exit2 = True
        else:
            print("Thanks for playing!")
            print_score(win_count, lose_count)
            exit = True
            break

blackjack()