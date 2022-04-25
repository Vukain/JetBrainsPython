import random


class Computer:

    def __init__(self, sign, diff, idx):
        self.sign = sign
        self.difficulty = diff
        self.win = False
        self.idx = idx

    def play(self, table):
        if self.difficulty == 'easy':
            choice = random.randrange(0, 9)

            while table[choice] != " ":
                choice = random.randrange(0, 9)

            table[choice] = self.sign
            print('Making move level "easy" -', self.sign)
        elif self.difficulty == 'medium':
            threes = [[table[0], table[1], table[2]], [table[3], table[4], table[5]],
                      [table[6], table[7], table[8]], [table[0], table[3], table[6]],
                      [table[1], table[4], table[7]], [table[2], table[5], table[8]],
                      [table[0], table[4], table[8]], [table[2], table[4], table[6]]]
            for index, three in enumerate(threes):
                if three.count(" ") == 1 and three.count("X") == 2 or three.count("0") == 2:
                    three_num = index
                    empty = threes[index].index(" ")
                    if index < 3:
                        choice = 3 * index + empty
                    elif index < 6:
                        choice = index - 3 + 3 * empty
                    elif index == 6:
                        choice = empty * 4
                    else:
                        choice = 2 + empty * 2
                    table[choice] = self.sign

                    break
            else:
                choice = random.randrange(0, 9)
                while table[choice] != " ":
                    choice = random.randrange(0, 9)
                table[choice] = self.sign
            print('Making move level "medium" -', self.sign)
        else:
            if len(self.empty_indices(table)) == 9:
                choice = random.randrange(0, 9)
                while table[choice] != " ":
                    choice = random.randrange(0, 9)
            else:
                choice = self.minimax(table, self.sign, self.sign)[1]
            table[choice] = self.sign

            print('Making move level "hard" -', self.sign)

    @staticmethod
    def empty_indices(board):
        return [i for i, e in enumerate(board) if e == " "]

    @staticmethod
    def minimax(boardie, ai_sign, next_move):
        empty_spots = Computer.empty_indices(boardie)
        enemy = get_opponent_side(ai_sign)

        if Game.win_checker(boardie, enemy):
            return -10, -1
        elif Game.win_checker(boardie, ai_sign):
            return 10, -1
        elif len(empty_spots) == 0:
            return 0, -1

        next_side = get_opponent_side(next_move)

        moves = dict()

        for i in range(9):
            if boardie[i] == " ":

                bords = boardie[:]
                bords[i] = next_move
                score, index = Computer.minimax(bords, ai_sign, next_side)
                moves[i] = score
                # print(moves)

        best_index = -1
        if ai_sign == next_move:
            best_score = -100
            for index, score in moves.items():
                if score > best_score:
                    best_score = score
                    best_index = index
        else:
            best_score = 100
            for index, score in moves.items():
                if score < best_score:
                    best_score = score
                    best_index = index

        return best_score, best_index


def get_opponent_side(side):
    if side == 'X':
        return 'O'
    if side == 'O':
        return 'X'
    return None


class Player:

    def __init__(self, sign):
        self.sign = sign
        self.win = False

    def play(self, table):
        while True:
            coordinate = 0
            numbs = input("Enter the coordinates (column row): ")

            if " " not in numbs:
                print("Bad format, You shold enter 'X Y'")
                continue
            else:
                numbs = numbs.split()
          
            if (not numbs[0].isnumeric()) or (not numbs[1].isnumeric()):
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
                table[coordinate] = self.sign
                break
            else:
                print("This cell is occupied! Choose another one!")
                continue

            print('ouch')


class Game:

    def __init__(self):
        self.table = [" " for i in range(9)]
        self.players = []
        self.playing = True
        self.state = ""

    def table_printer(self):
        print(f"""---------
| {self.table[6]} {self.table[7]} {self.table[8]} |
| {self.table[3]} {self.table[4]} {self.table[5]} |
| {self.table[0]} {self.table[1]} {self.table[2]} |
---------""")

    @staticmethod
    def win_checker(table, sign):
        threes = [[table[0], table[1], table[2]], [table[3], table[4], table[5]],
                  [table[6], table[7], table[8]], [table[0], table[3], table[6]],
                  [table[1], table[4], table[7]], [table[2], table[5], table[8]],
                  [table[0], table[4], table[8]], [table[2], table[4], table[6]]]
        for three in threes:
            if sign == three[0] and sign == three[1] and sign == three[2]:
                return True

    def game_starter(self):

        while True:
            print("To start a game enter 'start player_type player_type'.")
            print("Player types - user, easy, medium, hard.")
            print("To quit enter 'exit'.")
            choice = input("Input command: ")
            if choice == "exit":
                self.playing = False
                break
            else:
                options = choice.split()
                for option in options:
                    if option not in ['start', 'user', 'easy', 'medium', 'hard']:
                        print("Bad parameters")
                        break
                else:
                    p1 = Player("X") if options[1] == "user" else Computer("X", options[1], 0)
                    p2 = Player("O") if options[2] == "user" else Computer("O", options[2], 1)
                    self.players.extend([p1, p2])
                    self.table_printer()
                    break

    def game_on(self):
        while self.playing:
            for player in self.players:
                player.play(self.table)
                self.table_printer()

                if self.win_checker(self.table, player.sign):
                    print(f"{player.sign} wins")
                    self.state = f"{player.sign}"
                    self.playing = False
                    break
                elif " " not in self.table:
                    print("Draw")
                    self.state = "Draw"
                    self.playing = False
                    break


game = Game()
game.game_starter()
game.game_on()
