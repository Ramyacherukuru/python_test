import math
import random
n_friends = 10
friends = "A,B,C,D,E,F,G,H,I,J".split(",")
r = range(99, 1000)
cards = random.sample(r, k = n_friends)
max_card = max(cards)
pos = cards.index(max_card)
print(cards)
print("winning card:", max_card)
print("The person with highest number wins:", friends[pos])
print("The cards which one is picked:", cards_pick)

 
