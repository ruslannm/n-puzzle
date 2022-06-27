import random

RANDOM_SEED = 21
EMPTY_TILE = 0

def make_puzzle(s, solvable, iterations):
    def swap_empty(p):
        idx = p.index(EMPTY_TILE)
        poss = []
        if idx % s > 0:
            poss.append(idx - 1)
        if idx % s < s - 1:
            poss.append(idx + 1)
        if idx - s >= 0:
            poss.append(idx - s)
        if idx + s < len(p):
            poss.append(idx + s)
        swi = random.choice(poss)
        p[idx] = p[swi]
        p[swi] = EMPTY_TILE

    p = make_goal_snail(s)
    random.seed(RANDOM_SEED)
    for i in range(iterations):
        swap_empty(p)

    if not solvable:
        if p[EMPTY_TILE] == EMPTY_TILE or p[1] == EMPTY_TILE:
            p[-1], p[-2] = p[-2], p[-1]
        else:
            p[EMPTY_TILE], p[1] = p[1], p[EMPTY_TILE]
    return p


def make_goal_snail(size: int):
    puzzle = [[0 for _ in range(size)] for _ in range(size)]
    moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
    total_size = size * size
    i = 1
    row = 0
    col = 0
    size -= 1
    while i < total_size and size > 0:
        for move in moves:
            for _ in range(size):
                if i == total_size:
                    break
                puzzle[row][col] = i
                row += move[0]
                col += move[1]
                i += 1
        row += 1
        col += 1
        size -= 2
    return [i for row in puzzle for i in row]


def make_goal_empty_last(size):
    puzzle = [i for i in range(1, size * size)]
    puzzle.append(EMPTY_TILE)
    return puzzle


def get_inversion_count(size, puzzle):
    total_size = size * size
    inversion_count = 0
    for i in range(total_size - 1):
        for j in range(i + 1, total_size):
            if puzzle[j] != EMPTY_TILE and puzzle[i] != EMPTY_TILE and puzzle[i] > puzzle[j]:
                inversion_count += 1
    return inversion_count


def get_empty_tile_row(size, puzzle):
    return size - puzzle.index(EMPTY_TILE) // size


def get_position(size, puzzle, number):
    position = puzzle.index(number)
    row = position // size
    col = position - row * size
    return row, col


def move_empty_to_last(size, initial_puzzle):
    p = list(initial_puzzle)
    row, col = get_position(size, p, EMPTY_TILE)
    idx = p.index(EMPTY_TILE)
    while row < size - 1:
        p[idx], p[idx + size] = p[idx + size],  EMPTY_TILE
        row += 1
        idx += size
    while col < size - 1:
        p[idx], p[idx + 1] = p[idx + 1],  EMPTY_TILE
        col += 1
        idx += 1
    return tuple(p)


def is_solvable(size, initial_puzzle, goal):
    mapping = {key: value for key, value in zip(move_empty_to_last(size, goal), make_goal_empty_last(size))}
    puzzle = [mapping[i] for i in initial_puzzle]
    pretty_print(0, size, puzzle)
    inversion_count = get_inversion_count(size, puzzle)
    if size & 1:
        return not (inversion_count & 1)
    else:
        pos = get_empty_tile_row(size, puzzle)
        if pos & 1:
            return not (inversion_count & 1)
        else:
            return inversion_count & 1


def pretty_print(offset, size, puzzle):
    space = 4
    for row in range(size):
        if size < 11:
            print(" " * offset, "".join([f"{puzzle[col + row * size]:>3}" for col in range(size)]))
        elif size < 33:
            print(" " * offset, "".join([f"{puzzle[col + row * size]:>4}" for col in range(size)]))
        else:
            print(" " * offset, "".join([f"{puzzle[col + row * size]:>5}" for col in range(size)]))
