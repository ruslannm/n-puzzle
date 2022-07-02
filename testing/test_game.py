import pytest
from src.game import *
from config import COST

EPSILON = 1e-3

@pytest.fixture()
def init_game():
    size = 3
    initial_puzzle = [3, 2, 6, 1, 4, 0, 8, 7, 5]
    goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    heuristic = "manhattan_distance"
    uniform = True
    greedy = True
    return Game(size, initial_puzzle, goal, COST, heuristic, uniform, greedy)


@pytest.mark.parametrize("puzzle, move, expected_result", [
    ([1, 2, 3, 8, 0, 4, 7, 6, 5], "r",
     [((1, 2, 3, 8, 4, 0, 7, 6, 5), "r"), ((1, 0, 3, 8, 2, 4, 7, 6, 5), "u"), ((1, 2, 3, 8, 6, 4, 7, 0, 5), "d")]),
    ([1, 2, 3, 8, 0, 4, 7, 6, 5], "u",
     [((1, 2, 3, 0, 8, 4, 7, 6, 5), "l"), ((1, 2, 3, 8, 4, 0, 7, 6, 5), "r"), ((1, 0, 3, 8, 2, 4, 7, 6, 5), "u")]),
    ([0, 2, 3, 8, 1, 4, 7, 6, 5], "u",
     [((2, 0, 3, 8, 1, 4, 7, 6, 5), "r")])
])
def test_Game_get_expand(init_game, puzzle, move, expected_result):
    assert init_game._get_expand(puzzle, move) == expected_result


@pytest.mark.parametrize("value, expected_result", [
    (1, 1), (5, 5), (0, 0)
])
def test_g(init_game, value, expected_result):
    assert init_game._g(value) == expected_result


@pytest.mark.parametrize("value, expected_result", [
    (1, 0), (5, 0), (0, 0)
])
def test_g_0(init_game, value, expected_result):
    init_game._uniform_cost = False
    assert init_game._g(value) == expected_result


@pytest.mark.parametrize("puzzle, expected_result", [
    ([1, 2, 3, 8, 0, 8, 7, 6, 5], 0),
    ([2, 1, 3, 8, 0, 8, 7, 6, 5], 2),
    ([2, 1, 3, 8, 5, 8, 7, 6, 0], 4),
])
def test_manhattan_distance(init_game, puzzle, expected_result):
    assert init_game._manhattan_distance(puzzle) == expected_result


@pytest.mark.parametrize("puzzle, expected_result", [
    ([1, 2, 3, 8, 0, 8, 7, 6, 5], 0),
    ([2, 1, 3, 8, 0, 8, 7, 6, 5], 2),
    ([2, 1, 3, 8, 5, 8, 7, 6, 0], 3),
])
def test_hamming_distance(init_game, puzzle, expected_result):
    assert init_game._hamming_distance(puzzle) == expected_result


@pytest.mark.parametrize("puzzle, expected_result", [
    ([1, 2, 3, 8, 0, 8, 7, 6, 5], 0),
    ([2, 1, 3, 8, 0, 8, 7, 6, 5], 2),
    ([2, 1, 3, 8, 5, 8, 7, 6, 0], 3.414),
])
def test_euclidian_distance(init_game, puzzle, expected_result):
    assert abs(init_game._euclidian_distance(puzzle) - expected_result) < EPSILON
