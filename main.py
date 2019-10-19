from algorithms import tree_search


def main():
    # Map of romania as test data
    graph = [
        {"name": "Arad",
         "actions": [
             {"name": "Zerind", "cost": 75},
             {"name": "Sibiu", "cost": 140},
             {"name": "Timisoara", "cost": 118}
         ]},

        {"name": "Zerind",
         "actions": [
             {"name": "Gradea", "cost": 71},
             {"name": "Arad", "cost": 75}
         ]},

        {"name": "Sibiu",
         "actions": [
             {"name": "Gradea", "cost": 151},
             {"name": "Fagaras", "cost": 99},
             {"name": "Rimnicu", "cost": 80},
             {"name": "Arad", "cost": 140}
         ]},

        {"name": "Timisoara",
         "actions": [
             {"name": "Lugoj", "cost": 111},
             {"name": "Arad", "cost": 118}
         ]},

        {"name": "Gradea",
         "actions": [
             {"name": "Sibiu", "cost": 151},
             {"name": "Zerind", "cost": 71}
         ]},

        {"name": "Fagaras",
         "actions": [
             {"name": "Bucharest", "cost": 211},
             {"name": "Sibiu", "cost": 99}
         ]},

        {"name": "Rimnicu",
         "actions": [
             {"name": "Pitesti", "cost": 91},
             {"name": "Craiova", "cost": 146},
             {"name": "Sibiu", "cost": 80}
         ]},

        {"name": "Lugoj",
         "actions": [
             {"name": "Mehadia", "cost": 70},
             {"name": "Timisoara", "cost": 111}
         ]},

        {"name": "Pitesti",
         "actions": [
             {"name": "Bucharest", "cost": 101},
             {"name": "Craiova", "cost": 138},
             {"name": "Rimnicu", "cost": 97}
         ]},

        {"name": "Craiova",
         "actions": [
             {"name": "Drobeta", "cost": 120},
             {"name": "Rimnicu", "cost": 146},
             {"name": "Pitesti", "cost": 138}
         ]},

        {"name": "Medadia",
         "actions": [
             {"name": "Drobeta", "cost": 75},
             {"name": "Lugoj", "cost": 70}
         ]}
    ]

    path = tree_search(graph, "Bucharest")


if __name__ == '__main__':
    main()
