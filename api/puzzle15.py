import numpy as np
import time
from tqdm import tqdm


def format_time_diff(time_diff):
    # Convert the time difference to hours, minutes, seconds and milliseconds
    hours, rem = divmod(time_diff, 3600)
    minutes, seconds = divmod(rem, 60)
    seconds, milliseconds = divmod(seconds, 1)
    milliseconds = round(milliseconds * 1000)

    # Return time difference in "HH:MM:SS:MS" format
    return "{:0>2}:{:0>2}:{:0>2}:{:0>3}".format(int(hours), int(minutes), int(seconds), int(milliseconds))


class Puzzle15:
    def __init__(self, height=4, width=4):
        assert type(height) == int and height > 0
        assert type(width) == int and width > 0
        assert height * width <= 256

        # Generate random board
        self.board = np.arange(height * width).astype('int8')
        # Reshape to 2D
        self.board = self.board.reshape((height, width))

        # Define win state
        self.win_board = np.copy(self.board)

        # Define action operations
        self.action_map = {
            0: np.array((-1, 0), dtype='int8'),  # up (↑)
            1: np.array((0, 1), dtype='int8'),  # right (→)
            2: np.array((1, 0), dtype='int8'),  # down (↓)
            3: np.array((0, -1), dtype='int8')  # left (←)
        }

        # Initialize supportive variables
        self.zero_coord = np.array((0, 0), dtype='int8')
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                if self.board[i, j] == 0:
                    self.zero_coord = (i, j)

        # Shuffle the board
        self.shuffle_the_board()

        # Initialize start time
        self.start_time = time.time()
        # Initialize # moves
        self.n_moves = 0

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
            exit('Game Over - Invalid Move!')

        # Perform change of the state
        move_num_coord = tuple(self.zero_coord + self.action_map[move_number])
        move_num = self.board[move_num_coord]
        self.board[tuple(self.zero_coord)] = move_num
        self.board[move_num_coord] = 0
        self.zero_coord += self.action_map[move_number]

        if not self.shuffling:
            self.check_win()

    def check_win(self):
        self.n_moves += 1

        if np.all(self.board == self.win_board):
            finish_time = time.time()
            elapsed_time = format_time_diff(finish_time - self.start_time)
            exit(f'\nGame Completed!\nNumber of moves: {self.n_moves}\nTime: {elapsed_time}')

    def shuffle_the_board(self):
        self.shuffling = True
        all_moves = np.arange(4)
        for i in range(10_000):
            possible_moves = all_moves[self.get_possible_actions()]
            random_move = np.random.choice(possible_moves)
            self.move(random_move)
        self.shuffling = False


if __name__ == '__main__':
    # Demo script: random solver
    b = Puzzle15(3, 3)

    all_moves = np.arange(4)

    pbar = tqdm()

    print('Trying to solve the puzzle by random moves...')
    while True:
        possible_moves = all_moves[b.get_possible_actions()]
        random_move = np.random.choice(possible_moves)
        b.move(random_move)
        # tqdm.write("Processing...")
        pbar.update(1)
