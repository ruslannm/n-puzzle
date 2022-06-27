from node import Node
from puzzle import EMPTY_TILE
from math import sqrt


def get_node_min_f(opened):
    nodes = [(puzzle, node) for puzzle, node in opened.items()]
    nodes.sort(key=lambda x: x[1].f)
    return nodes[0][0], nodes[0][1]


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

    def _recover_path(self, node):
        path_to_goal = [node]
        parent = node.predecessor
        while parent is not None:
            path_to_goal.append(parent)
            parent = parent.predecessor
        path_to_goal.reverse()
        return path_to_goal

    def _get_position(self, puzzle, number):
        position = puzzle.index(number)
        row = position % self._size
        col = position - row * self._size
        return row, col

    def _append_node(self, expand, node_predecessor, direction, zero_position, tile_position):
        node = Node(node_predecessor.puzzle,
                    last_move=direction,
                    depth=node_predecessor.depth + self._cost,
                    predecessor=node_predecessor)
        node.puzzle[zero_position], node.puzzle[tile_position] = node.puzzle[tile_position], node.puzzle[zero_position]
        expand.append((tuple(node.puzzle), node))

    def _get_expand(self, node):
        idx = node.puzzle.index(EMPTY_TILE)
        last_move = node.last_move
        expand = list()
        if idx % self._size > 0 and last_move != "r":
            self._append_node(expand, node, "l", idx, idx - 1)
        if idx % self._size < self._size - 1 and last_move != "l":
            self._append_node(expand, node, "r", idx, idx + 1)
        if idx / self._size > 0 and idx - self._size >= 0 and last_move != "d":
            self._append_node(expand, node, "u", idx, idx - self._size)
        if idx / self._size < self._size - 1 and last_move != "u":
            self._append_node(expand, node, "d", idx, idx + self._size)
        return expand

    def _manhattan_distance(self, puzzle):
        answer = 0
        for i in puzzle:
            if i > 0:
                row, col = self._get_position(self._goal, i)
                current_row, current_col = self._get_position(puzzle, i)
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
                row, col = self._get_position(self._goal, i)
                current_row, current_col = self._get_position(puzzle, i)
                answer += round(sqrt((col - current_col) ** 2 + (row - current_row) ** 2))
        return answer

    def _g(self, depth):
        return depth if self._uniform_cost else 0

    def _h(self, puzzle):
        return self._heuristic(puzzle) if self._greedy else 0

    def solve_astar(self):
        node = Node(self._initial_puzzle)
        opened = {tuple(node.puzzle): node}
        closed = dict()
        success = False
        total_number_opened = 1
        max_number_opened = 1
        path_to_goal = []
        while opened != dict() and not success:
            print(f"total_number_opened={total_number_opened}, max_number_opened={max_number_opened}")
            e_puzzle, e = get_node_min_f(opened)
            print(f"total_number_opened={total_number_opened}, max_number_opened={max_number_opened}, f={e.f}")
            if e_puzzle == self._goal:
                path_to_goal = self._recover_path(e)
                success = True
            else:
                del opened[e_puzzle]
                max_number_opened -= 1
                closed[e_puzzle] = e
                for s_puzzle, s in self._get_expand(e):
                    if s_puzzle not in opened and s_puzzle not in closed:
                        opened[s_puzzle] = s
                        s.g = self._g(e.depth) + self._cost
                        s.f = s.g + self._h(s.puzzle)
                        total_number_opened += 1
                        max_number_opened += 1
                    else:
                        if s.g > e.g + self._cost:
                            print("c")
                            if s_puzzle in closed:
                                del closed[s_puzzle]
                                opened[s_puzzle] = s
                                s.g = self._g(e.depth) + self._cost
                                s.f = s.g + self._h(s.puzzle)
                                total_number_opened += 1
                                max_number_opened += 1
        return success, total_number_opened, max_number_opened, path_to_goal
