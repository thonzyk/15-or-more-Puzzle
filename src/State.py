import numpy as np
from Board import Board

MIN_LONG_VALUE = -np.int64((2 ** 63) - 1)
MAX_LONG_VALUE = np.int64((2 ** 63) - 1)

# TODO: optimize (change state representation to vector)

class State:
    def __init__(self, board: Board = None):
        self.cost: np.int8 = np.int8(0)
        self.heuristic: np.int8 = np.int8(0)
        self.board = board
        self.parent = None
        self.children = []
        # self.is_alive = True
        # self.is_closed = False

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
        child.cost = self.cost + np.int8(1)  # TODO: maybe move "+1" somewhere else
        child.parent = self
        child.children = []
        # child.is_alive = True
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

    def get_complete_cost(self) -> np.int8:
        return self.cost + self.heuristic

    def set_heuristic(self):
        heuristic = np.int8(0)
        for y in range(self.board.board_map.shape[1] - 1, -1, -1):
            for x in range(self.board.board_map.shape[0]):
                tile_number = np.int8(self.board.get_tile(x, y))
                if tile_number == 0:
                    continue
                heuristic = heuristic + self.board.get_manhattan_distance(np.int8(x), np.int8(y), tile_number)

        self.heuristic = heuristic
        # self.heuristic = 0

    def get_hash(self) -> np.int64:
        index = 0
        hash_value = MIN_LONG_VALUE
        for y in range(self.board.board_map.shape[1] - 1, -1, -1):
            for x in range(self.board.board_map.shape[0]):
                if index >= self.board.board_map.size - 1:
                    continue
                tile = np.int64(self.board.board_map[x, y])
                hash_value = hash_value + (tile * np.int64(16**index))
                index = index + 1

        return hash_value

    def get_transition(self, next_state: 'State') -> str:
        if self.board.y < next_state.board.y:
            return "UP"
        if self.board.x < next_state.board.x:
            return "RIGHT"
        if self.board.y > next_state.board.y:
            return "DOWN"
        if self.board.x > next_state.board.x:
            return "LEFT"

        return "NONE"
