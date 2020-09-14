from State import State


class Solution:
    def __init__(self):
        self.state_sequence = []
        self.action_sequence = []

    def __str__(self):
        return self.to_string()

    def to_string(self, header=False):
        """
        CSV format: Board_State; Cost; Heuristic; Action; Real_Heuristic
        :return:
        """
        if header:
            result = "Board_State;Cost;Heuristic;Action;Real_Heuristic\n"
        else:
            result = ""


        solution_depth: int = len(self.state_sequence)

        for i in range(solution_depth):
            state: State = self.state_sequence[i]
            action: str = self.action_sequence[i]
            real_heuristic = solution_depth - i - 1
            board_state = state.board.board_to_array()
            result = result + str(board_state) + ";" + str(state.cost) + ";" + str(
                state.heuristic) + ";" + action + ";" + str(real_heuristic) + "\n"

        return result
