import typing as t


class TicTac:
    author: str = "Kirill Denisov"

    def __init__(self) -> None:
        self.current_symbol: str = "X"
        self.board: list[t.Union[int, str]] = list(range(9))

    @property
    def columns(self) -> list[list[int]]:
        res = []
        for column_coord in range(3):
            column_coords = [column_coord + i * 3 for i in range(3)]
            res.append(column_coords)
        return res

    @property
    def rows(self) -> list[list[int]]:
        res = []
        for row_coord in range(0, 7, 3):
            row_coords = [row_coord + i for i in range(3)]
            res.append(row_coords)
        return res

    @property
    def diagonals(self) -> list[list[int]]:
        diag_coords1 = [(i * 4) for i in range(3)]
        diag_coords2 = [(i * 2) + 2 for i in range(3)]
        return [diag_coords1, diag_coords2]

    def switch_current_symbol(self) -> None:
        if self.current_symbol == "X":
            self.current_symbol = "O"
        else:
            self.current_symbol = "X"

    def show_board(self) -> None:
        for i, cell in enumerate(self.board):
            print(cell, end=" ")
            if (i + 1) % 3 == 0:
                print()
        print()

    def validate_input(self, inp: str) -> t.Union[str, bool]:
        if not inp.isnumeric():
            return "Input must be board coordinate"
        if (int_inp := int(inp)) > 8:
            return "Coordinate must be in range [0..8]"
        if isinstance(self.board[int_inp], str):
            return f"Place {int_inp} is taken"
        return False

    def validate_input_loop(self) -> int:
        while True:
            inp = input(f"{self.current_symbol}! Choose your next move!: ")
            if validation_message := self.validate_input(inp):
                print(validation_message)
            else:
                break
        return int(inp)

    def check_symbol_in_coords(self, symbol: str, coords: list[int]) -> bool:
        for i in coords:
            if self.board[i] != symbol:
                return False
        return True

    def check_if_won(self, symbol: str) -> bool:
        for coord_set in [self.columns, self.rows, self.diagonals]:
            for wining_combination_coords in coord_set:
                if self.check_symbol_in_coords(symbol, wining_combination_coords):
                    return True
        return False

    def check_draw(self) -> bool:
        for elem in self.board:
            if isinstance(elem, int):
                return False
        return True

    def check_winner(self) -> t.Union[str, bool]:
        if self.check_if_won("X"):
            return "X"
        if self.check_if_won("O"):
            return "O"
        if self.check_draw():
            return "Friendship"
        return False

    def turn(self) -> bool:
        self.show_board()

        coordinate = self.validate_input_loop()
        self.board[coordinate] = self.current_symbol
        self.switch_current_symbol()

        if winner := self.check_winner():
            print(f"{winner} won!")
            return True
        return False

    def start_game(self) -> None:
        print(f"Welcome to TicTac game by {self.author}")

        while True:
            if self.turn():
                break


if __name__ == "__main__":
    game = TicTac()
    game.start_game()
