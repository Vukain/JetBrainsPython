table = list(input("Enter cells: "))

print(f"""---------
| {table[0]} {table[1]} {table[2]} |
| {table[3]} {table[4]} {table[5]} |
| {table[6]} {table[7]} {table[8]} |
---------""")

threes = [[table[0], table[1], table[2]], [table[3], table[4], table[5]], [table[6], table[7], table[8]],
            [table[0], table[3], table[6]], [table[1], table[4], table[7]], [table[2], table[5], table[8]],
            [table[0], table[4], table[8]], [table[2], table[4], table[6]]]
players = [["X", False], ["O", False]]

difference = abs(table.count("X") - table.count("O"))

for player in players:
    win = False
    for three in threes:
        if player[0] == three[0] and player[0] == three[1] and player[0] == three[2]:
            win = True
        if win:
            player[1] = True
            break

if (players[0][1] and players[1][1]) or difference > 1:
    print("Impossible")
elif not(players[0][1] or players[1][1]):
    if "_" in table:
        print("Game not finished")
    else:
        print("Draw")
else:
    for player in players:
        if player[1]:
            print(f"{player[0]} wins")