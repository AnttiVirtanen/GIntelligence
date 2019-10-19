def remove_choice(frontier):
    return frontier.pop()


def tree_search(graph, goal_path):
    frontier = next(([node] for node in graph), [])
    normalized_graph = {node['name']: node for node in graph}

    while True:
        if len(frontier) == 0:
            break
        path = remove_choice(frontier)

        if path['name'] == goal_path:
            return path

        path_cost = path.get('cost') or 0
        path_route = path.get('router') or path['name']

        for action in path['actions']:
            new_frontier = normalized_graph[action['name']]
            new_frontier['cost'] = action['cost'] + path_cost
            new_frontier['route'] = f"{path_route}->{action['name']}"

            frontier.append(new_frontier)

    return None
