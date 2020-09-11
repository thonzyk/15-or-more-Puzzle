from src.Generator import random_root
from src.DumbAssLists import DumbAssLists
from src.State import State


class Search:

    def findSolution(self, root: State, seed=None):
        # Initialization
        lists = DumbAssLists()
        lists.push_open(root)

        # Search algorithm
        while len(lists.OPEN) > 0:
            node = lists.poll()

            if node.is_finished():
                return self.get_solve_sequence(node)

            node.expand()
            for child in node.children:
                lists.push_open(child)

        print("Solution was not found.")

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
