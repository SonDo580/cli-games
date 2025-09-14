from typing import TypeAlias, Literal

TTurn: TypeAlias = Literal["computer", "player"]
TTile: TypeAlias = Literal["X", "O"]
TMark: TypeAlias = TTile | Literal[" ", "."]
TBoard: TypeAlias = list[list[TMark]]
TScoreDict: TypeAlias = dict[TTile, int]
TPosition: TypeAlias = tuple[int, int] 
TDirection: TypeAlias = tuple[int, int] 
TPlayerChoice: TypeAlias = TPosition | Literal["q", "h"]