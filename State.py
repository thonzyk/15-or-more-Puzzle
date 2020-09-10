import numpy as np

class State:
    def __init__(self, board=None):
        self.cost = 0
        self.heuristic = 0
        self.board = board
        self.parent = None
        self.children = []

    def expand(self):
        # MOVE UP
        if self.board.y < self.board.board_map.shape[1] - 1:
            child = self.create_child()
            child.board.move_up()
            self.children.append(child)

        # MOVE RIGHT
        if self.board.x < self.board.board_map.shape[0] - 1:
            child = self.create_child()
            child.board.move_right()
            self.children.append(child)

        # MOVE DOWN
        if self.board.y > 0:
            child = self.create_child()
            child.board.move_down()
            self.children.append(child)

        # MOVE LEFT
        if self.board.x > 0:
            child = self.create_child()
            child.board.move_left()
            self.children.append(child)

    def create_child(self) -> 'State':
        child = State()
        child.board = self.board.clone()
        child.cost = self.cost + 1  # TODO: maybe move "+1" somewhere else
        child.parent = self
        child.children = []
        return child

    def is_finished(self) -> bool:
        # TODO: optimize
        last = -1
        for y in range(self.board.board_map.shape[1] - 1, -1, -1):
            for x in range(self.board.board_map.shape[0]):
                if self.board.board_map[x, y] < last:
                    return False
                last = self.board.board_map[x, y]

        return True

    def equals(self, another_state: 'State', include_cost: bool):
        if not self.board.equals(another_state.board):
            return False

        if include_cost:
            return self.cost == another_state.cost
        else:
            return True

    def get_complete_cost(self):
        return self.cost + self.heuristic