from typing import TypeAlias, Literal

TTile: TypeAlias = Literal["X", "O"]
TMark: TypeAlias = TTile | Literal[" "]
TBoard: TypeAlias = list[list[TMark]]
TScoreDict: TypeAlias = dict[TTile, int]
TPosition: TypeAlias = tuple[int, int] 
TDirection: TypeAlias = tuple[int, int] 