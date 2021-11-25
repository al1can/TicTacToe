import random

class TicTacToe:
    def __init__(self):
        self.table = []

    def create_table(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.table.append(row)

    def is_board_filled(self):
        is_filled = True
        for row in self.table:
            for element in row:
                if element=='-':
                    is_filled = False
        return is_filled

    def is_player_won(self,player):
        is_won = None
        size = len(self.table)
        for row in range(size):
            is_won = True
            for element in range(size):
                if self.table[row][element]!=player:
                    is_won = False
                    break
            if is_won:return is_won

        for row in range(size):
            is_won = True
            for column in range(size):
                if self.table[column][row]!=player:
                    is_won = False
                    break
            if is_won:return is_won
        
        for element in range(size):
            is_won = True
            if self.table[element][element]!=player:
                is_won = False
                break
        if is_won:return is_won

        for element in range(size):
            is_won = True
            if self.table[element][size - 1 - element]!=player:
                is_won = False
                break
        if is_won:return is_won

        return is_won
        
    def show_table(self):
        for row in self.table:
            for element in row:
                print(f"{element} ",end="")
            print("\n")

    def random_player(self):
        player = random.choice(['X','O'])
        return player

    def player_move(self,player):
        print(f"Now it is {player}'s turn.")
        while True:
            row,column = list(map(int, input().split()))

            if self.table[row][column]=='-':
                self.table[row][column] = player
                break
            else:
                print("This place is not available. Try again different spot!")

    def player_swap(self,player):
        return 'X' if player=='O' else 'O'
    def start(self):
        self.create_table()
        player = self.random_player()

        while True:
            self.show_table()

            player = self.player_swap(player)

            self.player_move(player)
            if self.is_player_won(player):
                print(f"player {player} is won!")
                break

            if self.is_board_filled():
                print("It is a draw!")
                break
        self.show_table()


tic_tac_toe = TicTacToe()
tic_tac_toe.start()