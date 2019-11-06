from typing import Type

from algorithms.graph_searchable import GraphSearchable


def uniform_cost_search(graph_struct: Type[GraphSearchable]):
    return graph_struct.pop_frontier_at(0)


def graph_search(graph_struct: Type[GraphSearchable]):
    while graph_struct.has_more_frontiers():
        node = uniform_cost_search(graph_struct)

        if graph_struct.is_goal(node):
            graph_struct.goal_found(node)

            continue

        graph_struct.add_node_to_explored(node)

        for next_node in graph_struct.get_next_states():
            if graph_struct.should_add_node_to_frontiers(next_node):
                graph_struct.add_node_to_frontiers(next_node)

    return None
