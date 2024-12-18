import random

with open('input.txt') as infile:
    coords = [tuple(int(c) for c in coord.split(',')) for coord in infile.read().strip().split('\n')]

coordset = set(coords)
placedset = set()

w, h = 71, 71
# w, h = 7, 7

ex, ey = w-1, h-1

chunks = {}

def colors(i):
    random.seed(i)
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def find(x, y):
    if (x, y) not in chunks:
        d = 0
        if x == 0:
            d |= 0b0001
        if x == w-1:
            d |= 0b0010
        if y == 0:
            d |= 0b0100
        if y == h-1:
            d |= 0b1000
        return (x, y), (d, y*w+x, 1)

    p = []
    data = None
    while data is None:
        pos, data = chunks[(x, y)]
        if pos is not None:
            assert data is None
            p.append((x, y))
            x, y = pos
        else:
            assert data is not None

    for px, py in p[:-1]: # last one already points to x, y
        chunks[(px, py)] = (x, y), None
    return (x, y), data

def join(x1, y1, x2, y2):
    (x1r, y1r), (d1, i1, s1) = find(x1, y1)
    (x2r, y2r), (d2, i2, s2) = find(x2, y2)
    if (x1r, y1r) == (x2r, y2r): # already joined
        assert d1 == d2
        assert i1 == i2
        assert s1 == s2
        return (x1r, y1r), (d1, i1, s1)
    # join chunk2 onto chunk1
    chunks[(x2r, y2r)] = (x1r, y1r), None
    chunks[(x1r, y1r)] = None, (d1 | d2, i1 if s1 >= s2 else s2, s1 + s2)
    return (x1r, y1r), (d1 | d2, i1 if s1 >= s2 else s2, s1 + s2)

def printmem(first=False):
    if not first:
        print(f'\x1b[{h//2+1}A', end='')
    for y in range(0, h, 2):
        for x in range(w):
            upper = -1 if y >= h or (x, y) not in placedset else find(x, y)[1][1]
            lower = -1 if y+1 >= h or (x, y+1) not in placedset else find(x, y+1)[1][1]
            if upper == -1:
                print('\x1b[48;2;0;0;0m', end='')
            else:
                r, g, b = colors(upper)
                print(f'\x1b[48;2;{r};{g};{b}m', end='')
            if lower == -1:
                print('\x1b[38;2;0;0;0m', end='')
            else:
                r, g, b = colors(lower)
                print(f'\x1b[38;2;{r};{g};{b}m', end='')
            print('▄\x1b[0m', end='')
        print()

def find_blocker():
    printmem(first=True)
    for i, (x, y) in enumerate(coords):
        placedset.add((x, y))
        for dx in range(x-1, x+2):
            for dy in range(y-1, y+2):
                if (dx, dy) == (x, y):
                    continue
                if (dx, dy) not in placedset:
                    continue
                _, (d, index, size) = join(x, y, dx, dy)
                if (d & 0b0011) == 0b0011: # west/east touching
                    return i, (x, y)
                if (d & 0b1100) == 0b1100: # north/south touching
                    return i, (x, y)
                if (d & 0b0101) == 0b0101: # north/west touching
                    return i, (x, y)
                if (d & 0b1010) == 0b1010: # south/east touching
                    return i, (x, y)
        printmem()
t, (bx, by) = find_blocker()
printmem()
print(f'blocking byte at x={bx}, y={by} at t={t}ns')
