import re, argparse
COMMENT = "#"

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
                if line[0] == COMMENT:
                    continue
                line = clear(line)
                if i == 0:
                    if line[0] == " " or not line.isdigit():
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
        exit(-1)
    for i in range(size * size):
        if i in puzzle:
            continue
        else:
            print("Error in set")
            exit(-1)
    return size, puzzle

def get_input():
    print("a")
    parser = argparse.ArgumentParser()
    group_input = parser.add_mutually_exclusive_group()
    group_input.add_argument("-f", "--file", metavar="file", help="Input file")
    group_input.add_argument("-g", "--generate", metavar="size", type=int, help="Generate a n-size puzzle")
    parser.add_argument("-i", "--iteration", metavar="number", type=int, help="Choose the number of scrambling moves")
    group_search = parser.add_mutually_exclusive_group()
    group_search.add_argument("-un", "--uniform", action="store_true", help="Enable uniform-cost search")
    group_search.add_argument("-gr", "--greedy", action="store_true", help="Enable greedy search")
    parser.add_argument("-hf", "--heuristic", default="Manhattan_distance",
                        choices=["Manhattan_distance", "Euclidian_distance", "Hamming_distance"],
                        help="Heuristic function choice, (default: %(default)s)")
    parser.add_argument("-t", "--time", action="store_true", help="Print time")
    args = parser.parse_args()
    print(args.time, args)