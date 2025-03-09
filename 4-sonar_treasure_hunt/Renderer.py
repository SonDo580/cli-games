import math
from functools import cache

from constants import MAX_ROW_DIGITS, NUM_ROWS, NUM_COLUMNS
from Board import Board


class Renderer:
    def __init__(self):
        self._tens_digits_line = self.__get_tens_digits_line()
        self._ones_digits_line = self.__get_ones_digits_line()

    def draw_board(self, board: Board) -> None:
        print(self._tens_digits_line)
        print(self._ones_digits_line)

        for row in range(NUM_ROWS):
            print(self.__get_row_with_coordinates(board.board, row))

        print(self._ones_digits_line)
        print(self._tens_digits_line)

    def __get_tens_digits_line(self) -> str:
        """Build the horizontal tens digits line
        1         2         3     ...
        """
        line = " " * (MAX_ROW_DIGITS + 2)
        space_between = " " * 9
        for col in range(1, math.ceil(NUM_COLUMNS / 10)):
            line += f"{space_between}{col}"
        return line

    def __get_ones_digits_line(self) -> str:
        """Build the horizontal ones digits line
        01234567890123456789012...
        """
        all_digits = "0123456789"
        padding = " " * (MAX_ROW_DIGITS + 1)
        return f"{padding}{all_digits * (NUM_COLUMNS // 10)}{all_digits[:NUM_COLUMNS % 10]}"

    def __get_row_with_coordinates(self, board: list[list[str]], row: int) -> str:
        """Render the board row with vertical coordinates on both sides
         9 ~`~``~``~``~`~`~```~`~``````~```~`~~~`~~```~~`~~~~~`~~`~~~~` 9
        10 ~~~~~`~~~~~````~``~~```~``~`~`~`~``~~```~~~`~`~```~~~~`~`~~` 10
        ...
        """
        padding = self.__get_row_padding(row)
        return f"{padding}{row} {''.join(board[row])} {row}"

    @cache
    def __get_row_padding(self, row: int) -> str:
        return " " * (MAX_ROW_DIGITS - len(str(row)))
