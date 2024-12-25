import os.path as path


def walk_path(start_pos: tuple) -> set:
    max_x = len(grid)
    max_y = len(grid[0])

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    d = 0
    dx, dy = dirs[d]

    visited_locations = set()
    pos = start_pos
    while (True):
        if ((*pos, d) in visited_locations):
            raise Exception # UGLY BAD UGLY BAD
        else:
            visited_locations.add((*pos, d))

        # If going OOB
        if any([(not -1 < pos[0] + dx < max_x), (not -1 < pos[1] + dy < max_y)]):
            break

        # Change direction if hitting wall
        if (grid[pos[0] + dx][pos[1] + dy] == '#'):
            d = (d + 1) % 4
            dx, dy = dirs[d]
        else:
            pos = (pos[0] + dx, pos[1] + dy)

    return visited_locations


with open(path.dirname(__file__) + "/input", 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]

found = False
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (grid[i][j] == '^'):
            initial_pos = (i, j)
            found = True
            break
    if (found):
        break

# Get all locations
all_locations = walk_path(initial_pos)
print(len(all_locations))
all_locations.remove((*initial_pos, 0)) # Can't place at starting point

loop_locations = set()

for location in all_locations:
    x, y, d = location
    grid[x][y] = '#'
    try:
        walk_path(initial_pos)
    except:
        loop_locations.add((x, y))
    grid[x][y] = '.'

print(len(loop_locations))