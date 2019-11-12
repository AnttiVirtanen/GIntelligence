from algorithms.graph_search import graph_search
from n_puzzle_solver.path_log import PathLog, PathSummary
from n_puzzle_solver.sliding_block_puzzle import SlidingBlockPuzzle
from n_puzzle_solver.sliding_block_puzzle_manager import SlidingBlockPuzzleManager


def main():
    initial_puzzle_raw = [[2, 1], [None, 4], [5, 3]]

    goal_puzzle_raw = [[1, 2], [3, 4], [5, None]]

    initial_puzzle: SlidingBlockPuzzle = SlidingBlockPuzzle(initial_puzzle_raw)
    goal_puzzle: SlidingBlockPuzzle = SlidingBlockPuzzle(goal_puzzle_raw)

    puzzle_manager: SlidingBlockPuzzleManager = SlidingBlockPuzzleManager(initial_puzzle, goal_puzzle)

    path_log: PathLog = PathLog()

    goal = graph_search(puzzle_manager, path_log)

    path_log.set_goal_node(goal)

    goal_log_summary: PathSummary = path_log.get_goal_log_summary()
    overall_log_summary: PathSummary = path_log.get_overall_log_summary()


if __name__ == '__main__':
    main()
