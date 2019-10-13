def main():
    graph = [
        "Arad", [{"name": "Zerind", "cost": "75"}, {"name": "Sibiu", "cost": 140}, {"name": "Timisoara", "cost": 118}],

        "Zerind", [{"name": "Gradea", "cost": 71}, {"name": "Arad", "cost": 75}],

        "Sibiu", [{"name": "Gradea", "cost": 151}, {"name": "Fagaras", "cost": 99}, {"name": "Rimnicu", "cost": 80},
                  {"name": "Arad", "cost": 140}],

        "Timisoara", [{"name": "Lugoj", "cost": 111}, {"name": "Arad", "cost": 118}],

        "Gradea", [{"name": "Sibiu", "cost": 151}, {"name": "Zerind", "cost": 71}],

        "Fagaras", [{"name": "Bucharest", "cost": 211}, {"name": "Sibiu", "cost": 99}],

        "Rimnicu", [{"name": "Pitesti", "cost": 91}, {"name": "Craiova", "cost": 146}, {"name": "Sibiu", "cost": 80}],

        "Lugoj", [{"name": "Mehadia", "cost": 70}, {"name": "Timisoara", "cost": 111}],

        "Pitesti",
        [{"name": "Bucharest", "cost": 101}, {"name": "Craiova", "cost": 138}, {"name": "Rimnicu", "cost": 97}],

        "Craiova",
        [{"name": "Drobeta", "cost": 120}, {"name": "Rimnicu", "cost": 146}, {"name": "Pitesti", "cost": 138}],

        "Medadia", [{"name": "Drobeta", "cost": 75}, {"name": "Lugoj", "cost": 70}]
    ]


if __name__ == '__main__':
    main()
