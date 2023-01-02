import numpy as np
import random

size = 10
grid = np.full((size,size), 0)
grid[0,0] = size*size*100

print(grid)

def evolve(grid):
    rows, cols = grid.shape
    next = np.full((rows,cols), 0)
    for i in range(rows):
        for j in range(cols):
            n = grid[i,j]
            for k in range(n):
                dx = random.choice([-1,0,1])
                dy = random.choice([-1,0,1])
                x = j + dx
                y = i + dy
                if (0 <= x < cols) and (0 <= y < rows):
                    next[y,x] += 1
                else:
                    next[i,j] += 1
    return next

vars = []
for i in range(1000):
    grid = evolve(grid)
    vars.append(np.var(grid))
    print(i, vars[-1])
    print(grid)

for i in range(len(vars)):
    print(i, vars[i])

window = 100
for i in range(len(vars)-window):
    print(i, np.var(vars[i:i+window]))