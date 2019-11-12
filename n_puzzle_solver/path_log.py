from n_puzzle_solver.sliding_block_puzzle import SlidingBlockPuzzle


class PathSummary:
    def __init__(self):
        self.actions_taken = 0
        self.path_history = []

    def add_path_to_history(self, path):
        self.actions_taken += 1
        self.path_history.append(path)


class PathLog:
    def __init__(self, goal_node: SlidingBlockPuzzle = None):
        self.goal_node = goal_node
        self.overall_path_summary: PathSummary = PathSummary()

    def set_goal_node(self, goal_node):
        self.goal_node = goal_node

    def mark_as_explored(self, node):
        self.overall_path_summary.add_path_to_history(node.puzzle)

    def get_overall_log_summary(self) -> PathSummary:
        return self.overall_path_summary

    def get_goal_log_summary(self) -> PathSummary:
        if not self.goal_node:
            raise Exception("PathLog has no goal node")

        path_summary = PathSummary()
        path_summary = self.traverse_tree(self.goal_node, path_summary)

        return path_summary

    def traverse_tree(self, node: SlidingBlockPuzzle, path_summary: PathSummary) -> PathSummary:
        path_summary.add_path_to_history(node.puzzle)

        if node.puzzle_parent:
            path_summary = self.traverse_tree(node.puzzle_parent, path_summary)

        return path_summary
