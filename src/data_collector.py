from Generator import random_root
from Search import Search

CSV_PATH = "D:\\ML-Data\\15-Puzzle\\data.csv"

if __name__ == '__main__':
    root = random_root((4, 4))
    search = Search("fast")
    solution = search.findSolution(root)
    data = str(solution)
    with open(CSV_PATH, 'a') as fd:
        fd.write(data)
