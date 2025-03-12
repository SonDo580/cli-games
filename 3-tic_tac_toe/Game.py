import random
from typing import Literal

from constants import SIZE, MAX_TURN
from Checker import Checker
from Board import Board


class Game:
    def __get_marks(self) -> Literal["O", "X"]:
        while True:
            player_mark = input("Do you want to be X or O? ").upper()
            if player_mark == "X":
                computer_mark = "O"
            elif player_mark == "O":
                computer_mark = "X"
            else:
                print("Please enter X or O!")
                continue
            return (player_mark, computer_mark)

    def __computer_move(
        self, board: list[list[str]], computer_mark: Literal["O", "X"], turn_num: int
    ) -> tuple[bool, int]:
        while True:
            row = random.randint(0, SIZE - 1)
            col = random.randint(0, SIZE - 1)
            if board[row][col] == " ":
                board[row][col] = computer_mark
                turn_num += 1
                return (Checker.check_board(board, computer_mark, row, col), turn_num)

    def __player_move(
        self, board: list[list[str]], player_mark: Literal["O", "X"], turn_num: int
    ) -> tuple[bool, int]:
        print("What is your next move?")
        while True:
            try:
                row = int(input(f"Enter row index (0-{SIZE-1}): "))
                col = int(input(f"Enter column index (0-{SIZE-1}): "))

                if not Board.is_on_board(row, col):
                    print("Please choose indices in allowed range!")
                    continue

                if board[row][col] != " ":
                    print("Cell occupied! Please choose another one!")
                    continue

                board[row][col] = player_mark
                turn_num += 1
                return (Checker.check_board(board, player_mark, row, col), turn_num)

            except ValueError:
                print("Please enter an integer!")

    def __turn(
        self,
        board: list[list[str]],
        computer_mark: Literal["O", "X"],
        player_mark: Literal["O", "X"],
        turn_num: int,
    ) -> tuple[bool, bool, int]:
        computer_win, turn_num = self.__computer_move(board, computer_mark, turn_num)
        Board.draw(board)
        if computer_win or turn_num == MAX_TURN:
            return (computer_win, False, turn_num)

        player_win, turn_num = self.__player_move(board, player_mark, turn_num)
        Board.draw(board)
        return (computer_win, player_win, turn_num)

    def __round(self):
        board = Board.create()
        turn_num = 0
        player_mark, computer_mark = self.__get_marks()
        print("The computer will go first.")

        computer_win = False
        player_win = False
        while (not computer_win) and (not player_win) and (turn_num < MAX_TURN):
            computer_win, player_win, turn_num = self.__turn(
                board, computer_mark, player_mark, turn_num
            )

        self.__print_result(computer_win, player_win)

    def __print_result(self, computer_win: bool, player_win: bool) -> None:
        if computer_win:
            print("You lost!")
        elif player_win:
            print("You won!")
        else:
            print("Tie")

    def __play_again(self) -> bool:
        while True:
            answer = input("Press 'y' to play again, 'n' to cancel: ").lower()
            if answer == "y":
                return True
            elif answer == "n":
                return False

    def loop(self) -> None:
        print("Welcome to Tic-Tac-Toe!")
        while True:
            self.__round()
            if not self.__play_again():
                return
