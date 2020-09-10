import numpy as np

class Board:
    def __init__(self, board_map, x, y):
        """
        :param board_map: all tiles in 2D numpy-array
        :param x: x-coordinate of empty tile (0)
        :param y: y-coordinate of empty tile (0)
        """
        self.board_map = board_map
        self.x = np.int8(x)
        self.y = np.int8(y)

    def move_up(self):
        self.y = self.y + 1
        self.board_map[self.x, self.y - 1] = self.board_map[self.x, self.y]
        self.board_map[self.x, self.y] = 0

    def move_right(self):
        self.x = self.x + 1
        self.board_map[self.x - 1, self.y] = self.board_map[self.x, self.y]
        self.board_map[self.x, self.y] = 0

    def move_down(self):
        self.y = self.y - 1
        self.board_map[self.x, self.y + 1] = self.board_map[self.x, self.y]
        self.board_map[self.x, self.y] = 0

    def move_left(self):
        self.x = self.x - 1
        self.board_map[self.x + 1, self.y] = self.board_map[self.x, self.y]
        self.board_map[self.x, self.y] = 0

    def to_string(self):
        result = "###"
        for i in range(self.board_map.shape[0]):
            result = result + "##"

        result = result + "\n"

        for y in range(self.board_map.shape[1]-1, -1, -1):
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
