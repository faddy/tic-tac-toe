'''
Created on Jun 30, 2013

@author: fahad
'''
import random
from data_structures.board import Board
from data_structures.constants import Mark
from utils.minimax import minimax


class Player(object):

    def __init__(self, m):
        self.mark = m
        self.opp_mark = (Mark.ALL - set([m, Mark.NOUGHT])).pop()
    
    def get_next_move(self, board):
        """Subclasses implement this method"""
        pass
    
    
class UserPlayer(Player):
    
    def get_next_move(self, board):
        valid_cells = board.get_empty_cells()
        correct_input = False
        
        print 'Your move!'
        while not correct_input:
            row_col = raw_input('Enter row and col separated by a space (e.g. 1 2): ')
            row_col = row_col.strip()
            
            try:
                if not row_col:   # user entered nothing or empty string or spaces
                    raise
                
                else:
                    row, col = [int(x) for x in row_col.split()] # raises exception when input is not int
                    if row not in [0, 1, 2] or col not in [0, 1, 2]:
                        raise
            
            except:
                print 'Incorrect or no values provided'
            
            else:
                if (row, col) not in valid_cells:
                    print 'This cell is already taken'
                else:
                    correct_input = True
            
        return (row, col)
    
    
class ComputerPlayer(Player):
    
    def get_next_move(self, board):
        pass


class RandomComputerPlayer(ComputerPlayer):
    """
    Chooses the next move at random (useless)
    """
    def get_next_move(self, board):
        print 'My Move! ...'
        valid_cells = board.get_empty_cells()   # tuples of available positions to move to
        return random.choice(valid_cells)
    
    
class SmartComputerPlayer(ComputerPlayer):
    """
    Detects if the user is about to win, and tries to block his move
    """
    
    def get_next_move(self, board):
        print 'My Move!'
        valid_cells = board.get_empty_cells()
    
        # find out if forced move (opponent wins in one move)
        forced_moves = []
        opponent_mark = (Mark.ALL - set([Mark.EMPTY, self.mark])).pop()
        for cell in valid_cells:
            board.update_board_with_move(cell, opponent_mark)
            opponent_wins = board.is_winner(opponent_mark)
            board.set_cell_to_empty(cell)
            if opponent_wins:
                forced_moves.append(cell)
                
        
        if forced_moves:
            return forced_moves[0]
        else:
            return random.choice(valid_cells)
        
    
class SmarterComputerPlayer(ComputerPlayer):
    """
    Searches minimax game tree upto 3 levels only
    """
    def get_next_move(self, board):
        val, best_move = minimax(3, board, self.mark)
        return best_move


class EvenSmarterComputerPlayer(ComputerPlayer):
    """
    Not as slow as I thought it could be.
    """
    def get_next_move(self, board):
        val, best_move = minimax(7, board, self.mark)
        return best_move


if __name__ == '__main__':
    u = SmarterComputerPlayer('X')
    print u.get_next_move(Board())
    