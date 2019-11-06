import copy
from typing import List

HANDLE_INDICATOR = None


class SlidingBlockPuzzle:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.board_width, self.board_length = self.get_board_dimensions(puzzle)

    def __eq__(self, other):
        flat_self = [column for row in self.puzzle for column in row]
        flat_other = [column for row in other.puzzle for column in row]
        zipped_puzzles = zip(flat_self, flat_other)

        return next((False for self_block, other_block in zipped_puzzles if self_block != other_block), True)

    def __str__(self):
        return self.puzzle

    def __repr__(self):
        return f"{self.__class__}: {self.puzzle}"

    def get_board_dimensions(self, list2d: list) -> tuple:
        first_row = next(row for row in list2d)
        number_of_rows = len(list2d)

        return len(first_row), number_of_rows

    def move_puzzle(self) -> List['SlidingBlockPuzzle']:
        new_puzzles = []
        handle_x, handle_y = self.find_puzzle_handle_indices()

        if self.has_top_neighbour(handle_x):
            target_x, target_y = self.get_top_block_indices_for_source(handle_x, handle_y)
            moved_puzzle = self.swap_places_of_blocks(handle_x, handle_y, target_x, target_y)

            new_puzzles.append(moved_puzzle)
        if self.has_right_neighbour(handle_x):
            target_x, target_y = self.get_right_block_indices_for_source(handle_x, handle_y)
            moved_puzzle = self.swap_places_of_blocks(handle_x, handle_y, target_x, target_y)

            new_puzzles.append(moved_puzzle)
        if self.has_bottom_neighbour(handle_x):
            target_x, target_y = self.get_bottom_block_indices_for_source(handle_x, handle_y)
            moved_puzzle = self.swap_places_of_blocks(handle_x, handle_y, target_x, target_y)

            new_puzzles.append(moved_puzzle)
        if self.has_left_neighbour(handle_y):
            target_x, target_y = self.get_left_block_indices_for_source(handle_x, handle_y)
            moved_puzzle = self.swap_places_of_blocks(handle_x, handle_y, target_x, target_y)

            new_puzzles.append(moved_puzzle)

        return new_puzzles

    def find_puzzle_handle_indices(self) -> tuple:
        return next((row_index, column_index) for row_index, row in enumerate(self.puzzle)
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

        origin_value = moved_puzzle[origin_x][origin_y]
        source_value = moved_puzzle[source_x][source_y]

        moved_puzzle[origin_x][origin_y] = source_value
        moved_puzzle[source_x][source_y] = origin_value

        return SlidingBlockPuzzle(moved_puzzle)

    def get_top_block_indices_for_source(self, source_x, source_y):
        return source_x, source_y - 1

    def get_right_block_indices_for_source(self, source_x, source_y):
        return source_x + 1, source_y

    def get_bottom_block_indices_for_source(self, source_x, source_y):
        return source_x, source_y + 1

    def get_left_block_indices_for_source(self, source_x, source_y):
        return source_x - 1, source_y
