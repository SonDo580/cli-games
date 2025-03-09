import random
import math

from constants import NUM_ROWS, NUM_COLUMNS, NUM_CHESTS, OCEAN_WAVES, SONAR_RANGE


class Board:
    def __init__(self):
        self.board = self.__get_new_board()
        self.chest_set = self.__get_chest_set()
        self._max_distance = math.ceil(math.sqrt(NUM_ROWS**2 + NUM_COLUMNS**2))

    def __get_new_board(self) -> list[list[str]]:
        """Return initial board state"""
        board: list[list[str]] = []
        for row in range(NUM_ROWS):
            board.append([])
            for _ in range(NUM_COLUMNS):
                board[row].append(random.choice(OCEAN_WAVES))
        return board

    def __get_chest_set(self) -> set[tuple[int, int]]:
        """Return the set of chest coordinates"""
        chest_set: set[tuple[int, int]] = set()
        while len(chest_set) < NUM_CHESTS:
            new_chest = (
                random.randint(0, NUM_ROWS - 1),
                random.randint(0, NUM_COLUMNS - 1),
            )
            if new_chest not in chest_set:
                chest_set.add(new_chest)
        return chest_set

    @staticmethod
    def is_on_board(row: int, col: int) -> bool:
        return row >= 0 and row < NUM_ROWS and col >= 0 and col < NUM_COLUMNS

    def make_move(self, row: int, col: int) -> int:
        """
        Place the sonar device at a specific coordinates (update board state).
        Collect the treasure chests as they are found (remove from chest set).
        Return the distance from sonar to the closest chest.
        """
        smallest_distance = self._max_distance
        for c_row, c_column in self.chest_set:
            distance = self.__get_distance(c_row, c_column, row, col)
            if distance < smallest_distance:
                smallest_distance = distance

        if smallest_distance == 0:
            self.chest_set.remove((row, col))
            print("You have found a sunken treasure chest!")
        elif smallest_distance < SONAR_RANGE:
            self.board[row][col] = str(smallest_distance)
            print(
                f"Treasure detected at a distance of {smallest_distance} from the sonar device."
            )
        else:
            self.board[row][col] = "X"
            print("Sonar did not detect anything. All treasure chests out of range.")

        return smallest_distance

    def __get_distance(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return round(math.sqrt((row1 - row2) ** 2 + (col1 - col2) ** 2))
