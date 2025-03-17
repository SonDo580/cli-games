from _types import TTurn, TTile, TMark, TDirection, TPlayerChoice

COMPUTER: TTurn = "computer"
PLAYER: TTurn = "player"

X: TTile = "X"
O: TTile = "O"
EMPTY: TMark = " "
HINT_MARK: TMark = "."

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

QUIT_CHOICE: TPlayerChoice = "q"
HINT_CHOICE: TPlayerChoice = "h"
