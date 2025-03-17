import sys
import random

from constants import (
    X,
    O,
    EMPTY,
    HINT_MARK,
    COMPUTER,
    PLAYER,
    SIDE,
    DIRECTIONS,
    QUIT_CHOICE,
    HINT_CHOICE,
)
from _types import TTile, TTurn, TBoard, TScoreDict, TPosition, TPlayerChoice
from Board import Board
from Renderer import Renderer


class Game:
    def __init__(self):
        pass

    def start(self) -> None:
        print("Welcome to Reversegam!")
        self.__loop()

    def __loop(self) -> None:
        while True:
            player_tile: TTile = self.__get_player_tile()
            computer_tile: TTile = self.__assign_computer_tile(player_tile)
            final_board: TBoard = self.__round(player_tile, computer_tile)

            # Display the final result
            score_dict: TScoreDict = self.__get_scores(final_board)
            self.__print_scores(score_dict, player_tile, computer_tile)
            self.__print_round_results(score_dict, player_tile, computer_tile)

            # Ask if user want to play again
            if not (input("Do you want to play again? (y/n)?").strip().lower() == "y"):
                print("Thanks for playing!")
                sys.exit()

    def __round(self, player_tile: TTile, computer_tile: TTile) -> TBoard:
        """Handle a round. Return the final board"""
        show_hints: bool = False
        board: TBoard = Board.init()
        turn: TTurn = self.__pick_first_turn()
        print(f"The {turn} will go first.")

        while True:
            player_valid_moves: list[TPosition] = self.__get_valid_moves(
                board, player_tile
            )
            computer_valid_moves: list[TPosition] = self.__get_valid_moves(
                board, computer_tile
            )

            # No one can move -> End this round
            if len(player_valid_moves) == 0 and len(computer_valid_moves) == 0:
                break

            if turn == PLAYER:
                if len(player_valid_moves) > 0:
                    # Show current board (with or without hints) and scores
                    if show_hints:
                        board_with_hints = self.__get_cloned_board_with_hint(
                            board, player_tile
                        )
                        Renderer.draw_board(board_with_hints)
                    else:
                        Renderer.draw_board(board)

                    score_dict: TScoreDict = self.__get_scores(board)
                    self.__print_scores(score_dict, player_tile, computer_tile)

                    # Player move
                    player_choice: TPlayerChoice = self.__get_player_choice(
                        board, player_tile
                    )
                    if player_choice == QUIT_CHOICE:
                        print("Thanks for playing!")
                        sys.exit()
                    elif player_choice == HINT_CHOICE:
                        show_hints = not show_hints
                        continue
                    else:
                        self.__make_move(
                            board, player_tile, player_choice[0], player_choice[1]
                        )
                turn = COMPUTER  # Swap turn

            elif turn == COMPUTER:
                if len(computer_valid_moves) > 0:
                    # Show current board and scores
                    Renderer.draw_board(board)
                    score_dict: TScoreDict = self.__get_scores(board)
                    self.__print_scores(score_dict, player_tile, computer_tile)

                    # Computer move
                    computer_move: TPosition = self.__get_computer_move(board, computer_tile)
                    self.__make_move(
                        board, computer_tile, computer_move[0], computer_move[1]
                    )
                turn = PLAYER  # Swap turn

        return board  # Return the final board

    def __print_round_results(self, score_dict, player_tile, computer_tile) -> None:
        player_score: int = score_dict[player_tile]
        computer_score: int = score_dict[computer_tile]

        if player_score > computer_score:
            print(
                f"Congratulations! You beat the computer by {player_score - computer_score} points!"
            )
        elif player_score < computer_score:
            print(
                f"You lost. The computer beat you by {computer_score - player_score} points."
            )
        else:
            print("The game was a tie!")

    def __get_player_tile(self) -> TTile:
        """Let player choose the tile they want"""
        while True:
            player_choice: str = (
                input(f"Which do you want to be? ({X}/{O})").strip().upper()
            )
            if player_choice in [X, O]:
                return player_choice
            print(f"Please enter {X} or {O}!")

    def __assign_computer_tile(self, player_tile: TTile) -> TTile:
        """Assign the remaining tile for the computer"""
        return O if player_tile == X else X

    def __pick_first_turn(self) -> TTurn:
        """Randomly choose who goes first"""
        return random.choice([COMPUTER, PLAYER])

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
        self, score_dict: TScoreDict, player_tile: TTile, computer_tile: TTile
    ) -> None:
        print(
            f"You: {score_dict[player_tile]} points. Computer: {score_dict[computer_tile]} points."
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

    def __get_cloned_board_with_hint(self, board: TBoard, tile: TTile) -> TBoard:
        """Return a cloned board with hint for valid moves"""
        cloned_board: TBoard = Board.clone(board)
        valid_moves: list[TPosition] = self.__get_valid_moves(board, tile)
        for row, col in valid_moves:
            cloned_board[row][col] = HINT_MARK
        return cloned_board

    def __make_move(self, board: TBoard, tile: TTile, row: int, col: int) -> None:
        """Place the tile at a valid (row, col) and flip opponent's tiles"""
        tiles_to_flip: list[TPosition] = self.__get_tiles_to_flip(board, tile, row, col)
        board[row][col] = tile
        for x, y in tiles_to_flip:
            board[x][y] = tile

    def __get_player_choice(self, board: TBoard, player_tile: TTile) -> TPlayerChoice:
        """
        Get player choice, which can be:
        - a valid move (row, col)
        - quit option: exit the game immediately
        - toggle hints option: show valid moves on the board
        """
        while True:
            choice: str = (
                input(
                    f"Enter your move (0-{SIDE - 1} 0-{SIDE - 1}), {QUIT_CHOICE} to quit, {HINT_CHOICE} to toggle hints:\n"
                )
                .strip()
                .lower()
            )

            if choice in [QUIT_CHOICE, HINT_CHOICE]:
                return choice

            try:
                row, col = map(int, choice.split())
                if not (0 <= row < SIDE and 0 <= col < SIDE):
                    print(
                        f"Invalid move! Enter row and column in range [0-{SIDE - 1}]."
                    )
                    continue
                if board[row][col] != EMPTY:
                    print("Invalid move! The cell is already occupied.")
                    continue
                if not self.__get_tiles_to_flip(board, player_tile, row, col):
                    print(
                        "Invalid move! You must place your tile where it can flip opponent tiles."
                    )
                    continue
                return (row, col)

            except ValueError:
                print(
                    "Invalid input! Enter two numbers separated by space (e.g., '3 4')."
                )

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
            if Board.is_on_corner(row, col):
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
