total_cards = int (input ("Enter the amount of cards: "))
total_sum = 0
for card in range (1, total_cards+1):
    total_sum += card
for card in range (total_cards-1):
    remaining_card = int (input ("The number of remaining card: "))
    total_sum -= remaining_card
print ("The number of lost card is :", total_sum)