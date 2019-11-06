from algorithms.graph_search import graph_search
from n_puzzle_solver.sliding_block_puzzle import SlidingBlockPuzzle
from n_puzzle_solver.sliding_block_puzzle_manager import SlidingBlockPuzzleManager


def main():
    initial_puzzle_raw = [[7, 5, 3], [8, 2, 6], [1, 4, None]]
    goal_puzzle_raw = [[1, 2, 3], [4, 5, 6], [7, 8, None]]

    initial_puzzle: SlidingBlockPuzzle = SlidingBlockPuzzle(initial_puzzle_raw)
    goal_puzzle: SlidingBlockPuzzle = SlidingBlockPuzzle(goal_puzzle_raw)

    puzzle_manager: SlidingBlockPuzzleManager = SlidingBlockPuzzleManager(initial_puzzle, goal_puzzle)

    goal = graph_search(puzzle_manager)


if __name__ == '__main__':
    main()
