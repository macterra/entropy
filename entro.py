import numpy as np
import random

size = 16
mean = 100
grid = np.full((size,size), 0)
grid[0,0] = size*size*100

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

stds = []
for i in range(1000):
    grid = evolve(grid)
    sall = np.std(grid)
    q = size//2
    nw = grid[:q,:q]
    ne = grid[:q,q:size]
    sw = grid[q:size,:q]
    se = grid[q:size,q:size]
    stds.append(np.std(grid))
    mnw = np.mean(nw)
    mne = np.mean(ne)
    msw = np.mean(sw)
    mse = np.mean(se)
    qsd = np.std([mnw, mne, msw, mse])
    print(f'{i:4d} {stds[i]/mean:10.4f} {mnw:10.4f} {mne:10.4f} {msw:10.4f} {mse:10.4f} {qsd:10.4f}')
    print(grid)
    if qsd < 1:
        break

def analyze(data, window):
    for i in range(len(data)-window):
        m = np.mean(data[i:i+window])
        s = np.std(data[i:i+window])
        z = s/m
        print(f'{i:4d} {data[i]:10.4f} {m:10.4f} {s:10.4f} {z:10.4f}')

#analyze(stds, 100)
