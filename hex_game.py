#! /usr/bin/python
from cached_property import cached_property

X = 'x'
O = 'o'


class Board(object):
    def __init__(self, board=None, height=3, width=3):
        if board:
            # TODO Automate!
            self.has_winning_strategy = board.has_winning_strategy
            self.active_player = board.active_player
            # Deep copy
            self.state = [[cell for cell in row] for row in board.state]
            self.height = board.height
            self.width = board.width
        else:
            self.height = height
            self.width = width
            self.active_player = X
            self.state = [[None for y in range(self.height)] for x in range(self.width)]

    has_winning_strategy = None

    @classmethod
    def other_player(cls, player):
        return X if player == O else O

    def copy(self):
        return Board(self)

    def make_move(self, x, y):
        if self.state[y][x]:
            raise Exception('Invalid move')

        self.state[y][x] = self.active_player
        self.active_player = self.other_player(self.active_player)

    @cached_property
    def winner(self):
        pass

    @cached_property
    def hash(self):
        return self.__str__

    def legal_moves(self):
        for y, row in enumerate(self.state):
            for x, cell in enumerate(row):
                if not cell:
                    yield x, y

    @cached_property
    def __str__(self):
        string = ''
        for row_number, row in enumerate(self.state):
            string += ' ' * row_number
            for cell_value in row:
                string += (cell_value or '_') + ' '
            string += '\n'
        return string

if __name__ == "__main__":
    empty_board = Board()
    pass

'''
determine_winning_strategy(board)
    if (winning_strategies_list[board.hash]) return that
    if (board.winner()) return that
    for x, y in board.legal_moves():
        if (determine_winning_strategy(board with new move) == active)
            winning_strategies_list[board.hash] = active
            return active

    winning_strategies_list[board.hash] = !active
    return !active
'''
