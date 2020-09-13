from jproperties import Properties
from src.Search import Search
from src.Generator import explicit_root
from src.Generator import random_root
import time

if __name__ == '__main__':
    p = Properties()
    with open("config.properties", "rb") as f:
        p.load(f, "utf-8")

    # root = explicit_root()
    root = random_root((2, 2))
    search = Search()

    start = time.time()
    solution = search.findSolution(root)
    end = time.time()

    for state in solution:
        print(state.board.to_string())

    print("Compute time: " + str(end-start) + " seconds")



