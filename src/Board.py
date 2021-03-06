import numpy as np
from math import ceil

class Board:
    def __init__(self, board_map, x, y):
        """
        :param board_map: all tiles in 2D numpy-array
        :param x: x-coordinate of empty tile (0)
        :param y: y-coordinate of empty tile (0)
        """
        self.board_map = board_map
        self.x: np.int8 = np.int8(x)
        self.y: np.int8 = np.int8(y)

    def move_up(self):
        self.y = np.int8(self.y + 1)
        self.board_map[self.x, self.y - 1] = self.board_map[self.x, self.y]
        self.board_map[self.x, self.y] = 0

    def move_right(self):
        self.x = np.int8(self.x + 1)
        self.board_map[self.x - 1, self.y] = self.board_map[self.x, self.y]
        self.board_map[self.x, self.y] = 0

    def move_down(self):
        self.y = np.int8(self.y - 1)
        self.board_map[self.x, self.y + 1] = self.board_map[self.x, self.y]
        self.board_map[self.x, self.y] = 0

    def move_left(self):
        self.x = np.int8(self.x - 1)
        self.board_map[self.x + 1, self.y] = self.board_map[self.x, self.y]
        self.board_map[self.x, self.y] = 0

    def to_string(self):
        result = "###"
        for i in range(self.board_map.shape[0]):
            result = result + "##"

        result = result + "\n"

        for y in range(self.board_map.shape[1] - 1, -1, -1):
            result = result + "#"
            for x in range(self.board_map.shape[0]):
                if self.board_map[x, y] != 0:
                    result = result + " " + str(self.board_map[x, y])
                else:
                    result = result + "  "
            result = result + " #\n"

        result = result + "###"
        for i in range(self.board_map.shape[0]):
            result = result + "##"

        return result

    def find_empty_tile(self):
        for y in range(self.board_map.shape[1] - 1, -1, -1):
            for x in range(self.board_map.shape[0]):
                if self.board_map[x, y] == 0:
                    self.x = np.int8(x)
                    self.y = np.int8(y)

    def equals(self, another_board):
        return np.array_equal(self.board_map, another_board.board_map)

    def clone(self):
        clone = Board(self.board_map.copy(), self.x, self.y)
        return clone

    def is_solvable(self):
        if self.board_map.shape[0] != self.board_map.shape[1]:
            print("Not implemented for N*M yet.")
            return True

        inversions_count = 0
        board_array = self.board_to_array()
        for i in range(len(board_array)):
            for j in range(i, len(board_array)):
                if board_array[i] > board_array[j] and board_array[j] != 0 and board_array[i] != 0:
                    inversions_count = inversions_count + 1

        if self.board_map.shape[0] % 2 == 0:  # EVEN N*N
            self.find_empty_tile()
            row_number = self.y + 1
            if row_number % 2 == 1:  # ODD
                return inversions_count % 2 == 0
            else:  # EVEN
                return inversions_count % 2 == 1
        else:  # ODD N*N
            return inversions_count % 2 == 0


    def board_to_array(self):
        board_array = []
        for y in range(self.board_map.shape[1] - 1, -1, -1):
            for x in range(self.board_map.shape[0]):
                board_array.append(self.board_map[x, y])

        return board_array

    def get_manhattan_distance(self, x, y, tile_number) -> np.int8:
        """
        Returns Manhattan distance of the tile with coordinates [x, y] from its right location
        :param tile_number:
        :param x:
        :param y:
        :return:
        """
        right_x, right_y = self.get_coordinates_of_number(tile_number)
        return abs(x - right_x) + abs(y - right_y)

    def get_coordinates_of_number(self, number) -> (np.int8, np.int8):
        if number == 0:
            x = np.int8(self.board_map.shape[0] - 1)
            y = np.int8(0)
        else:
            x = np.int8(((number - 1) % self.board_map.shape[0]))
            y = np.int8(self.board_map.shape[1] - 1 - np.int8(((number - 1) / self.board_map.shape[0])))

        return x, y

    def get_tile(self, x, y) -> np.int8:
        return self.board_map[x, y]
