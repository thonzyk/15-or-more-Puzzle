from DumbAssLists import DumbAssLists
from State import State
from bfs_lists import BfsCollection
from solution import Solution


class Search:
    def __init__(self, mode: str):
        if mode == "fast":
            self.lists = BfsCollection()
        elif mode == "slow":
            self.lists = DumbAssLists()
        self.iterations_count: int = 0

    def findSolution(self, root: State, seed=None) -> Solution:
        # Initialization

        self.iterations_count: int = 0
        root.set_heuristic()
        self.lists.push(root)

        # Search algorithm
        while self.lists.get_open_size() > 0:
            self.iterations_count = self.iterations_count + 1
            node = self.lists.poll()

            if node.is_finished():
                return self.get_solution(node)

            node.expand()
            for child in node.children:
                self.lists.push(child)

        print("Solution was not found.")
        return []

    def get_solution(self, finish_node: State) -> Solution:
        solution = Solution()
        solution.state_sequence = self.get_state_sequence(finish_node)
        solution.action_sequence = self.get_action_sequence(solution.state_sequence)
        solution
        return solution

    def get_action_sequence(self, state_sequence):
        action_sequence = []
        last_state = state_sequence[0]
        for state in state_sequence:
            if last_state is not None:
                action_sequence.append(last_state.get_transition(state))
            last_state = state

        return action_sequence

    def get_state_sequence(self, finish_node: State):
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
