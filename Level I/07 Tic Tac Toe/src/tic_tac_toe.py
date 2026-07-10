import random


class TicTacToe:

    def __init__(self):
        self.board = [" "] * 10  # list(map(str, range(10)))
        self.player_turn = self.random_player_tur()

    def random_player_tur(self) -> str:
        return random.choice(["X", "O"])

    def show_board(self) -> None:
        print("\n")
        print(self.board[1] + "|" + self.board[2] + "|" + self.board[3])
        print("-----")
        print(self.board[4] + "|" + self.board[5] + "|" + self.board[6])
        print("-----")
        print(self.board[7] + "|" + self.board[8] + "|" + self.board[9])
        print("\n")

    def swap_player_turn(self) -> str:
        self.player_turn = "X" if self.player_turn == "O" else "O"
        return self.player_turn

    def is_board_filled(self) -> bool:
        return " " not in self.board[1:]

    def fix_spot(self, cell: int, player: str) -> None:
        self.board[cell] = player

    def has_player_won(self, player: str) -> bool:
        win_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]
        ]
        for combination in win_combinations:
            if all([self.board[cell] == player for cell in combination]):
                return True
        return False

    def start(self) -> None:
        while True:
            situation = input(
                "Enter S to play and enter q for exit : ").lower()
            if situation == "s":
                while True:
                    self.show_board()
                    print(f"Player {self.player_turn} turn! \n")
                    cell = int(input("Enter cell number from 1 to 9: "))
                    if self.board[cell] == " " and cell in range(1, 10):
                        self.fix_spot(cell=cell, player=self.player_turn)

                        if self.has_player_won(self.player_turn):
                            self.show_board()
                            print(f"player {self.player_turn} won !!\n")
                            break

                        if self.is_board_filled():
                            print("Draw !!\n")
                            break

                        self.swap_player_turn()
                    else:
                        print("Invalid cell number !!")
            elif situation == "q":
                break


if __name__ == "__main__":
    game = TicTacToe()
    game.start()
