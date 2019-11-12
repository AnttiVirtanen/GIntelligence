import copy
from typing import List

HANDLE_INDICATOR = None


class SlidingBlockPuzzle:
    def __init__(self, puzzle, puzzle_parent=None):
        self.puzzle, self.puzzle_parent = puzzle, puzzle_parent
        self.board_width, self.board_length = self.get_board_dimensions(puzzle)

    def __eq__(self, other):
        flat_self = self.flatten_puzzle(self.puzzle)
        flat_other = self.flatten_puzzle(other.puzzle)
        zipped_puzzles = zip(flat_self, flat_other)

        return next((False for self_block, other_block in zipped_puzzles if self_block != other_block), True)

    def __str__(self):
        return ", ".join(map(str, self.flatten_puzzle(self.puzzle)))

    def __repr__(self):
        return f"{self.__class__}: {self.puzzle}"

    def flatten_puzzle(self, puzzle):
        return [column for row in puzzle for column in row]

    def get_board_dimensions(self, list2d: list) -> tuple:
        first_row = next(row for row in list2d)
        number_of_rows = len(list2d)

        return len(first_row), number_of_rows

    def move_puzzle(self) -> List['SlidingBlockPuzzle']:
        new_puzzles = []
        handle_x, handle_y = self.find_puzzle_handle_indices()

        if self.has_top_neighbour(handle_y):
            target_x, target_y = self.get_top_block_indices_for_source(handle_x, handle_y)
            moved_puzzle = self.swap_places_of_blocks(handle_x, handle_y, target_x, target_y)
            moved_puzzle.set_puzzle_parent(self)

            new_puzzles.append(moved_puzzle)
        if self.has_right_neighbour(handle_x):
            target_x, target_y = self.get_right_block_indices_for_source(handle_x, handle_y)
            moved_puzzle = self.swap_places_of_blocks(handle_x, handle_y, target_x, target_y)
            moved_puzzle.set_puzzle_parent(self)

            new_puzzles.append(moved_puzzle)
        if self.has_bottom_neighbour(handle_y):
            target_x, target_y = self.get_bottom_block_indices_for_source(handle_x, handle_y)
            moved_puzzle = self.swap_places_of_blocks(handle_x, handle_y, target_x, target_y)
            moved_puzzle.set_puzzle_parent(self)

            new_puzzles.append(moved_puzzle)
        if self.has_left_neighbour(handle_x):
            target_x, target_y = self.get_left_block_indices_for_source(handle_x, handle_y)
            moved_puzzle = self.swap_places_of_blocks(handle_x, handle_y, target_x, target_y)
            moved_puzzle.set_puzzle_parent(self)

            new_puzzles.append(moved_puzzle)

        return new_puzzles

    def find_puzzle_handle_indices(self) -> tuple:
        return next((column_index, row_index) for row_index, row in enumerate(self.puzzle)
                    for column_index, column in enumerate(row) if column == HANDLE_INDICATOR)

    def has_top_neighbour(self, row_index) -> bool:
        return row_index != 0

    def has_bottom_neighbour(self, row_index) -> bool:
        return row_index + 1 < self.board_length

    def has_left_neighbour(self, cell_index) -> bool:
        return cell_index > 0

    def has_right_neighbour(self, cell_index) -> bool:
        return cell_index + 1 < self.board_width

    def swap_places_of_blocks(self, origin_x, origin_y, source_x, source_y) -> 'SlidingBlockPuzzle':
        moved_puzzle = copy.deepcopy(self.puzzle)

        origin_value = moved_puzzle[origin_y][origin_x]
        source_value = moved_puzzle[source_y][source_x]

        moved_puzzle[origin_y][origin_x] = source_value
        moved_puzzle[source_y][source_x] = origin_value

        return SlidingBlockPuzzle(moved_puzzle)

    def set_puzzle_parent(self, puzzle_parent):
        self.puzzle_parent = puzzle_parent

    def get_top_block_indices_for_source(self, source_x, source_y):
        return source_x , source_y - 1

    def get_right_block_indices_for_source(self, source_x, source_y):
        return source_x + 1, source_y

    def get_bottom_block_indices_for_source(self, source_x, source_y):
        return source_x, source_y + 1

    def get_left_block_indices_for_source(self, source_x, source_y):
        return source_x - 1, source_y
