COST = 1
COMMENT = "#"
EMPTY_TILE = 0
SIZE = 3
ERROR_MESSAGE_SIZE = f"Acceptable value for generate puzzle: {SIZE} <= size"
ITERATION = 1
ERROR_MESSAGE_ITERATION = f"Acceptable value for generate puzzle: {ITERATION} <= iteration"
RANDOM_SEED = 21
HEURISTIC = ("manhattan_distance", "euclidian_distance", "hamming_distance")
HEURISTIC_DEFAULT = "manhattan_distance"
RESULT = {"success": "Success result",
          "total_number_opened": "Complexity in time",
          "max_number_opened": "Complexity in size",
          "len(path_to_goal)": "Number of moves",
          "path_to_goal": "Path to the final state",
          "t_work": "Working time",
          "puzzle_solvable": "Possibility of a solution without searching"}
