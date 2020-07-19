# write your code here
table = list(input('Enter cells: ').replace("_", " "))

def table_printer():
    print(f"""---------
| {table[0]} {table[1]} {table[2]} |
| {table[3]} {table[4]} {table[5]} |
| {table[6]} {table[7]} {table[8]} |
---------""")
    
def pos_enter(table):
    while True:
        coordinate = 0
        numbs = input("Enter the coordinates: ").split()
        
        if not numbs[0].isnumeric() or not numbs[1].isnumeric():
            print("You should enter numbers!")
            continue
        elif numbs[0] not in "123" or numbs[1] not in "123":
            print("Coordinates should be from 1 to 3!")
            continue
        else:
            if numbs[1] == "1":
                coordinate += 6
            elif numbs[1] == "2":
                coordinate += 3
            coordinate += int(numbs[0]) - 1
        
        if table[coordinate] == " ":
            table[coordinate] = "X"
            break
        else:
            print("This cell is occupied! Choose another one!")
            continue
            
        
    
table_printer()
pos_enter(table)
table_printer()

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
