import re, argparse
from src.puzzle import make_puzzle
from config import COMMENT, SIZE, ITERATION, ERROR_MESSAGE_SIZE, ERROR_MESSAGE_ITERATION, HEURISTIC, HEURISTIC_DEFAULT


def clear(s):
    comment = s.find(COMMENT)
    if comment != -1:
        return s[:comment]
    else:
        return s


def read_file(file):
    size = 0
    puzzle = []
    try:
        with open(file, "r", encoding='utf-8') as f:
            data = f.read()
            ds, i = data.split("\n"), 0
            for line in ds:
                line = clear(line)
                if len(line) == 0:
                    continue
                if i == 0:
                    if line[0] == " " or not line.strip().isdigit():
                        raise ValueError()
                    size = int(line)
                else:
                    row = re.sub(r"\s+", ' ', line).strip().split()
                    if len(row) != size:
                        raise ValueError()
                    puzzle += list(map(int, row))
                i += 1
            if i != size + 1:
                raise ValueError()
    except:
        print("Error reading file")
        return 0, None
    for i in range(size * size):
        if i in puzzle:
            continue
        else:
            print("Error in set")
            return 0, None
    return size, puzzle


def validate_args(args: dict):
    file = args.get("file", None)
    if file:
        size, puzzle = read_file(file)
        if size < SIZE:
            print(ERROR_MESSAGE_SIZE)
            return None
    else:
        size = args["size"]
        puzzle = make_puzzle(size, args["unsolvable"], args['iteration'])
    uniform = args['uniform']
    greedy = args['greedy']
    if not (uniform or greedy):
        uniform, greedy = True, True
    return size, puzzle, uniform, greedy, args['heuristic'], args['time'], args["unsolvable"], args['iteration'], args[
        'attempt'], file


def check_size(value):
    if not value.isdigit():
        raise argparse.ArgumentTypeError(ERROR_MESSAGE_SIZE)
    value = int(value)
    if value < SIZE:
        raise argparse.ArgumentTypeError(ERROR_MESSAGE_SIZE)
    return value


def check_iteration(value):
    if not value.isdigit():
        raise argparse.ArgumentTypeError(ERROR_MESSAGE_ITERATION)
    value = int(value)
    if value < ITERATION:
        raise argparse.ArgumentTypeError(ERROR_MESSAGE_ITERATION)
    return value


def get_input():
    parser = argparse.ArgumentParser()
    group_input = parser.add_mutually_exclusive_group()
    group_input.add_argument("-f", "--file", metavar="file", help="Input file")
    group_input.add_argument("-s", "--size", metavar="size", type=check_size, default=SIZE,
                             help="Generate a n-size puzzle")
    parser.add_argument("-us", "--unsolvable", action="store_true", help="Generate an unsolvable puzzle")
    parser.add_argument("-i", "--iteration", metavar="number", type=check_iteration, default=ITERATION,
                        help="Choose the number of scrambling moves")
    group_search = parser.add_mutually_exclusive_group()
    group_search.add_argument("-un", "--uniform", action="store_true", help="Enable uniform-cost search")
    group_search.add_argument("-gr", "--greedy", action="store_true", help="Enable greedy search")
    parser.add_argument("-hf", "--heuristic", default=HEURISTIC_DEFAULT,
                        choices=HEURISTIC,
                        help="Heuristic function choice, (default: %(default)s)")
    parser.add_argument("-t", "--time", action="store_true", help="Print time")
    parser.add_argument("-a", "--attempt", action="store_true", help="Attempt to solve unsolvable puzzle")
    return vars(parser.parse_args())
