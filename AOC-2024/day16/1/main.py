with open('input.txt') as infile:
    map = [list(row) for row in infile.read().strip().split('\n')]

w, h = len(map[0]), len(map)

sx, sy = 1, h-2
ex, ey = w-2, 1

#          x   y   dx dy px    py    score
stack = [ (sx, sy, 1, 0, None, None, 0) ]

while len(stack) > 0:
    x, y, dx, dy, px, py, score = stack.pop() # look at next move
    if map[y][x] == '#': # cannot move into wall
        continue
    if isinstance(map[y][x], str) and map[y][x] in '.ES': # first time visiting this tile
        map[y][x] = px, py, score
    elif map[y][x][2] > score: # lower score this way
        map[y][x] = px, py, score
    else: # not lower score
        continue
    if x != ex or y != ey: # not at end
        stack.append((x + dx, y + dy, dx, dy, x, y, score + 1)) # move forward
        stack.append((x - dy, y - dx, -dy, -dx, x, y, score + 1001)) # move left
        stack.append((x + dy, y + dx, dy, dx, x, y, score + 1001)) # move right
score = 0

x, y = ex, ey
pdx, pdy = None, None

path = [ (ex, ey) ]

while True:
    px, py, _ = map[y][x]
    if px is None:
        break
    path.append((px, py))
    x, y = px, py

for y in range(h):
    for x in range(w):
        if map[y][x] == '#':
            print('\x1b[48;2;220;0;0m#\x1b[0m', end='')
        elif isinstance(map[y][x], tuple):
            px, py, _ = map[y][x]
            if px is None:
                print('\x1b[48;2;0;255;0m*\x1b[0m', end='')
                continue
            if (x, y) in path:
                print('\x1b[48;2;100;100;0m', end='')
            dx, dy = x - px, y - py
            if dx == 0 and dy == 1:
                print('v', end='')
            if dx == 0 and dy == -1:
                print('^', end='')
            if dx == -1 and dy == 0:
                print('<', end='')
            if dx == 1 and dy == 0:
                print('>', end='')
            print('\x1b[0m', end='')
        else:
            print('.', end='')
    print()

print(map[ey][ex][2])
