from abc import ABC


class GraphSearchable(ABC):

    def has_more_frontiers(self):
        raise NotImplementedError

    def is_goal(self, node):
        raise NotImplementedError

    def goal_found(self, node):
        raise NotImplementedError

    def add_node_to_explored(self, node):
        raise NotImplementedError

    def get_next_states(self):
        raise NotImplementedError

    def should_add_node_to_frontiers(self, node):
        raise NotImplementedError

    def add_node_to_frontiers(self, node):
        raise NotImplementedError

    def pop_frontier_at(self, index):
        raise NotImplementedError
