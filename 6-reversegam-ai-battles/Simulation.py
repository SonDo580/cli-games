import random

from constants import (
    NUM_ROUNDS,
    X,
    O,
    EMPTY,
    SIDE,
    DIRECTIONS,
)
from _types import TTile, TBoard, TScoreDict, TPosition
from Board import Board


class Simulation:
    def __init__(self):
        pass

    def start(self) -> None:
        print("Welcome to Reversegam!")
        x_wins = o_wins = 0

        for _ in range(NUM_ROUNDS):
            score_dict = self.__round()
            self.__print_scores(score_dict, X, O)

            if score_dict[X] > score_dict[O]:
                x_wins += 1
            elif score_dict[O] > score_dict[X]:
                o_wins += 1

        self.__print_simulation_result(x_wins, o_wins)

    def __print_simulation_result(self, x_wins: int, o_wins: int) -> None:
        """Print the result of all the rounds"""
        x_wins_percent = round(100 * x_wins / NUM_ROUNDS, 1)
        o_wins_percent = round(100 * o_wins / NUM_ROUNDS, 1)
        ties = NUM_ROUNDS - x_wins - o_wins
        ties_percent = round(100 - x_wins_percent - o_wins_percent, 1)

        print("==============================")
        print(f"X wins: {x_wins}/{NUM_ROUNDS} ({x_wins_percent}%)")
        print(f"O wins: {o_wins}/{NUM_ROUNDS} ({o_wins_percent}%)")
        print(f"Ties: {ties}/{NUM_ROUNDS} ({ties_percent}%)")

    def __round(self) -> TScoreDict:
        """Handle a round. Return the final scores."""
        player_1_tile: TTile = X
        player_2_tile: TTile = O
        board: TBoard = Board.init()
        turn: TTile = self.__pick_first_turn()

        while True:
            player_1_valid_moves: list[TPosition] = self.__get_valid_moves(
                board, player_1_tile
            )
            player_2_valid_moves: list[TPosition] = self.__get_valid_moves(
                board, player_2_tile
            )

            # No one can move -> End this round
            if len(player_1_valid_moves) == 0 and len(player_2_valid_moves) == 0:
                break

            if turn == player_1_tile:
                if len(player_1_valid_moves) > 0:
                    player_1_move: TPosition = self.__get_computer_move(
                        board, player_1_tile
                    )
                    self.__make_move(
                        board, player_1_tile, player_1_move[0], player_1_move[1]
                    )
                turn = player_2_tile

            elif turn == player_2_tile:
                if len(player_2_valid_moves) > 0:
                    player_2_move: TPosition = self.__get_computer_move(
                        board, player_2_tile
                    )
                    self.__make_move(
                        board, player_2_tile, player_2_move[0], player_2_move[1]
                    )
                turn = player_1_tile

        score_dict: TScoreDict = self.__get_scores(board)
        return score_dict

    def __pick_first_turn(self) -> TTile:
        """Randomly choose who goes first"""
        return random.choice([X, O])

    def __get_scores(self, board: TBoard) -> TScoreDict:
        """Determine the score of player and computer"""
        x_score: int = 0
        o_score: int = 0
        for row in range(SIDE):
            for col in range(SIDE):
                if board[row][col] == X:
                    x_score += 1
                elif board[row][col] == O:
                    o_score += 1
        return {X: x_score, O: o_score}

    def __print_scores(
        self, score_dict: TScoreDict, player_1_tile: TTile, player_2_tile: TTile
    ) -> None:
        """Print the result of a round"""
        print(
            f"{player_1_tile} scored {score_dict[player_1_tile]} points. {player_2_tile} scored {score_dict[player_2_tile]} points."
        )

    def __get_tiles_to_flip(
        self, board: TBoard, tile: TTile, placed_row: int, placed_col: int
    ) -> list[TPosition]:
        """
        Return the list of other tile's positions to be flipped
        if tile is placed at a valid position (row, col)
        """
        other_tile: TTile = X if tile == O else O
        tiles_to_flip: list[TPosition] = []

        for dx, dy in DIRECTIONS:
            # Collect the other tile's positions on the way
            captured: list[TPosition] = []

            row: int = placed_row + dx
            col: int = placed_col + dy
            while Board.is_on_board(row, col) and board[row][col] == other_tile:
                captured.append((row, col))
                row += dx
                col += dy

            # If the sequence ends with the same tile, the captured positions are valid
            if Board.is_on_board(row, col) and board[row][col] == tile:
                tiles_to_flip.extend(captured)

        return tiles_to_flip

    def __is_possibly_valid_move(self, board: TBoard, row: int, col: int) -> bool:
        """
        Check if a move is possibly valid.
        Haven't check if there are tiles to flipped.
        """
        return Board.is_on_board(row, col) and board[row][col] == EMPTY

    def __is_valid_move(self, board: TBoard, tile: TTile, row: int, col: int) -> bool:
        """
        Combine the conditions:
        - an empty position on the board
        - there are tiles to be flipped
        """
        is_possibly_valid: bool = self.__is_possibly_valid_move(board, row, col)
        tiles_to_flip: list[TPosition] = self.__get_tiles_to_flip(board, tile, row, col)
        return is_possibly_valid and len(tiles_to_flip) > 0

    def __get_valid_moves(self, board: TBoard, tile: TTile) -> list[TPosition]:
        """Return the list of valid moves for the given tile"""
        valid_moves: list[TPosition] = []
        for row in range(SIDE):
            for col in range(SIDE):
                if self.__is_valid_move(board, tile, row, col):
                    valid_moves.append((row, col))
        return valid_moves

    def __make_move(self, board: TBoard, tile: TTile, row: int, col: int) -> None:
        """Place the tile at a valid (row, col) and flip opponent's tiles"""
        tiles_to_flip: list[TPosition] = self.__get_tiles_to_flip(board, tile, row, col)
        board[row][col] = tile
        for x, y in tiles_to_flip:
            board[x][y] = tile

    def __get_computer_move(self, board: TBoard, computer_tile: TTile) -> TPosition:
        """Determine the move for computer"""
        possible_moves: list[TPosition] = self.__get_valid_moves(board, computer_tile)

        # Randomize the order of moves:
        # - To make the AI less predictable (avoid player memorizing the moves)
        # - Needed because the implementation below always choose the first best move
        #   (when there are multiple moves producing the same score)
        random.shuffle(possible_moves)

        # Find the highest-scoring move
        best_score: int = -1
        best_move: TPosition | None = None
        for row, col in possible_moves:
            # Go for a corner right away if possible
            # (cannot be flipped, control the edges and diagonal)
            if Board.is_at_corner(row, col):
                return (row, col)

            # Make the "virtual" move to get the score
            cloned_board: TBoard = Board.clone(board)
            self.__make_move(cloned_board, computer_tile, row, col)
            score_dict: TScoreDict = self.__get_scores(cloned_board)
            computer_score: int = score_dict[computer_tile]

            # Update best score and best move
            if computer_score > best_score:
                best_move = (row, col)
                best_score = computer_score

        return best_move
