import os.path as path
import itertools


def antinode_diff(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    dx = (b[0] - a[0])
    dy = (b[1] - a[1])
    return (dx, dy)


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
        antinodes_1 = antinode_diff(pair[0], pair[1])
        antinodes_2 = antinode_diff(pair[1], pair[0])
        x, y = pair[0]
        while (in_bounds((x, y), max_i, max_j)):
            antinodes.add((x, y))
            x = x + antinodes_1[0]
            y = y + antinodes_1[1]
        x, y = pair[1]
        while (in_bounds((x, y), max_i, max_j)):
            antinodes.add((x, y))
            x = x + antinodes_2[0]
            y = y + antinodes_2[1]

print(len(antinodes))