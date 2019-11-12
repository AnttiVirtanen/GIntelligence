from algorithms.graph_searchable import GraphSearchable
from n_puzzle_solver.sliding_block_puzzle import SlidingBlockPuzzle


class SlidingBlockPuzzleManager(GraphSearchable):

    def __init__(self, state: SlidingBlockPuzzle, goal_state: SlidingBlockPuzzle):
        self.state: SlidingBlockPuzzle = state
        self.goal_state: SlidingBlockPuzzle = goal_state
        self.frontiers = [self.state]
        self.explored = []

    def has_more_frontiers(self):
        return len(self.frontiers) > 0

    def is_goal(self, node):
        return self.goal_state == node

    def goal_found(self, node):
        print("Goal found, awesome.")

    def add_node_to_explored(self, node):
        self.explored.append(node)

    def get_next_states(self, node):
        return node.move_puzzle()

    def should_add_node_to_frontiers(self, node):
        node_in_explored = node in self.explored
        node_in_frontiers = node in self.frontiers
        node_is_goal = self.is_goal(node)

        return not node_in_explored and not node_in_frontiers or node_is_goal

    def add_node_to_frontiers(self, node):
        self.frontiers.append(node)

    def pop_frontier_at(self, index):
        return self.frontiers.pop(index)
