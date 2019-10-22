from algorithms import tree_search


def main():
    # Map of romania as test data
    graph = [
        {"name": "Arad", "cost": 0, "step_cost": 0,
         "actions": [
             {"name": "Zerind", "cost": 75, "step_cost": 1},
             {"name": "Sibiu", "cost": 140, "step_cost": 1},
             {"name": "Timisoara", "cost": 118, "step_cost": 1}
         ]},

        {"name": "Zerind", "cost": 0, "step_cost": 0,
         "actions": [
             {"name": "Gradea", "cost": 71, "step_cost": 1},
             {"name": "Arad", "cost": 75, "step_cost": 1}
         ]},

        {"name": "Sibiu", "cost": 0, "step_cost": 0,
         "actions": [
             {"name": "Gradea", "cost": 151, "step_cost": 1},
             {"name": "Fagaras", "cost": 99, "step_cost": 1},
             {"name": "Rimnicu", "cost": 80, "step_cost": 1},
             {"name": "Arad", "cost": 140, "step_cost": 1}
         ]},

        {"name": "Timisoara", "cost": 0, "step_cost": 0,
         "actions": [
             {"name": "Lugoj", "cost": 111, "step_cost": 1},
             {"name": "Arad", "cost": 118, "step_cost": 1}
         ]},

        {"name": "Gradea", "cost": 0, "step_cost": 0,
         "actions": [
             {"name": "Sibiu", "cost": 151, "step_cost": 1},
             {"name": "Zerind", "cost": 71, "step_cost": 1}
         ]},

        {"name": "Fagaras", "cost": 0, "step_cost": 0,
         "actions": [
             {"name": "Bucharest", "cost": 211, "step_cost": 1},
             {"name": "Sibiu", "cost": 99, "step_cost": 1}
         ]},

        {"name": "Rimnicu", "cost": 0, "step_cost": 0,
         "actions": [
             {"name": "Pitesti", "cost": 97, "step_cost": 1},
             {"name": "Craiova", "cost": 146, "step_cost": 1},
             {"name": "Sibiu", "cost": 80, "step_cost": 1}
         ]},

        {"name": "Lugoj", "cost": 0, "step_cost": 0,
         "actions": [
             {"name": "Mehadia", "cost": 70, "step_cost": 1},
             {"name": "Timisoara", "cost": 111, "step_cost": 1}
         ]},

        {"name": "Pitesti", "cost": 0, "step_cost": 0,
         "actions": [
             {"name": "Bucharest", "cost": 101, "step_cost": 1},
             {"name": "Craiova", "cost": 138, "step_cost": 1},
             {"name": "Rimnicu", "cost": 97, "step_cost": 1}
         ]},

        {"name": "Craiova", "cost": 0, "step_cost": 0,
         "actions": [
             {"name": "Drobeta", "cost": 120, "step_cost": 1},
             {"name": "Rimnicu", "cost": 146, "step_cost": 1},
             {"name": "Pitesti", "cost": 138, "step_cost": 1}
         ]},

        {"name": "Mehadia", "cost": 0, "step_cost": 0,
         "actions": [
             {"name": "Drobeta", "cost": 75, "step_cost": 1},
             {"name": "Lugoj", "cost": 70, "step_cost": 1}
         ]},

        {"name": "Drobeta", "cost": 0, "step_cost": 0,
         "actions": [
             {"name": "Craiova", "cost": 120, "step_cost": 1},
             {"name": "Mehadia", "cost": 75, "step_cost": 1}
         ]},
        {"name": "Bucharest", "cost": 0, "step_cost": 0,
         "actions": [
             {"name": "Pitesti", "cost": 101, "step_cost": 1},
             {"name": "Fagaras", "cost": 211, "step_cost": 1}
         ]},
    ]

    path = tree_search(graph, "Bucharest")


if __name__ == '__main__':
    main()
