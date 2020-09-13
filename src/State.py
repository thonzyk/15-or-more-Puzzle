import numpy as np
from src.Board import Board


# TODO: optimize (change state representation to vector)

class State:
    def __init__(self, board: Board = None):
        self.cost: int = 0
        self.heuristic: int = 0
        self.board = board
        self.parent = None
        self.children = []
        self.is_alive = True

    def __str__(self):
        return self.board.to_string() + " cost: " + str(self.cost) + " heuristic: " + str(self.heuristic)

    def to_string(self):
        return self.board.to_string() + " cost: " + str(self.cost) + " heuristic: " + str(self.heuristic)

    def expand(self):
        # MOVE UP
        if self.board.y < self.board.board_map.shape[1] - 1:
            child = self.create_child()
            child.board.move_up()
            child.set_heuristic()
            self.children.append(child)

        # MOVE RIGHT
        if self.board.x < self.board.board_map.shape[0] - 1:
            child = self.create_child()
            child.board.move_right()
            child.set_heuristic()
            self.children.append(child)

        # MOVE DOWN
        if self.board.y > 0:
            child = self.create_child()
            child.board.move_down()
            child.set_heuristic()
            self.children.append(child)

        # MOVE LEFT
        if self.board.x > 0:
            child = self.create_child()
            child.board.move_left()
            child.set_heuristic()
            self.children.append(child)

    def create_child(self) -> 'State':
        child = State()
        child.board = self.board.clone()
        child.cost = self.cost + 1  # TODO: maybe move "+1" somewhere else
        child.parent = self
        child.children = []
        child.is_alive = True
        return child

    def is_finished(self) -> bool:
        # TODO: optimize
        last = -1
        for y in range(self.board.board_map.shape[1] - 1, -1, -1):
            for x in range(self.board.board_map.shape[0]):
                this = self.board.board_map[x, y] if self.board.board_map[x, y] != 0 else 125
                if this < last:
                    return False
                last = this

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

    def set_heuristic(self):
        heuristic = 0
        for y in range(self.board.board_map.shape[1] - 1, -1, -1):
            for x in range(self.board.board_map.shape[0]):
                tile_number = self.board.get_tile(x, y)
                heuristic = heuristic + self.board.get_manhattan_distance(x, y, tile_number)

        self.heuristic = heuristic / 2
        # self.heuristic = 0
