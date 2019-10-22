# shortest path
def breadth_first_search(frontiers):
    minimum_step_cost = min(map(lambda route: route['step_cost'], frontiers))
    first_frontier_to_match, index = next((frontier, index) for index, frontier in enumerate(frontiers)
                                          if frontier['step_cost'] == minimum_step_cost)
    frontiers.pop(index)

    return first_frontier_to_match


# Cheapest first
def uniform_cost_search(frontiers):
    minimum_cost = min(map(lambda route: route['cost'], frontiers))

    first_frontier_to_match, index = next((frontier, index) for index, frontier in enumerate(frontiers)
                                          if frontier['cost'] == minimum_cost)
    frontiers.pop(index)

    return first_frontier_to_match


def tree_search(graph, goal_path):
    explored_routes = []

    frontier = next(([node] for node in graph), [])
    normalized_graph = {node['name']: node for node in graph}

    while True:
        if len(frontier) == 0:
            break
        #path = breadth_first_search(frontier)
        path = uniform_cost_search(frontier)

        if path['name'] == goal_path:
            print(
                f"GOAL FOUND, route is: {path['route']} and step cost {path['step_cost']} with cost of {path['cost']}")
            continue

        explored_routes.append(path['name'])

        path_route = path.get('route', path['name'])

        for action in path['actions']:
            new_frontier = {**normalized_graph[action['name']]}

            new_frontier['cost'] = action['cost'] + path['cost']
            new_frontier['step_cost'] = action['step_cost'] + path['step_cost']
            new_frontier['route'] = f"{path_route}->{action['name']}"

            if action['name'] not in explored_routes and \
                    not any(map(lambda route: route['name'] == action['name'], frontier)) or action[
                'name'] == goal_path:
                frontier.append(new_frontier)

    return None
