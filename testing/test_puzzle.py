import pytest
from src.puzzle import make_goal_snail


@pytest.mark.parametrize("size, expected_result", [
    (3, [1, 2, 3, 8, 0, 4, 7, 6, 5]),
    (4, [1, 2, 3, 4, 12, 13, 14, 5, 11, 0, 15, 6, 10, 9, 8, 7])
])
def test_make_goal_snail(size, expected_result):
    print(make_goal_snail(4))
    assert make_goal_snail(size) == expected_result
