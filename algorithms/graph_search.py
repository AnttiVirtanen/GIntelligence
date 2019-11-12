from typing import Type

from algorithms.graph_searchable import GraphSearchable
from n_puzzle_solver.path_log import PathLog
from n_puzzle_solver.sliding_block_puzzle import SlidingBlockPuzzle


def uniform_cost_search(graph_struct: Type[GraphSearchable]):
    pass


def brute_force(graph_struct: Type[GraphSearchable]):
    return graph_struct.pop_frontier_at(0)


def graph_search(graph_struct: Type[GraphSearchable], path_log: PathLog) -> SlidingBlockPuzzle:
    while graph_struct.has_more_frontiers():
        node = brute_force(graph_struct)

        if graph_struct.is_goal(node):
            graph_struct.goal_found(node)

            return node

        graph_struct.add_node_to_explored(node)

        for next_node in graph_struct.get_next_states(node):
            if graph_struct.should_add_node_to_frontiers(next_node):
                graph_struct.add_node_to_frontiers(next_node)

    return None
