import cards
from pynput import keyboard

from board import Board

class Game:
    def __init__(self):
        self.board = Board(3,3)
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
    
    def on_press(self, key):
        if key == keyboard.Key.up:
            self.board.move_agent("up")
        if key == keyboard.Key.down:
            self.board.move_agent("down")
        if key == keyboard.Key.left:
            self.board.move_agent("left")
        if key == keyboard.Key.right:
            self.board.move_agent("right")
        self.print_board()
        
    def print_board(self):
        print('\n')
        agent = self.board.board[self.board.agent_position[1]][self.board.agent_position[0]]
        print("{:^10}{:^10}{:^10}".format('hp', 'gold',  'weapon'))
        print("{:^10}{:^10}{:^10}- {}".format(agent.hp, agent.gold, str(agent.weapon), agent.weapon.damage if agent.weapon else ''))
        print('-'*34)
        for row in self.board.board:
            line1 = "|"
            line2 = "|"
            for elem in row:
                line1 += "{:^10}|".format(str(elem))
                line2 += "{:^10}|".format(elem.hp if isinstance(elem, (cards.Monster, cards. Elixir)) else 
                                                        (elem.damage if isinstance(elem, cards.Sword) else 
                                                        (elem.value if isinstance(elem, cards.Gold) else "")))
                                            
            print(line1)
            print(line2)
            print('-'*34)
        print('\n')