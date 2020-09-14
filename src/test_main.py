import numpy as np
from Board import Board
from State import State
from Generator import random_root
import random
import time
from heapq import heappush, heappop
from bfs_lists import CostIndexMap
import pandas as pd


CSV_PATH = "D:\\ML-Data\\15-Puzzle\\data.csv"

if __name__ == '__main__':
    # data = pd.read_csv(CSV_PATH, header=0, delimiter=';')


    print(16**16)
    print(2**64)
    print(np.int64(((2**63)) - 1))
    pass
