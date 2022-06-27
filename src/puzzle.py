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
        if idx / s > 0 and idx - s >= 0:
            poss.append(idx - s)
        if idx / s < s - 1:
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


def make_goal_snail(s: int):
    ts = s * s
    puzzle = [-1 for i in range(ts)]
    cur = 1
    x = 0
    ix = 1
    y = 0
    iy = 0
    while True:
        puzzle[x + y * s] = cur
        if cur == 0:
            break
        cur += 1
        if x + ix == s or x + ix < 0 or (ix != 0 and puzzle[x + ix + y * s] != -1):
            iy = ix
            ix = 0
        elif y + iy == s or y + iy < 0 or (iy != 0 and puzzle[x + (y + iy) * s] != -1):
            ix = -iy
            iy = 0
        x += ix
        y += iy
        if cur == s * s:
            cur = 0
    return puzzle


def make_goal_empty_tile_last(size):
    puzzle = []
    for i in range(1, size * size):
        puzzle.append(i)
    puzzle.append(EMPTY_TILE)
    return puzzle


def get_inversion_count(size, puzzle):
    inversion_count = 0
    for i in range(size * size - 1):
        for j in range(i + 1, size * size):
            if puzzle[j] and puzzle[i] and puzzle[i] > puzzle[j]:
                inversion_count += 1
    return inversion_count


def get_empty_tile_row(size, puzzle):
    return size - puzzle.index(EMPTY_TILE) // size


def is_solvable(size, initial_puzzle, goal):
    mapping = {key: value for key, value in zip(goal, make_goal_empty_tile_last(size))}
    puzzle = [mapping[i] for i in initial_puzzle]
    inversion_count = get_inversion_count(size, puzzle)
    if size & 1:
        return not (inversion_count & 1)
    else:
        pos = get_empty_tile_row(size, puzzle)
        if pos & 1:
            return not (inversion_count & 1)
        else:
            return inversion_count & 1