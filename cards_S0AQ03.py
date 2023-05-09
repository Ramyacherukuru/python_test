import math
import random
print("The person with highest number wins:")
friends = "Ajay,Balu,Chirag,Deny,Eris,Fox,Gopal,Henry,Irfan,Jaffar".split(",")
print(friends)
n_friends = 10
r = range(300, 326)
cards = random.sample(r, k = n_friends)
max_card = max(cards)
pos = cards.index(max_card)
print(cards)
print("winning card:", max_card)
print("winner is in the position:",pos + 1)
print("winner",friends[pos])
