import os.path as path

with open(path.dirname(__file__) + "/input", "r") as file:
    grid = file.readlines()

max_x = len(grid)
max_y = len(grid[0])
count = 0

for x in range(max_x):
    for y in range(max_y):
        if (grid[x][y] == 'A'):
            if any([(x - 1 < 0), (y - 1 < 0), (x + 1 >= max_x), (y + 1 >= max_y)]):
                pass
            elif any([((grid[x-1][y-1] == grid[x-1][y+1] == 'M') and (grid[x+1][y-1] == grid[x+1][y+1] == 'S')),
                     ((grid[x+1][y-1] == grid[x+1][y+1] == 'M') and (grid[x-1][y-1] == grid[x-1][y+1] == 'S')),
                     ((grid[x+1][y-1] == grid[x-1][y-1] == 'M') and (grid[x+1][y+1] == grid[x-1][y+1] == 'S')),
                     ((grid[x+1][y+1] == grid[x-1][y+1] == 'M') and (grid[x+1][y-1] == grid[x-1][y-1] == 'S'))]):
                count += 1

print(count)