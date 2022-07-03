import pytest
from src.game import *
from config import COST

@pytest.fixture()
def init_game():
    size = 3
    initial_puzzle = [3, 2, 6, 1, 4, 0, 8, 7, 5]
    goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    heuristic = "manhattan_distance"
    uniform = True
    greedy = True
    return Game(size, initial_puzzle, goal, COST, heuristic, uniform, greedy)


@pytest.mark.parametrize("puzzle, prev_empty, expected_result", [
    ([1, 2, 3, 8, 0, 4, 7, 6, 5], 3,
     [((1, 2, 3, 8, 4, 0, 7, 6, 5), 4), ((1, 0, 3, 8, 2, 4, 7, 6, 5), 4), ((1, 2, 3, 8, 6, 4, 7, 0, 5), 4)]),
    ([1, 2, 3, 8, 0, 4, 7, 6, 5], 7,
     [((1, 2, 3, 0, 8, 4, 7, 6, 5), 4), ((1, 2, 3, 8, 4, 0, 7, 6, 5), 4), ((1, 0, 3, 8, 2, 4, 7, 6, 5), 4)]),
    ([0, 2, 3, 8, 1, 4, 7, 6, 5], 3,
     [((2, 0, 3, 8, 1, 4, 7, 6, 5), 0)])
])
def test_Game_get_expand(init_game, puzzle, prev_empty, expected_result):
    assert init_game._get_expand(puzzle, prev_empty) == expected_result
