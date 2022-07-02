import pytest
from src.puzzle import *

@pytest.mark.parametrize("size, puzzle, expected_result", [
    (3, [1, 2, 3, 8, 0, 4, 7, 6, 5], (4, [3, 5, 1, 7])),
    (3, [1, 2, 3, 4, 5, 6, 7, 8, 0], (8, [7, 5])),
])
def test_get_possible_position(size, puzzle, expected_result):
    assert get_possible_position(size, puzzle) == expected_result


@pytest.mark.parametrize("size, expected_result", [
    (3, [1, 2, 3, 8, 0, 4, 7, 6, 5]),
    (4, [1, 2, 3, 4, 12, 13, 14, 5, 11, 0, 15, 6, 10, 9, 8, 7])
])
def test_make_goal_snail(size, expected_result):
    print(make_goal_snail(4))
    assert make_goal_snail(size) == expected_result


@pytest.mark.parametrize("size, initial_puzzle, expected_result", [
    (3, [3, 2, 6, 1, 4, 0, 8, 7, 5], (3, 2, 6, 1, 4, 5, 8, 7, 0)),
])
def test_move_empty_to_last(size, initial_puzzle, expected_result):
    assert move_empty_to_last(size, initial_puzzle) == expected_result

@pytest.mark.parametrize("size, puzzle, expected_result", [
    (3, [1, 2, 3, 4, 5, 6, 7, 8, 0], 0),
    (3, [3, 2, 6, 1, 4, 0, 8, 7, 5], 9),
])
def test_get_inversion_count(size, puzzle, expected_result):
    assert get_inversion_count(size, puzzle) == expected_result


@pytest.mark.parametrize("size, puzzle, number, expected_result", [
    (3, [1, 2, 3, 4, 5, 6, 7, 8, 0], 0, (2, 2)),
    (3, [3, 2, 6, 1, 4, 0, 8, 7, 5], 1, (1, 0)),
])
def test_get_position(size, puzzle, number, expected_result):
    assert get_position(size, puzzle, number) == expected_result
