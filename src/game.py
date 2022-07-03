from itertools import count
from heapq import heappush, heappop
from config import EMPTY_TILE, COST_EUCLIDIAN_DISTANCE
from src.puzzle import get_possible_position
from math import sqrt


def position_by_index(size):
    d = {}
    for i in range(size * size):
        row = i // size
        col = i % size
        d[i] = (row, col)
    return d


class Game:
    def __init__(self, size: int, initial_puzzle: list, goal: list, cost: int, heuristic: str, uniform_cost: bool,
                 greedy: bool):
        self._size = size
        self._total_size = size * size
        self._initial_puzzle = [i for i in initial_puzzle]
        self._goal = goal
        if heuristic not in ("manhattan_distance", "euclidian_distance", "hamming_distance"):
            raise Exception("Unknown heuristic function")
        self._cost = COST_EUCLIDIAN_DISTANCE if heuristic == "euclidian_distance" else cost
        self._heuristic = heuristic
        self._hash_heuristic = self._hash_distance()
        self._uniform_cost = uniform_cost
        self._greedy = greedy

    def _get_expand(self, puzzle, prev_empty):

        def swap_tile(i, j):
            tmp = list(puzzle)
            tmp[i], tmp[j] = tmp[j], tmp[i]
            return tuple(tmp)

        empty = puzzle.index(EMPTY_TILE)
        possible = get_possible_position(self._size, self._total_size, empty)
        expand = list()
        for next_empty in possible:
            if next_empty != prev_empty:
                expand.append((swap_tile(empty, next_empty), empty))
        return expand

    def _hash_distance(self):
        d = position_by_index(self._size)
        h_hash = dict()
        for i in range(self._total_size - 1):
            i_row, i_col = d[i]
            for j in range(i + 1, self._total_size):
                j_row, j_col = d[j]
                if self._heuristic == "manhattan_distance":
                    tmp = abs(i_col - j_col) + abs(i_row - j_row)
                elif self._heuristic == "euclidian_distance":
                    tmp = round(sqrt((i_col - j_col) ** 2 + (i_row - j_row) ** 2) * self._cost)
                elif self._heuristic == "hamming_distance":
                    tmp = 1
                else:
                    tmp = 0
                h_hash[(i, j)] = tmp
                h_hash[(j, i)] = tmp
        for i in range(self._total_size):
            h_hash[(i, i)] = 0
        return h_hash

    def _h(self, puzzle):
        if self._greedy:
            return sum(
                [self._hash_heuristic[(self._goal.index(i), i_puzzle)] for i_puzzle, i in enumerate(puzzle) if i > 0])
        else:
            return 0

    def solve_a_star(self):
        counter = count()
        queue = [(0, next(counter), tuple(self._initial_puzzle), 0, -1, None)]
        opened = set()
        opened.add(tuple(self._initial_puzzle))
        closed = dict()
        success = False
        max_number_opened = 1
        cur_number_opened = 1
        path_to_goal = []
        while queue and not success:
            _, _, e, e_g, e_prev_empty, e_parent = heappop(queue)
            if e == self._goal:
                path_to_goal = [e]
                while e_parent is not None:
                    path_to_goal.append(e_parent)
                    e_parent = closed.get(e_parent, None)
                path_to_goal.reverse()
                success = True
            else:
                opened.remove(e)
                cur_number_opened -= 1
                closed[e] = e_parent
                next_g = e_g + self._cost if self._uniform_cost else 0
                for s, s_empty in self._get_expand(e, e_prev_empty):
                    if s in closed or s in opened:
                        continue
                    next_h = self._h(s)
                    opened.add(s)
                    heappush(queue, (next_g + next_h, next(counter), s, next_g, s_empty, e))
                    cur_number_opened += 1
                    if cur_number_opened > max_number_opened:
                        max_number_opened = cur_number_opened
        return success, next(counter), max_number_opened, path_to_goal
