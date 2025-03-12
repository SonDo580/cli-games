from constants import SIZE


class Board:
    def __init__(self):
        pass

    @staticmethod
    def create() -> list[list[str]]:
        """Create an empty SIZE x SIZE board"""
        return [[" " for _ in range(SIZE)] for _ in range(SIZE)]

    @staticmethod
    def draw(board: list[list[str]]) -> None:
        for i in range(SIZE):
            print("|".join(board[i]))
            if i < SIZE - 1:
                print("+".join("-" * SIZE))
        print("-" * 30)

    @staticmethod
    def is_on_board(row: int, col: int) -> bool:
        return 0 <= row <= SIZE and 0 <= col <= SIZE
