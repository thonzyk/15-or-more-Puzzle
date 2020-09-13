import numpy as np
from src.Board import Board
from src.State import State

def random_board(board_shape, seed=None):
    number_of_tiles = board_shape[0] * board_shape[1]
    board_map = np.array(range(number_of_tiles))
    np.random.shuffle(board_map)
    board_map = board_map.reshape(board_shape)
    board = Board(board_map, 0, 0)
    board.find_empty_tile()
    return board

def random_root(board_shape):
    board = random_board(board_shape)
    while not board.is_solvable():
        board = random_board(board_shape)
    root = State(board)
    return root

def explicit_root_1():
    board_map = np.array([1, 0, 3, 2])
    board_map = board_map.reshape((2, 2))
    board = Board(board_map, 0, 0)
    board.find_empty_tile()
    root = State(board)
    return root

def explicit_root_2():
    board_map = np.array([3, 1, 5, 4, 0, 2])
    board_map = board_map.reshape((2, 3))
    board = Board(board_map, 0, 0)
    board.find_empty_tile()
    root = State(board)
    return root


def explicit_root_3():
    board_map = np.array([1, 3, 0, 8, 4, 6, 5, 2, 7])
    board_map = board_map.reshape((3, 3))
    board = Board(board_map, 0, 0)
    board.find_empty_tile()
    root = State(board)
    return root

