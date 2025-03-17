from constants import EMPTY, SIDE, X, O
from _types import TBoard, TScoreDict


class Board:
    @staticmethod
    def new() -> TBoard:
        """Get an empty board"""
        return [[EMPTY for _ in range(SIDE)] for _ in range(SIDE)]
    
    @staticmethod
    def init() -> TBoard:
        """Get the empty board then place starting tiles at the center"""
        # Note: works for SIDE % 2 == 0
        board: TBoard = Board.new()

        mid: int = SIDE // 2
        board[mid-1][mid-1] = X # north west
        board[mid-1][mid] = O # north east
        board[mid][mid] = X # south east
        board[mid][mid - 1] = O # south west

        return board


    @staticmethod
    def clone(board: TBoard) -> TBoard:
        """Get a deep clone version of the board"""
        cloned_board: TBoard = Board.new()
        for row in range(SIDE):
            for col in range(SIDE):
                cloned_board[row][col] = board[row][col]
        return cloned_board

    @staticmethod
    def is_on_board(row: int, col: int) -> bool:
        return 0 <= row < SIDE and 0 <= col < SIDE

    @staticmethod
    def is_on_corner(row: int, col: int) -> bool:
        return (row == 0 or row == SIDE - 1) and (col == 0 or col == SIDE - 1)
