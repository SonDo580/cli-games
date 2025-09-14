from _types import TTile, TMark, TDirection

NUM_ROUNDS = 250

X: TTile = "X"
O: TTile = "O"
EMPTY: TMark = " "

SIDE: int = 8  # SIDE < 10 and SIDE % 2 == 0
MAX_ROW_DIGITS: int = len(str(SIDE))
ALL_DIGITS: str = "0123456789"

DIRECTIONS: list[TDirection] = (
    (0, 1),  # east
    (1, 1),  # south east
    (1, 0),  # south
    (1, -1),  # south west
    (0, -1),  # west
    (-1, -1),  # north west
    (-1, 0),  # north
    (-1, 1),  # north east
)
