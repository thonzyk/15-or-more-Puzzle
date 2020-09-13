from src.DumbAssLists import DumbAssLists
from src.State import State
from src.bfs_lists import BfsCollection


class Search:
    def __init__(self, mode: str):
        if mode == "fast":
            self.lists = BfsCollection()
        elif mode == "slow":
            self.lists = DumbAssLists()
        self.iterations_count: int = 0

    def findSolution(self, root: State, seed=None):
        # Initialization

        self.iterations_count: int = 0

        self.lists.push(root)

        # Search algorithm
        while self.lists.get_open_size() > 0:
            self.iterations_count = self.iterations_count + 1
            node = self.lists.poll()

            if node.is_finished():
                return self.get_solve_sequence(node)

            node.expand()
            for child in node.children:
                self.lists.push(child)

        print("Solution was not found.")
        return []

    def get_solve_sequence(self, finish_node: State):
        solution = []

        node = finish_node
        while node.parent is not None:
            solution.append(node)
            node = node.parent

        solution.append(node)

        solution.reverse()
        return solution

    def to_string(self):
        print('Search---')
