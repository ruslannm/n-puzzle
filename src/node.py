class Node:
  def __init__(self, puzzle, last_move="", depth=0, predecessor=None, g=0, f=0):
    self.predecessor = predecessor
    self.puzzle = [i for i in puzzle]
    self.last_move = last_move
    self.depth = depth
    self.g = g
    self.f = f



