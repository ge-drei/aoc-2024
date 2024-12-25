import os.path as path

with open(path.dirname(__file__) + "/debug", 'r') as file:
    grid = [list(line) for line in file.readlines()]

found = False
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (grid[i][j] == '^'):
            pos = (i, j)
            found = True
            break
    if (found):
        break

max_x = len(grid)
max_y = len(grid[0])

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d = 0
dx, dy = dir[d]
visited_locations = set()

while (True):
    visited_locations.add((*pos, d))

    # If going OOB
    if any([(not -1 < pos[0] + dx < max_x), (not -1 < pos[1] + dy < max_y)]):
        break

    # Change direction if hitting wall
    if (grid[pos[0] + dx][pos[1] + dy] == '#'):
        d = (d + 1) % 4
        dx, dy = dir[d]
    
    pos = (pos[0] + dx, pos[1] + dy)

print(len(visited_locations))