import numpy as np


class Puzzle15:
    def __init__(self, height=4, width=4):
        assert type(height) == int and height > 0
        assert type(width) == int and width > 0
        assert height * width <= 256

        # Generate random board
        self.board = np.arange(height * width).astype('int8')

        # Shuffle the board
        self.board = self.board[np.random.permutation(len(self.board))]

        # Reshape to 2D
        self.board = self.board.reshape((height, width))

        # Initialize # moves
        self.moves = 0

        # Initialize supportive variables
        self.zero_coord = (0, 0)
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                if self.board[i, j] == 0:
                    self.zero_coord = (i, j)

    def get_state(self):
        return np.copy(self.board)

    def get_possible_actions(self):
        """
        0: move zero up (↑)
        1: move zero right (→)
        2: move zero down (↓)
        3: move zero left (←)
        """
        return np.array((self.zero_coord[0] > 0, self.zero_coord[1] < self.board.shape[1] - 1,
                         self.zero_coord[0] < self.board.shape[0] - 1, self.zero_coord[1] > 0))

    def move(self, move_number):
        """
        0: move zero up (↑)
        1: move zero right (→)
        2: move zero down (↓)
        3: move zero left (←)
        """
        possible_actions = self.get_possible_actions()
        if not possible_actions[move_number]:
            assert False, 'Invalid Move - Game Over'

        # TODO: implement the change of the state


if __name__ == '__main__':
    b = Puzzle15()
