from src.State import State


class DumbAssLists:
    def __init__(self):
        self.OPEN = []
        self.CLOSED = []

    def __str__(self):
        result = "OPEN:\n"

        for item in self.OPEN:
            result = result + item.to_string()

        result = result + "CLOSED:\n"

        for item in self.CLOSED:
            result = result + item.to_string() + "\n\n"

        return result

    def poll(self) -> State:
        favorite: State = None

        for state in self.OPEN:
            if favorite is None or state.get_complete_cost() < favorite.get_complete_cost():
                favorite = state

        self.OPEN = [list_state for list_state in self.OPEN if not favorite.equals(list_state, True)]

        self.push_closed(favorite)
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
                    self.remove_subtree(list_state)
                    self.clear_lists()
                    self.OPEN.append(state)
                else:
                    state = None
                    return

        for list_state in self.CLOSED:
            if state.equals(list_state, False):
                if state.get_complete_cost() < list_state.get_complete_cost():
                    self.remove_subtree(list_state)
                    self.clear_lists()
                    self.OPEN.append(state)
                else:
                    state = None
                    return

        self.OPEN.append(state)

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
