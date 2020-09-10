from src.State import State


class DumbAssLists:
    def __init__(self):
        self.OPEN = []
        self.CLOSED = []

    def poll(self) -> State:
        favorite: State = None

        for state in self.OPEN:
            if favorite is None or state.cost < favorite.cost:
                favorite = state

        self.OPEN = [list_state for list_state in self.OPEN if not favorite.equals(list_state, True)]
        return favorite

    def insert(self, state: State):
        self.OPEN.append(state)

    def push_closed(self, state: State):
        self.CLOSED.append(state)

    def push_open(self, state: State):
        """
        If similar state doesn't exist, appends to the list
        If similar, but with same or lower cost state exists, discard the push-state
        If similar state with higher cost exists, remove original state and its subtree and append to the list
        :param state: state to push
        """

        for list_state in self.OPEN:
            if state.equals(list_state, False):
                if state.get_complete_cost() < list_state.get_complete_cost():
                    self.remove_subtree(list_state, self.OPEN)
                    self.OPEN.append(state)
                else:
                    state = None
                    return

        for list_state in self.CLOSED:
            if state.equals(list_state, False):
                if state.get_complete_cost() < list_state.get_complete_cost():
                    self.remove_subtree(list_state, self.CLOSED)
                    self.OPEN.append(state)
                else:
                    state = None
                    return

        self.OPEN.append(state)

    def remove_subtree(self, root: State, target_list):
        """
        Removes the root and its subtree by recursion.
        """
        self.remove(root, target_list)
        for child in root.children:
            self.remove_subtree(child, target_list)

    def remove(self, state: State, target_list):
        target_list = [list_state for list_state in target_list if not state.equals(list_state, True)]
