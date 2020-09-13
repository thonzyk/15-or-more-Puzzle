import numpy as np
from src.Board import Board
from src.State import State
from src.Generator import random_root
import random
import time
from heapq import heappush, heappop
from src.bfs_lists import CostIndexMap

if __name__ == '__main__':
    halda = []
    slovnik = dict()

    for i in range(10000):
        a = random.randint(-2147483647, 2147483647)
        b = random.randint(-2147483647, 2147483647)
        slovnik[a] = b

    start = time.time()
    for i in range(10000):
        c = 1234 in slovnik
        pass

    end = time.time()
    print(end - start)
    pass
