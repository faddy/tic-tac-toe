'''
Created on Jun 30, 2013

@author: fahad
'''
import random
from data_structures import board, players
from data_structures.constants import Mark, GameStatus

LEVELS = {1: (players.RandomComputerPlayer, 'The dumb one'),
          2: (players.SmartComputerPlayer, 'I am going to obstruct your moves'),
          3: (players.SmarterComputerPlayer, 'I like to win')}


class TicTacToe(object):
    
    def __init__(self):
        self.game_status = GameStatus.STARTING
        self.board = board.Board()
        self.turn_of_player = None
        
        while self.game_status != GameStatus.END:
            self.new_game()
            self.game_status = self.continue_or_end()
      
    def new_game(self):
        self.board.initialize()
        self.game_status = GameStatus.PLAYING
        
        # user always gets nought and computer always gets cross
        user = players.UserPlayer(Mark.NOUGHT)
        computer = self.get_computer_player(Mark.CROSS)

        # randomize who gets to go first
        players_list = [user, computer]
        random.shuffle(players_list)
        
        self.start(players_list[0], players_list[1])
    
    
    def start(self, player1, player2):
        
        print 'Starting a new game...\n'
        
        current_player = player1
        
        while True:
            self.display_board()
            
            cell = current_player.get_next_move(self.board)
            self.update_move_on_board(cell, current_player.mark)
            self.update_game_state_with_mark(current_player.mark)
            
            if self.game_status in [GameStatus.CROSS_WON, GameStatus.NOUGHT_WON]:
                self.declare_winner(current_player)
                break
            
            if self.game_status == GameStatus.DRAW:
                self.declare_draw()
                break
                
            if current_player == player1:
                current_player = player2
            else:
                current_player = player1
            
    def get_computer_player(self, mark):
        print 'Which computer do you want to play against?'
        for level in sorted(LEVELS.keys()):
            print '  {0}: {1}'.format(level, LEVELS[level][1])
                
        while True:
            choice = raw_input('Enter choice here: ')
            try:
                choice = int(choice.strip())
                if not 0 < choice < 4:
                    raise
                break
            except:
                print "That level doesn't exist yet."
        
        player_class = LEVELS[choice][0]
        return player_class(mark)
        
            
    def display_board(self):
        print 'Board Status:'
        self.board.display()
        print    

    def declare_draw(self):
        self.display_board()
        print 'Alas... we have reached a draw :('
    
    def declare_winner(self, winner):
        self.display_board()        
        print '{0} have won this game!'.format('You' if isinstance(winner, players.UserPlayer) else 'I')
                
    
    def update_game_state_with_mark(self, mark):
            
        if self.board.is_winner(mark):
            if mark == Mark.CROSS:
                self.game_status = GameStatus.CROSS_WON
        
            else:
                self.game_status = GameStatus.NOUGHT_WON
                
        elif self.board.is_full():
            self.game_status = GameStatus.DRAW
        
    
    def update_move_on_board(self, cell, mark):
        self.board.update_board_with_move(cell, mark)
    
    
    def continue_or_end(self):
        while True:
            play_more = raw_input('Do you want to play a new game? (Enter Y/N): ')
            try:
                play_more = play_more.strip().lower()
                if play_more not in ['y', 'n']:
                    raise Exception()
            except:
                print 'Invalid choice'
            else:
                return GameStatus.STARTING if play_more == 'y' else GameStatus.END
        
    
if __name__ == '__main__':
    try:
        t = TicTacToe()
    except KeyboardInterrupt:
        print '\nExiting the game...'
        exit (1)
    