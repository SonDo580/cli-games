import sys

from constants import INSTRUCTIONS, NUM_SONAR_DEVICES, NUM_ROWS, NUM_COLUMNS
from Renderer import Renderer
from Board import Board


class Game:
    def __init__(self):
        self._renderer = Renderer()

    def start(self):
        print("S O N A R !")

        # Ask if user need instructions
        if (
            input("Would you like to view the instructions? (y/n): ").strip().lower()
            == "y"
        ):
            print(INSTRUCTIONS)

        # Start the game loop
        self.__loop()

    def __loop(self):
        while True:
            num_sonar_devices = NUM_SONAR_DEVICES
            board = Board()
            previous_move_set: set[tuple[int, int]] = set()
            self._renderer.draw_board(board)

            # Keep placing sonar devices until we find all the chests
            # or run out of sonar devices
            while num_sonar_devices > 0:
                print(
                    f"You have {num_sonar_devices} sonar device(s) left. {len(board.chest_set)} treasure chest(s) remaining."
                )

                row, col = self.__get_move(previous_move_set)
                previous_move_set.add((row, col))
                smallest_distance = board.make_move(row, col)

                # If a sunken chest is found,
                # update all sonar devices on the map (find the next closest chest)
                if smallest_distance == 0:
                    for prev_row, prev_col in previous_move_set:
                        board.make_move(prev_row, prev_col)

                self._renderer.draw_board(board)

                # Check if all chests have been found
                if len(board.chest_set) == 0:
                    print(
                        "You have found all the sunken treasure chests! Congratulations and good game!"
                    )
                    break

                num_sonar_devices -= 1

            # Check if we haven't found all the chests
            if num_sonar_devices == 0:
                print(
                    "We've run out of sonar devices! Now we have to turn the ship around and head for home with treasure chests still out there! Game over."
                )
                print("\tThe remaining chests were here:")
                for row, col in board.chest_set:
                    print(f"\t{row}, {col}")

            # Ask if user want to play again
            if not (input("Do you want to play again? (y/n)?").strip().lower() == "y"):
                sys.exit()

    def __get_move(self, previous_move_set: set[tuple[int, int]]) -> tuple[int, int]:
        """Let player enter their move"""
        while True:
            move = input(
                "Where do you want to put the next sonar device?\n"
                + f"(0-{NUM_ROWS - 1} 0-{NUM_COLUMNS - 1}) (or type 'q' to quit): "
            ).strip()

            if move.lower() == "q":
                print("Thanks for playing!")
                sys.exit()

            try:
                row, col = map(int, move.split())
                if not Board.is_on_board(row, col):
                    raise ValueError
                if (row, col) in previous_move_set:
                    print("You already move there.")
                    continue
                return row, col

            except ValueError:
                print(
                    f"Enter a integer from 0 to {NUM_ROWS - 1}, a space, then a number from 0 to {NUM_COLUMNS - 1}."
                )
