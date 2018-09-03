# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 16:22:19 2018

@author: Sullysaurus
"""
import copy

class game_state(object):
    def __init__(self):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
     
    # Define print
    def __str__(self):
        return (self[0][0] + "│" + self[0][1] + "│" + self[0][2] + "\n" +
                "─┼─┼─\n" +
                self[1][0] + "│" + self[1][1] + "│" + self[1][2] + "\n" +
                "─┼─┼─\n" +
                self[2][0] + "│" + self[2][1] + "│" + self[2][2] + "\n")
    
    # Define indexing
    def __getitem__(self, idx):
        return self.board[idx - 1]
    
    # Define hash
    """
    https://stackoverflow.com/questions/12512511/automatically-making-a-class-hashable
    """
    def __key(self):
        return self.__str__()
    
    def __eq__(x, y):
        return x.__key() == y.__key()
    
    def __hash__(self):
        return hash(self.__key())
    
    # locate player with current turn
    def turn(self):
        """
        
        """
        flat = [item for sublist in self for item in sublist]
        if flat.count("X") == flat.count("O"):
            return "X"
        else:
            return "O"
    
    def move(self, row, col):
        """
        
        """
        print("{player} plays at ({row}, {col})".format(player = self.turn(),
              row = row, col = col))
        self.board[row][col] = self.turn()
        print('{board}'.format(board = self))
    
    def winner(self):
        """
        checks if the game is at a terminal game state, returns symbol of
        winner or nothing
        """
        n_row = len(self.board)
        player_list = [["X"], ["O"]]
        
        # win-diagonal
        diag_down = []
        diag_up   = []
        for i in range(n_row):
            diag_down.append(self[i            ][i])
            diag_up  .append(self[n_row - i][i])
        if list(set(diag_down)) in player_list:
            return list(set(diag_down))
        if list(set(diag_up  )) in player_list:
            return list(set(diag_up  ))
        
        # win-horizontal
        for row in range(n_row):
            row_values = list(set(self[row]))
            if row_values in player_list:
                return row_values
        
        # win-vertical
        for col in range(n_row):
            col_values = []
            for row in range(n_row):
                col_values.append(self[row][col])
            col_values = list(set(col_values)) # prob shouldn't overwrite
            if col_values in player_list:
                return col_values
        
        # tie (if made it here and board is full, tie, otherwise no winner)
        flat = [item for sublist in self for item in sublist]
        if flat.count(" ") == 0:
            return "Tie"
        else:
            return None
    
    def legal_moves(self):
        """
        find set of valid moves from current game state (i.e. empty cells)
        if game is at a terminal state, return empty list
        """
        if self.winner() is None: # comparisons with None are weird
            moves = []
            for row in range(len(self.board)):
                for col in range(len(self.board)):
                    if self.board[row][col] == " ":
                        moves.append([row, col])
        return moves
    
    def project_move(self, row, col):
        """
        copies the current state and makes the given move
        """
        # assert the move is a valid one
        assert [row, col] in self.legal_moves()
        
        # branch the current state
        game_branch = copy.deepcopy(self)
        
        # apply move to new branch
        game_branch.move(row, col)
        
        return game_branch
    
import unittest


class test_game(unittest.TestCase):
    def test_play(self):
        """
        """

        game = game_state()

        assert str(game) == (" │ │ \n"
                             "─┼─┼─\n"
                             " │ │ \n"
                             "─┼─┼─\n"
                             " │ │ \n")

        assert game.legal_moves() == [(0, 0), (0, 1), (0, 2),
                                      (1, 0), (1, 1), (1, 2),
                                      (2, 0), (2, 1), (2, 2)]

        # Opening game
        game.move(1, 1)  # X
        game.move(0, 2)  # O
        game.move(1, 2)  # X
        game.move(1, 0)  # O
        game.move(2, 1)  # X

        assert str(game) == (" │ │O\n"
                             "─┼─┼─\n"
                             "O│X│X\n"
                             "─┼─┼─\n"
                             " │X│ \n")

        # Keep track of the current game state so we can some alternate end
        # games from this point later
        game_copy1 = copy.deepcopy(game)
        game_copy2 = copy.deepcopy(game)

        # End game #1
        game.move(0, 0)  # O
        game.move(0, 1)  # X plays a winning horizontal line

        assert game.winner() == 'X'

        # End game #2
        game_copy1.move(0, 0)  # O
        game_copy1.move(2, 2)  # X
        game_copy1.move(2, 0)  # O plays a winning vertical line

        assert game_copy1.winner() == 'O'
        assert not game_copy1.legal_moves()

        # End game #3
        game_copy2.move(2, 2)  # O
        game_copy2.move(0, 0)  # X
        game_copy2.move(0, 1)  # O
        game_copy2.move(2, 0)  # X
        assert game_copy2.winner() == 'Tie'
        
        assert str(game) == ("X│O│O\n"
                             "─┼─┼─\n"
                             "O│X│X\n"
                             "─┼─┼─\n"
                             "X│X│O\n")


if __name__ == '__main__':
    unittest.main()
