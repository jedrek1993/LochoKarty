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
        print("hp  gold  weapon")
        print(agent.hp,"  ", agent.gold, ' ', agent.weapon,'-',  agent.weapon.damage if agent.weapon else '')
        for row in self.board.board:
            print(row)
        print('\n')