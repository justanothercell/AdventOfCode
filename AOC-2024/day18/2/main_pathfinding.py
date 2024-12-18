from time import sleep
from queue import PriorityQueue

with open('input.txt') as infile:
    coords = [[int(c) for c in coord.split(',')] for coord in infile.read().strip().split('\n')]

w, h = 71, 71
# w, h = 7, 7

ex, ey = w-1, h-1
memory = [[100_000 for x in range(w)] for y in range(h)]

def printmem(first=False):
    if not first:
        print(f'\x1b[{h//2+1}A', end='')
    for y in range(0, h, 2):
        for x in range(w):
            upper = 100_000 if y >= h else memory[y][x]
            lower = 100_000 if y+1 >= h else memory[y+1][x]
            if (x, y) in path:
                print('\x1b[48;2;255;255;0m', end='')
            elif upper == 100_000:
                print('\x1b[48;2;0;0;0m', end='')
            elif upper == -1:
                print('\x1b[48;2;255;0;0m', end='')
            else:
                print(f'\x1b[48;2;0;255;{int(upper/plen*255)}m', end='')
            if (x, y+1) in path:
                print('\x1b[38;2;255;255;0m', end='')
            elif lower == 100_000:
                print('\x1b[38;2;0;0;0m', end='')
            elif lower == -1:
                print('\x1b[38;2;255;0;0m', end='')
            else:
                print(f'\x1b[38;2;0;255;{int(lower/plen*255)}m', end='')
            print('▄\x1b[0m', end='')
        print()

path = []
printmem(first=True)
for mx, my in coords:
    memory[my][mx] = -1
    for y in range(h):
        for x in range(w):
            if memory[y][x] >= 0:
                memory[y][x] = 100_000
    plen = 1
    path.clear()
    queue = PriorityQueue()
    queue.put((ex+ey, (0, 0, 0)))
    while not queue.empty():
        _, (x, y, s) = queue.get()
        plen = max(plen, s)
        if memory[y][x] <= s:
           continue
        memory[y][x] = s
        if (x, y) == (ex, ey):
            break
        if x > 0 and memory[y][x-1] != -1:
            queue.put(((ex-(x-1))+(ey-y    ), (x-1, y  , s+1)))
        if x < w-1 and memory[y][x+1] != -1:
            queue.put(((ex-(x+1))+(ey-y    ), (x+1, y  , s+1)))
        if y > 0 and memory[y-1][x] != -1:
            queue.put(((ex-x    )+(ey-(y-1)), (x  , y-1, s+1)))
        if y < h-1 and memory[y+1][x] != -1:
            queue.put(((ex-x    )+(ey-(y+1)), (x  , y+1, s+1)))

    x, y = ex, ey
    path.append((x, y))
    blocked = False
    while (x, y) != (0, 0):
        if x > 0 and memory[y][x] > memory[y][x-1] and memory[y][x-1] >= 0:
            x, y = x-1, y
        elif x < w-1 and memory[y][x] > memory[y][x+1] and memory[y][x+1] >= 0:
            x, y = x+1, y
        elif y > 0 and memory[y][x] > memory[y-1][x] and memory[y-1][x] >= 0:
            x, y = x, y-1
        elif y < w-1 and memory[y][x] > memory[y+1][x] and memory[y+1][x] >= 0:
            x, y = x, y+1
        else:
            blocked = True
            break
        path.append((x, y))
    printmem()
    if blocked:
        print(f'byte at x={mx} y={my} blocked path')
        break


