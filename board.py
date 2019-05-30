import sys
from random import choice
from cards import Agent, Monster, Elixir, Gold, Sword

AVAILABLE_CARDS = [Monster,Monster, Elixir, Gold, Sword]


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = BoardGenerator().generate_board(width, height)
        self.agent_position = [int(width/2), int(height/2)]
        print(self.board)

    def move_agent(self, direction):
        if not self.__is_available_move(direction):
            return 
        card_position = {
            "up": lambda x: [x[0], x[1]-1],
            "down": lambda x: [x[0], x[1]+1],
            "left": lambda x: [x[0]-1, x[1]],
            "right": lambda x: [x[0]+1, x[1]],
        }[direction](self.agent_position)
        agent = self.board[self.agent_position[1]][self.agent_position[0]]
        cards = self.board[card_position[1]][card_position[0]].interaction(agent)
        if cards[1] is None:
            print("You died")
            sys.exit()

        elif cards[0] is None:
            self.board[card_position[1]][card_position[0]] = cards[1]
            self.board[self.agent_position[1]][self.agent_position[0]] = choice(AVAILABLE_CARDS)()
            self.agent_position = card_position

        else:
            self.board[card_position[1]][card_position[0]] = cards[0]
            self.board[self.agent_position[1]][self.agent_position[0]] = cards[1]
        
        

    def __is_available_move(self, direction):
        dir_conditions = {
            "up": self.agent_position[1] > 0,
            "down": self.agent_position[1] < self.height,
            "left": self.agent_position[0] > 0,
            "right": self.agent_position[0] < self.width
        }
        return dir_conditions[direction]


class BoardGenerator:
    def generate_board(self, width, height):
        board = []
        for i in range(height):
            board.append([choice(AVAILABLE_CARDS)() for j in range(width)])
        board[int(height/2)][int(width/2)] = Agent()
        return board
            

