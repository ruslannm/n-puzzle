from time import perf_counter
from src.parse import get_input, validate_args
from src.puzzle import make_goal_snail, is_solvable, pretty_print
from src.game import Game
from config import COST, RESULT


if __name__ == "__main__":
    args = get_input()
    data = validate_args(args)
    if not data:
        exit(-1)
    size, initial_puzzle, uniform, greedy, heuristic, time, unsolvable, iteration, attempt, file = data
    goal = tuple(make_goal_snail(size))
    if file:
        print(f"Puzzle was got from {file}")
    else:
        print(f"Puzzle with size {size} was generated with {iteration} iterations", ", and made unsolvable." if unsolvable else ".", sep="")
    pretty_print(0, size, initial_puzzle)
    puzzle_solvable = is_solvable(size, initial_puzzle, goal)
    if not puzzle_solvable:
        print(f"{RESULT['puzzle_solvable']}: {puzzle_solvable}")
        if not attempt:
            exit()
    game = Game(size, initial_puzzle, goal, COST, heuristic, uniform, greedy)
    t_start = perf_counter()
    success, total_number_opened, max_number_opened, path_to_goal = game.solve_a_star()
    t_work = perf_counter() - t_start
    print(f"{RESULT['success']}: {success}")
    print(f"{RESULT['total_number_opened']}: {total_number_opened}")
    print(f"{RESULT['max_number_opened']}: {max_number_opened}")
    if len(path_to_goal) > 0:
        print(f"{RESULT['len(path_to_goal)']}: {len(path_to_goal) - 1}")
    if time:
        print(f"{RESULT['t_work']}: {t_work:.3f} seconds")
    offset = 7
    for ind, puzzle in enumerate(path_to_goal):
        if ind > 0:
            print(f"Step: {ind:>3}.")
            pretty_print(10, size, puzzle)
