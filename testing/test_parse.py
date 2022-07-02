import pytest
from src.parse import *


@pytest.mark.parametrize("line, expected_result", [
    ("3 0 5", "3 0 5"),
    ("3 0 5# c", "3 0 5"),
    ("3 0 5 100 # 10", "3 0 5 100 "),
])
def test_clear(line, expected_result):
    assert clear(line) == expected_result


@pytest.mark.parametrize("file, expected_result", [
    ("./testing/valid_files/npuzzle-3-1.txt", (3, [3, 2, 6, 1, 4, 0, 8, 7, 5])),
    ("./testing/valid_files/npuzzle-4-1.txt", (4, [0, 10, 5, 7, 11, 14, 4, 8, 1, 2, 6, 13, 12, 3, 15, 9])),
    ("./testing/valid_files/npuzzle-4-2.txt", (4, [0, 10, 5, 7, 11, 14, 4, 8, 1, 2, 6, 13, 12, 3, 15, 9])),
])
def test_read_valid_file(file, expected_result):
    assert read_file(file) == expected_result


@pytest.mark.parametrize("file, expected_result", [
    ("./testing/invalid_files/npuzzle-3-1.txt", (0, None)),
    ("./testing/invalid_files/npuzzle-3-2.txt", (0, None)),
    ("./testing/invalid_files/npuzzle-3-3.txt", (0, None)),
    ("./testing/invalid_files/npuzzle-3-4.txt", (0, None)),
    ("./testing/invalid_files/npuzzle-3-5.txt", (0, None)),
    ("./testing/invalid_files/npuzzle-4-1.txt", (0, None)),
    ("./testing/invalid_files/npuzzle-4-2.txt", (0, None)),
])
def test_read_invalid_file(file, expected_result):
    assert read_file(file) == expected_result
