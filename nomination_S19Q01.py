#{"Football":['Ashish','vinay']} first 2 parts
#{"Sanketh":['Basket ball',cricket'], "Ashish":[]

Games = dict()
Games1 = dict()
with open("nomination.txt", 'r') as FH:
    
    for line in FH:
        player, sport = line.strip().split('-')
        
        if sport not in Games:
            Games[sport] = [player]
        else:
            Games[sport].append(player)

        if player not in Games1:
            Games1[player] = [sport]
        else:
            Games1[player].append(sport)           
            
#dict.keys() to get keys
print("Games that have nominations:")
for game in Games.keys():
    print(game)
    
for sport in Games:
    print("players playing:", sport)

    for name in Games[sport]:
        print(name)


print("players who play more than one sport:")

for player in Games1.keys():
    if len(Games1[player]) > 1:
        print(player)

print("players who plays only one sport:")

for player in Games1.keys():
    if len(Games1[player]) == 1:
        print(player)
    
#pprint: pretty print

















































































