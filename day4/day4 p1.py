import os.path as path

with open(path.dirname(__file__) + "/input", "r") as file:
    grid = file.readlines()

max_x = len(grid)
max_y = len(grid[0])
count = 0

for x in range(max_x):
    for y in range(max_y):
        if (grid[x][y] == 'X'):

            for i in range(-1, 2):
                for j in range(-1, 2):
                    #If endpoint out of bounds
                    if (not -1 < x + 3*i < max_x) or (not -1 < y + 3*j < max_y):
                        pass
                    elif (grid[x+i][y+j] == 'M' and grid[x+2*i][y+2*j] == 'A' and grid[x+3*i][y+3*j] == 'S'):
                        count += 1

print(count)