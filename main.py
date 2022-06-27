from src.parse import get_input

if __name__ == "__main__":
    get_input()

    # parser = argparse.ArgumentParser()
    # group_input = parser.add_mutually_exclusive_group()
    # group_input.add_argument("-f", "--file", metavar="file", help="Input file")
    # group_input.add_argument("-g", "--generate", metavar="size", type=int, help="Generate a n-size puzzle")
    # parser.add_argument("-i", "--iteration", metavar="number", type=int, help="Choose the number of scrambling moves")
    # group_search = parser.add_mutually_exclusive_group()
    # group_search.add_argument("-un", "--uniform", action="store_true", help="Enable uniform-cost search")
    # group_search.add_argument("-gr", "--greedy", action="store_true", help="Enable greedy search")
    # parser.add_argument("-hf", "--heuristic", default="Manhattan_distance",
    #                     choices=["Manhattan_distance", "Euclidian_distance", "Hamming_distance"],
    #                     help="Heuristic function choice, (default: %(default)s)")
    # parser.add_argument("-t", "--time", action="store_true", help="Print time")
    # args = parser.parse_args()
    # print(args.time, args)
