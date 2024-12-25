import os.path as path
import itertools


def antinode(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    x = b[0] + (b[0] - a[0])
    y = b[1] + (b[1] - a[1])
    return (x, y)


def in_bounds(a: tuple[int, int], max_i: int, max_j: int) -> bool:
    if (a[0] >= 0 and a[0] < max_i) and (a[1] >= 0 and a[1] < max_j):
        return True
    else:
        return False


grid = []
antennas = {}
antinodes = set()

with open(path.dirname(__file__) + "/input", 'r') as file:
    grid = [line.strip() for line in file.readlines()]

max_i = len(grid)
max_j = len(grid[0])

for i in range(max_i):
    for j in range(max_j):
        c = grid[i][j]
        if (c == '.'):
            pass
        elif (c not in antennas.keys()):
            antennas[c] = [(i, j)]
        else:
            antennas[c].append((i, j))

for antenna in antennas.keys():
    for pair in list(itertools.combinations(antennas[antenna], 2)):
        antinode_1 = antinode(pair[0], pair[1])
        antinode_2 = antinode(pair[1], pair[0])
        if in_bounds(antinode_1, max_i, max_j):
            antinodes.add(antinode_1)
        if in_bounds(antinode_2, max_i, max_j):
            antinodes.add(antinode_2)

print(len(antinodes))