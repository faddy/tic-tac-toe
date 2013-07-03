'''
Created on Jul 2, 2013

@author: fahad
'''
from data_structures.constants import Mark
from data_structures.board import Board

def minimax(depth, board, mark):
    
    # we have reached max depth, without finding any result, return IDK
    if depth <= 0:
        return (1, None)
    
    status = decide_board(board, mark)
    
    # if the game has ended at this board, return its value
    if status != 1:
        return (status, None)
    
    all_moves = board.get_empty_cells()
    best_move = None
    
    if mark == Mark.CROSS:
        # Computer's turn, calcuate max
        best_score = -10
        for move in all_moves:
            board.update_board_with_move(move, mark)
            val, x = minimax(depth-1, board, Mark.NOUGHT)
            board.set_cell_to_empty(move)
            if val > best_score:
                best_score = val
                best_move = move
    
    else:
        # User's turn, calculate min
        best_score = 10
        for move in all_moves:
            board.update_board_with_move(move, mark)
            val, x = minimax(depth-1, board, Mark.CROSS)
            board.set_cell_to_empty(move)
            if val < best_score:
                best_score = val
                best_move = move
                
    return (best_score, best_move)
            

def decide_board(board, player):
    """
    Returns:-
     2: if computer wins
     0: if draw
    -1: if user wins
     1: if the game has not ended yet
    """
    if board.is_winner(Mark.CROSS):     # computer wins
        return 2
    
    elif board.is_winner(Mark.NOUGHT):  # user wins
        return -1
    
    elif board.is_full():               # draw
        return 0
    
    else:
        return 1                        # can't determine
    
    
    
def test1():
    b = Board()
    b.update_board_with_move((0,0), Mark.CROSS)
    b.update_board_with_move((0,1), Mark.CROSS)
    b.update_board_with_move((1,0), Mark.CROSS)
    b.update_board_with_move((1,1), Mark.NOUGHT)
    b.update_board_with_move((1,2), Mark.NOUGHT)
    b.update_board_with_move((2,0), Mark.NOUGHT)
    b.display()
    
    v, n = minimax(3, b, Mark.CROSS)
    print v
    print n
    
def test2():
    b = Board()
    b.update_board_with_move((0,0), Mark.NOUGHT)
    b.update_board_with_move((0,1), Mark.NOUGHT)
    b.update_board_with_move((1,1), Mark.CROSS)
    b.update_board_with_move((2,1), Mark.NOUGHT)
    b.update_board_with_move((2,2), Mark.CROSS)
    b.display()
    
    v, n = minimax(3, b, Mark.CROSS)
    print v
    print n
    
if __name__ == '__main__':
    test1()
    
