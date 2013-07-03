'''
Created on Jun 30, 2013

@author: fahad
'''
from data_structures.constants import Mark, GameStatus

class Board(object):
    
    def __init__(self):
        self.storage = [[Mark.EMPTY for col in range(3)] for row in range(3)]
        
    def initialize(self):
        '''clears out all cells'''
        self.storage = [[Mark.EMPTY for col in range(3)] for row in range(3)]
        
    def update_board_with_move(self, cell, mark):
        """
        cell is a tuple of (row, col)
        mark is the kind of mark added in that cell
        """
        row, col = cell
        self.storage[row][col] = mark
    
    def set_cell_to_empty(self, cell):
        row, col = cell
        self.storage[row][col] = Mark.EMPTY
    
    def get_empty_cells(self):
        return [(row, col) for row in range(3) for col in range(3) if self.storage[row][col] == Mark.EMPTY]
    
    def is_winner(self, mark):
        """
        Returns True if mark has won
        Else returns False
        """
        # row matching
        for row in self.storage:
            if row[0] == row[1] == row[2] == mark:
                return True
        
        # col matching
        for col in range(3):
            if self.storage[0][col] == self.storage[1][col] == self.storage[2][col] == mark:
                return True
        
        # diagonal matching
        if self.storage[0][0] == self.storage[1][1] == self.storage[2][2] == mark:
            return True
        
        # reverse diagonal matching
        if self.storage[0][2] == self.storage[1][1] == self.storage[2][0] == mark:
            return True
                
        return False
    
    def is_full(self):
        cells = self.get_empty_cells()
        return not cells
    
    def get_board_status(self):
        
        if self.is_winner(Mark.CROSS):
            return GameStatus.CROSS_WON
        
        elif self.is_winner(Mark.NOUGHT):
            return GameStatus.NOUGHT_WON
        
        elif self.is_full():
            return GameStatus.DRAW
        
        else:
            return None
        
    def copy(self):
        b = Board()
        b.storage = []
        for row in self.storage:
            b.storage.append(row[:])
        
        return b    
    
    def display(self):
        for row in range(3):
            line = ''
            for col in range(3):
                if   self.storage[row][col] == Mark.EMPTY:  val = '   '
                elif self.storage[row][col] == Mark.CROSS:  val = ' X '
                elif self.storage[row][col] == Mark.NOUGHT: val = ' O '
                else:
                    print 'Fatal error!'
                    import sys; sys.exit(1)
                
                if col < 2:
                    val += '|'
                
                line = line + val
            
            print line
            if row < 2:
                print '-----------'
        print
        

if __name__ == '__main__':
    b = Board()
    print b.storage
    for i in range(2):
        b.update_board_with_move((0, i), Mark.CROSS)
        b.update_board_with_move((i, 0), Mark.CROSS)
    print b.storage
    print b.get_empty_cells()