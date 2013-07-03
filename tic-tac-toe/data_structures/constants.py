'''
Created on Jun 30, 2013

@author: fahad
'''

class Mark(object):
    EMPTY, CROSS, NOUGHT = range(0,3)
    ALL = set([EMPTY, CROSS, NOUGHT])
    
class GameStatus(object):
    STARTING, PLAYING, DRAW, CROSS_WON, NOUGHT_WON, END = range(0,6)
