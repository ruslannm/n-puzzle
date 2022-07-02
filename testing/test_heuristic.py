import pytest
from src.heuristic import *

EPSILON = 1e-3


@pytest.mark.parametrize("size, puzzle, goal, expected_result", [
    (3, [1, 2, 3, 4, 5, 6, 7, 8, 0], [1, 2, 3, 4, 5, 6, 7, 8, 0], 0),
    (3, [1, 2, 3, 4, 5, 6, 7, 8, 0], [2, 1, 3, 4, 5, 6, 7, 8, 0], 2),
    (3, [1, 2, 3, 4, 5, 6, 7, 8, 0], [2, 1, 3, 4, 0, 6, 7, 8, 5], 4),
])
def test_manhattan_distance(size, puzzle, goal, expected_result):
    assert manhattan_distance(size, puzzle, goal) == expected_result


@pytest.mark.parametrize("puzzle, goal, expected_result", [
    ([1, 2, 3, 4, 5, 6, 7, 8, 0], [1, 2, 3, 4, 5, 6, 7, 8, 0], 0),
    ([1, 2, 3, 4, 5, 6, 7, 8, 0], [2, 1, 3, 4, 5, 6, 7, 8, 0], 2),
    ([1, 2, 3, 4, 5, 6, 7, 8, 0], [2, 1, 3, 4, 0, 6, 7, 8, 5], 3),
])
def test_hamming_distance(puzzle, goal, expected_result):
    assert hamming_distance(puzzle, goal) == expected_result


@pytest.mark.parametrize("size, puzzle, goal, expected_result", [
    (3, [1, 2, 3, 4, 5, 6, 7, 8, 0], [1, 2, 3, 4, 5, 6, 7, 8, 0], 0),
    (3, [1, 2, 3, 4, 5, 6, 7, 8, 0], [2, 1, 3, 4, 5, 6, 7, 8, 0], 2),
    (3, [1, 2, 3, 4, 5, 6, 7, 8, 0], [2, 1, 3, 4, 0, 6, 7, 8, 5], 3.414),
])
def test_euclidian_distance(size, puzzle, goal, expected_result):
    print(euclidian_distance(size, puzzle, goal))
    assert abs(euclidian_distance(size, puzzle, goal) - expected_result) < EPSILON
