from functools import cache

from constants import MAX_ROW_DIGITS, SIDE, ALL_DIGITS
from _types import TBoard


# Note: Renderer works for SIDE < 10 
class Renderer:
    @staticmethod
    def draw_board(board: TBoard) -> None:
        column_indicators: str = Renderer.__get_column_indicators()
        horizontal_border: str = Renderer.__get_board_horizontal_border()

        print(column_indicators)
        print(horizontal_border)

        for row in range(SIDE):
            print(Renderer.__get_board_row_with_indicators(board, row))

        print(horizontal_border)
        print(column_indicators)

    @cache
    def __get_column_indicators() -> str:
        padding: str = " " * (MAX_ROW_DIGITS + 1)
        return f"{padding}{ALL_DIGITS[:SIDE]}"

    @cache
    def __get_board_horizontal_border() -> str:
        padding: str = " " * MAX_ROW_DIGITS
        return f"{padding}+{'-' * SIDE}+"

    def __get_board_row_with_indicators(board: TBoard, row: int) -> str:
        """Render the board row with row indicators on both sides
        1|X O X ...|1
        2| O X  ...|2
        """
        board_row: str = "".join(str(mark) for mark in board[row])
        return f"{row}|{board_row}|{row}"
