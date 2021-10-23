#! env\bin\python
# Ryan Simmons
# Tic Tac Toe game
from string import digits


class TicTacToe:

    def __init__(self):

        self.board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        self.row = 3
        self.column = 3
        self.last_move = 'O'

    def win_checker(self):
        x_wins = 0  # local variables
        o_wins = 0

    # Checking for WINS in the rows
        for y in range(self.column):
            if self.board[y] == ['X', 'X', 'X']:
                x_wins += 1
            if self.board[y] == ['O', 'O', 'O']:
                o_wins += 1

    # Checking for WINS in the columns
        for z in range(self.row):
            if self.board[0][z] == self.board[1][z] == self.board[2][z]:
                if self.board[0][z] == 'X':
                    x_wins += 1
                elif self.board[0][z] == 'O':
                    o_wins += 1

    # Checking for WINS in the diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            if self.board[0][0] == 'X':
                x_wins += 1
            elif self.board[0][0] == 'O':
                o_wins += 1

        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            if self.board[0][2] == 'X':
                x_wins += 1
            elif self.board[0][2] == 'O':
                o_wins += 1

    # Returning results of game

        if x_wins > o_wins:
            print('X wins')
            return False
        elif o_wins > x_wins:
            print('O wins')
            return False
        elif any(True for y in range(self.column) if '_' in self.board[y]):
            return True
        else:
            print('Draw')
            return False

    def board_printer(self):

        print('---------')
        print('|', " ".join(self.board[0]), '|')
        print('|', " ".join(self.board[1]), '|')
        print('|', " ".join(self.board[2]), '|')
        print('---------')

    def move_request(self):

        while True:
            z, y = input('Enter the coordinates: ').split()
            if z not in digits or y not in digits:
                print('You should enter numbers!')
            else:
                z = int(z)  # z-1 converts Cartesian to index
                y = int(y)  # -y converts Cartesian to index

                if (z not in range(1, 4)) or (y not in range(1, 4)):
                    print('Coordinates should be from 1 to 3!')
                elif self.board[-y][z-1] != '_':
                    print('This cell is occupied! Choose another one!')
                else:
                    if self.last_move == 'O':
                        self.board[-y][z-1] = 'X'
                        self.last_move = 'X'
                        break
                    elif self.last_move == 'X':
                        self.board[-y][z-1] = 'O'
                        self.last_move = 'O'
                        break

    def game(self):
        self.board_printer()
        while self.win_checker():
            self.move_request()
            self.board_printer()


the_game = TicTacToe()
the_game.game()
