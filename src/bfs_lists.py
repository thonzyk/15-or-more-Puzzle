from src.State import State
from heapq import heappush, heappop
import numpy as np


class BfsCollection:
    def __init__(self):
        self.STATE_LIST: list = []
        self.INDEX_DICT: dict = dict()
        self.COST_HEAP: list = []
        self.OPEN_size = 0

    def __str__(self):
        result = "OPEN:\n"

        for item in self.OPEN:
            result = result + item.to_string()

        result = result + "CLOSED:\n"

        for item in self.CLOSED:
            result = result + item.to_string() + "\n\n"

        return result

    def poll(self) -> State:
        """
        Returns the open state with smallest total cost and mark it as closed.
        :return:
        """
        best_state = self.find_best_state()
        best_state.is_closed = True
        self.OPEN_size = self.OPEN_size - 1
        return best_state

    def push(self, state: State):
        """
        If similar state doesn't exist, appends to the list
        If similar, but with same or lower cost state exists, discard the push-state
        If similar state with higher cost exists, remove original state and its subtree and append to the list
        :param state: state to push
        """

        if state.get_hash() in self.INDEX_DICT:
            index = self.INDEX_DICT[state.get_hash()]
            alternative_state = self.STATE_LIST[index]
            if state.get_complete_cost() < alternative_state.get_complete_cost():
                self.remove_subtree(alternative_state)
                self.append(state)
            else:
                return

        self.append(state)

    def append(self, state: State):
        self.STATE_LIST.append(state)
        index = len(self.STATE_LIST) - 1
        self.INDEX_DICT[state.get_hash()] = index
        cost_index_map = CostIndexMap(state.cost, index)
        heappush(self.COST_HEAP, cost_index_map)
        self.OPEN_size = self.OPEN_size + 1

    def get_state_alternative(self, state: State):
        """
        Returns same state (without counting cost) from the list
        :param state_hash:
        :return:
        """
        index = self.INDEX_DICT[state.get_hash()]
        return self.STATE_LIST[index]

    def find_index_of_state(self, state: State):
        """
        Returns index of the state in the STATE_LIST or returns -1 if the state is not present
        :param state:
        :return:
        """
        pass

    def remove_subtree(self, root: State):
        """
        Removes the root and its subtree by recursion.
        """
        self.remove(root)
        for child in root.children:
            self.remove_subtree(child)

    def remove(self, state: State):
        state.is_alive = False

    def clear_lists(self):
        self.OPEN = [state for state in self.OPEN if state.is_alive]
        self.CLOSED = [state for state in self.CLOSED if state.is_alive]

    def find_best_state(self) -> State:
        index = heappop(self.COST_HEAP).index
        state: State = self.STATE_LIST[index]
        while not state.is_alive:  # TODO: optimize
            index = heappop(self.COST_HEAP).index
            state = self.STATE_LIST[index]

        return state

    def get_open_size(self):
        return self.OPEN_size

class CostIndexMap:
    def __init__(self, cost=-1, index=-1):
        self.cost = cost
        self.index = index

    def __lt__(self, other: 'CostIndexMap'):
        return self.cost < other.cost
