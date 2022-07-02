from src.puzzle import get_position
from math import sqrt


def manhattan_distance(size, puzzle, goal):
    answer = 0
    for i in puzzle:
        if i > 0:
            row, col = get_position(size, goal, i)
            current_row, current_col = get_position(size, puzzle, i)
            answer += abs(col - current_col) + abs(row - current_row)
    return answer


def hamming_distance(puzzle, goal):
    answer = 0
    for i in puzzle:
        if i > 0:
            answer += 1 if puzzle.index(i) != goal.index(i) else 0
    return answer


def euclidian_distance(size, puzzle, goal):
    answer = 0
    for i in puzzle:
        if i > 0:
            row, col = get_position(size, goal, i)
            current_row, current_col = get_position(size, puzzle, i)
            answer += sqrt((col - current_col) ** 2 + (row - current_row) ** 2)
    return answer


HEURISTIC = {"manhattan_distance": manhattan_distance,
             "euclidian_distance": euclidian_distance,
             "hamming_distance": hamming_distance}
