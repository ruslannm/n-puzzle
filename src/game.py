from src.puzzle import EMPTY_TILE, get_position
from math import sqrt
from itertools import count
from heapq import heappush, heappop


class Game:
    def __init__(self, size, initial_puzzle, goal, cost, heuristic="manhattan_distance", uniform_cost=True,
                 greedy=True):
        self._size = size
        self._initial_puzzle = [i for i in initial_puzzle]
        self._goal = goal
        self._cost = cost
        heuristic_dict = {"manhattan_distance": self._manhattan_distance,
                          "euclidian_distance": self._euclidian_distance,
                          "hamming_distance": self._hamming_distance}
        if heuristic not in heuristic_dict:
            raise Exception("Unknown heuristic function")
        self._heuristic = heuristic_dict.get(heuristic)
        self._uniform_cost = uniform_cost
        self._greedy = greedy

    def _get_expand(self, puzzle, move):

        def swap_tile(i, j):
            tmp = list(puzzle)
            tmp[i], tmp[j] = tmp[j], tmp[i]
            return tuple(tmp)

        idx = puzzle.index(EMPTY_TILE)
        s = self._size
        expand = list()
        if idx % s > 0 and move != "r":
            expand.append((swap_tile(idx, idx - 1), "l"))
        if idx % s < s - 1 and move != "l":
            expand.append((swap_tile(idx, idx + 1), "r"))
        if idx - s >= 0 and move != "d":
            expand.append((swap_tile(idx, idx - s), "u"))
        if idx + s < len(puzzle) and move != "u":
            expand.append((swap_tile(idx, idx + s), "d"))
        return expand

    def _manhattan_distance(self, puzzle):
        answer = 0
        for i in puzzle:
            if i > 0:
                row, col = get_position(self._size, self._goal, i)
                current_row, current_col = get_position(self._size, puzzle, i)
                answer += abs(col - current_col) + abs(row - current_row)
        return answer

    def _hamming_distance(self, puzzle):
        answer = 0
        for i in puzzle:
            if i > 0:
                answer += 1 if puzzle.index(i) != self._goal.index(i) else 0
        return answer

    def _euclidian_distance(self, puzzle):
        answer = 0
        for i in puzzle:
            if i > 0:
                row, col = get_position(self._size, self._goal, i)
                current_row, current_col = get_position(self._size, puzzle, i)
                answer += round(sqrt((col - current_col) ** 2 + (row - current_row) ** 2))
        return answer

    def _g(self, value):
        return value if self._uniform_cost else 0

    def _h(self, puzzle):
        return self._heuristic(puzzle) if self._greedy else 0

    def solve_a_star(self):
        counter = count()
        queue = [(0, next(counter), tuple(self._initial_puzzle), 0, "", None)]
        opened = set()
        opened.add(tuple(self._initial_puzzle))
        closed = dict()
        success = False
        total_number_opened = 1
        max_number_opened = 1
        path_to_goal = []
        while queue and not success:
            _, _, e, e_g, e_move, e_parent = heappop(queue)
            if e == self._goal:
                path_to_goal = [e]
                while e_parent is not None:
                    path_to_goal.append(e_parent)
                    e_parent = closed.get(e_parent, None)
                path_to_goal.reverse()
                success = True
            else:
                opened.remove(e)
                max_number_opened -= 1
                closed[e] = e_parent
                next_g = self._g(e_g) + self._g(self._cost)
                for s, s_move in self._get_expand(e, e_move):
                    if s not in opened and s not in closed:
                        next_f = self._h(s)
                        opened.add(s)
                        heappush(queue, (next_g + next_f, next(counter), s, next_g, s_move, e))
                        total_number_opened += 1
                        max_number_opened += 1
                    else:
                        if next_g > e_g + self._g(self._cost):
                            print("c")
        return success, total_number_opened, max_number_opened, path_to_goal
