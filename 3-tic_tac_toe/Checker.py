from typing import Literal

from constants import SIZE, NUM_WIN


class Checker:
    @staticmethod
    def check_board(
        board: list[list[str]], mark: Literal["X", "O"], row: int, col: int
    ) -> bool:
        """Check if the given mark has won at the specified position"""
        return any(
            get_points(board, mark, row, col) >= NUM_WIN
            for get_points in [
                Checker.__check_horizontal,
                Checker.__check_vertical,
                Checker.__check_northwest_southeast,
                Checker.__check_northeast_southwest,
            ]
        )

    @staticmethod
    def __check_horizontal(
        board: list[list[str]], mark: Literal["X", "O"], row: int, col: int
    ):
        point = 0
        j = col
        while j > 0:
            j -= 1
            if board[row][j] == mark:
                point += 1

        j = col
        while j < SIZE - 1:
            j += 1
            if board[row][j] == mark:
                point += 1

        return point + 1

    @staticmethod
    def __check_vertical(
        board: list[list[str]], mark: Literal["X", "O"], row: int, col: int
    ):
        point = 0
        i = row
        while i > 0:
            i -= 1
            if board[i][col] == mark:
                point += 1

        i = row
        while i < SIZE - 1:
            i += 1
            if board[i][col] == mark:
                point += 1

        return point + 1

    @staticmethod
    def __check_northwest_southeast(
        board: list[list[str]], mark: Literal["X", "O"], row: int, col: int
    ):
        point = 0
        i = row
        j = col
        while i > 0 and j > 0:
            i -= 1
            j -= 1
            if board[i][j] == mark:
                point += 1

        i = row
        j = col
        while i < SIZE - 1 and j < SIZE - 1:
            i += 1
            j += 1
            if board[i][j] == mark:
                point += 1

        return point + 1

    @staticmethod
    def __check_northeast_southwest(
        board: list[list[str]], mark: Literal["X", "O"], row: int, col: int
    ):
        point = 0
        i = row
        j = col
        while i > 0 and j < SIZE - 1:
            i -= 1
            j += 1
            if board[i][j] == mark:
                point += 1

        i = row
        j = col
        while i < SIZE - 1 and j > 0:
            i += 1
            j -= 1
            if board[i][j] == mark:
                point += 1

        return point + 1
