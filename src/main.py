from jproperties import Properties
from src.Search import Search
from src.Generator import explicit_root_1, explicit_root_2, explicit_root_3
from src.Generator import explicit_root_2
from src.Generator import random_root
import time

if __name__ == '__main__':
    p = Properties()
    with open("config.properties", "rb") as f:
        p.load(f, "utf-8")

    root = explicit_root_3()
    # root = random_root((3, 3))
    search = Search("slow")

    start = time.time()
    solution = search.findSolution(root)
    end = time.time()

    for state in solution:
        print(state.board.to_string())

    print("Compute time: " + str(end-start) + " seconds")
    print("iterations: " + str(search.iterations_count))

    root = explicit_root_3()
    # root = random_root((3, 3))
    search = Search("slow")

    start = time.time()
    solution = search.findSolution(root)
    end = time.time()

    print("Compute time: " + str(end - start) + " seconds")
    print("iterations: " + str(search.iterations_count))









