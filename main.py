from time import perf_counter
from src.parse import get_input
from src.puzzle import make_goal_snail, is_solvable, pretty_print
from src.game import Game

COST = 1

if __name__ == "__main__":
    size, initial_puzzle, uniform, greedy, heuristic, time = get_input()
    goal = tuple(make_goal_snail(size))
    puzzle_solvable = is_solvable(size, initial_puzzle, goal)
    print(f"This puzzle is {'solvable' if puzzle_solvable else 'unsolvable'}")
    pretty_print(0, size, initial_puzzle)
    heuristic = "manhattan_distance"
    game = Game(size, initial_puzzle, goal, COST, heuristic, uniform, greedy)
    t_start = perf_counter()
    success, total_number_opened, max_number_opened, path_to_goal = game.solve_a_star()
    t_work = perf_counter() - t_start
    print(f"Complexity in time: {total_number_opened}")
    print(f"Complexity in size: {max_number_opened}")
    print(f"Number of moves: {len(path_to_goal) - 1}")
    if time:
        print(f"Working time: {t_work:.3f} seconds")
    offset = 7
    for ind, puzzle in enumerate(path_to_goal):
        if ind > 0:
            print(f"Step: {ind:>3}.")
            pretty_print(10, size, puzzle)
