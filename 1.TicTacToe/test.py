import pytest

from tictactoe import TicTac


@pytest.fixture
def game():
    return TicTac()


validation_cases = [
    ("test_string", "Input must be board coordinate"),
    ("10", "Coordinate must be in range [0..8]"),
    ("0", "Place 0 is taken"),
]


@pytest.mark.parametrize("inp,expected_msg", validation_cases)
def test_validation(game, inp, expected_msg):
    game.board[0] = "X"
    msg = game.validate_input(inp)
    assert msg == expected_msg


game_cases = [
    ([0, 1], False),
    ([1, 0, 3, 2, 4, 5, 6, 7, 8], "Friendship"),
    ([0, 8, 1, 6, 2], "X"),
    ([0, 8, 3, 4, 6], "X"),
    ([0, 6, 4, 2, 8], "X"),
    ([0, 2, 6, 5, 7, 8], "O"),
    ([0, 6, 5, 7, 4, 8], "O"),
    ([0, 2, 8, 4, 5, 6], "O"),
]

game_cases_ids = [
    "not finished",
    "draw",
    "x wins column",
    "x wins rows",
    "x wins diagonals",
    "o wins column",
    "o wins rows",
    "o wins diagonals",
]


@pytest.mark.parametrize("turns,won", game_cases, ids=game_cases_ids)
def test_game(game, monkeypatch, turns, won):
    for coordinate in turns:
        monkeypatch.setattr("builtins.input", lambda _: str(coordinate))
        game.turn()

    assert game.check_winner() == won
