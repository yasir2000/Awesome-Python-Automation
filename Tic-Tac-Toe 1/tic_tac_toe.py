# .env
# This file would contain environment variables.
PLAYER_SYMBOL='X'
COMPUTER_SYMBOL='O'

import os
import random

class Board:
    """Class to represent the Tic Tac Toe board."""
    
    def __init__(self):
        self.board = [i for i in range(0, 9)]
    
    def print_board(self):
        """Print the current state of the board."""
        x = 1
        for i in self.board:
            end = ' | '
            if x % 3 == 0:
                end = ' \n'
                if i != 1:
                    end += '---------\n'
            char = ' '
            if i in ('X', 'O'):
                char = i
            x += 1
            print(char, end=end)

    def can_move(self, move):
        """Check if a move can be made."""
        return move in range(1, 10) and self.board[move - 1] == move - 1

    def make_move(self, player, move):
        """Make a move on the board."""
        if self.can_move(move):
            self.board[move - 1] = player
            return True
        return False

    def space_exist(self):
        """Check if there are any spaces left on the board."""
        return self.board.count('X') + self.board.count('O') != 9

    def check_winner(self, player):
        """Check if specified player has won."""
        winners = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8), 
            (0, 3, 6), (1, 4, 7), (2, 5, 8), 
            (0, 4, 8), (2, 4, 6)
        )
        for tup in winners:
            if all(self.board[i] == player for i in tup):
                return True
        return False

class Player:
    """Class to represent a player in the game."""
    
    def __init__(self, symbol):
        self.symbol = symbol

class Computer(Player):
    """Class to represent the computer player, inheriting from Player."""
    
    def __init__(self):
        super().__init__(os.getenv("COMPUTER_SYMBOL", 'O'))

    def make_move(self, board):
        """Determine the computer's move."""
        for i in range(1, 10):
            if board.can_move(i) and board.make_move(self.symbol, i):
                if board.check_winner(self.symbol):
                    return i
                board.make_move(i, i)  # Undo
        for i in range(1, 10):
            if board.make_move(os.getenv("PLAYER_SYMBOL", 'X'), i):
                if board.check_winner(os.getenv("PLAYER_SYMBOL", 'X')):
                    board.make_move(self.symbol, i)  # Block
                    return i
                board.make_move(i, i)  # Undo
        return self.select_best_move(board)

    def select_best_move(self, board):
        """Greater strategy to select moves."""
        moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))
        move = -1
        for tup in moves:
            for mv in tup:
                if board.can_move(mv):
                    move = mv
                    break
            if move != -1:
                break
        return move

def select_char():
    """Randomly select symbols for the player and the computer."""
    return (os.getenv("PLAYER_SYMBOL", 'X'), os.getenv("COMPUTER_SYMBOL", 'O'))

def main():
    player_symbol, computer_symbol = select_char()
    player = Player(player_symbol)
    computer = Computer()
    board = Board()

    print(f'Player is [{player.symbol}] and computer is [{computer.symbol}]')
    result='%%% Draw! %%%'

    while board.space_exist():
        board.print_board()
        print('# Make your move! [1-9]: ', end='')
        move = int(input())

        if not board.make_move(player.symbol, move):
            print('Invalid number! Try again!')
            continue

        if board.check_winner(player.symbol):
            result='*** Congratulations! You won! ***'
            break
        
        if computer.make_move(board) != -1 and board.check_winner(computer.symbol):
            result='=== You lose! ==='
            break

    board.print_board()
    print(result)

if __name__ == '__main__':
    main()
