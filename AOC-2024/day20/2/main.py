with open('input.txt') as infile:
    raw_map = infile.read().strip().split('\n')

w, h = len(raw_map[0]), len(raw_map)

sx, sy = 0, 0
ex, ey = 0, 0
map = []

for y, row in enumerate(raw_map):
    r = []
    for x, t in enumerate(row):
        if t == '#':
            r.append(-1)
        elif t == '.':
            r.append(0)
        elif t == 'S':
            sx, sy = x, y
            r.append(0)
        elif t == 'E':
            ex, ey = x, y
            r.append(0)
        else:
            assert False, 'unreachable'
    map.append(r)

picoseconds = 0

x, y = sx, sy
px, py = None, None
while (x, y) != (ex, ey):
    if x > 0 and (px, py) != (x-1, y) and map[y][x-1] != -1:
        nx, ny = x-1, y
    elif x < w-1 and (px, py) != (x+1, y) and map[y][x+1] != -1:
        nx, ny = x+1, y
    elif y > 0 and (px, py) != (x, y-1) and map[y-1][x] != -1:
        nx, ny = x, y-1
    elif y < h-1 and (px, py) != (x, y+1) and map[y+1][x] != -1:
        nx, ny = x, y+1
    else:
        assert False, 'unreachable'
    picoseconds += 1
    map[ny][nx] = picoseconds
    px, py = x, y
    x, y = nx, ny

print(f'course normally takes {picoseconds}ps')

cheats = {}

x, y = sx, sy
px, py = None, None
while (x, y) != (ex, ey):
    if x > 0 and (px, py) != (x-1, y) and map[y][x-1] != -1:
        nx, ny = x-1, y
    elif x < w-1 and (px, py) != (x+1, y) and map[y][x+1] != -1:
        nx, ny = x+1, y
    elif y > 0 and (px, py) != (x, y-1) and map[y-1][x] != -1:
        nx, ny = x, y-1
    elif y < h-1 and (px, py) != (x, y+1) and map[y+1][x] != -1:
        nx, ny = x, y+1
    else:
        assert False, 'unreachable'
    current = map[y][x]
    for dy in range(-20, 21):
        for dx in range(-20, 21):
            # move at most two cheat steps
            if abs(dx)+abs(dy) > 20:
                continue
            if x+dx < 0 or x+dx >= w or y+dy < 0 or y+dy >= h:
                continue
            dest = map[y+dy][x+dx]
            if dest == -1: # landed on wall
                continue
            delta = dest - current - abs(dx) - abs(dy) # how much we skip
            if delta <= 0: # we do not wish to skip backwards or make zero progress
                continue
            if delta not in cheats:
                cheats[delta] = 1
            else:
                cheats[delta] += 1
    px, py = x, y
    x, y = nx, ny

# sort cheats by saved time
cheats = dict(sorted(cheats.items(), key=lambda item: item[0]))

total = 0

print()
for cheat, count in cheats.items():
    print(f'There are {count} cheats that save {cheat}ps')
    if cheat >= 100:
        total += count
print()
print(f'{total} cheats save at least 100ps')
