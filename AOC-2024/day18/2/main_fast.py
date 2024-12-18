import random

with open('input.txt') as infile:
    coords = [tuple(int(c) for c in coord.split(',')) for coord in infile.read().strip().split('\n')]

coordset = set(coords)
placedset = set()

w, h = 71, 71
# w, h = 7, 7

ex, ey = w-1, h-1

chunks = {}

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
        return (x, y), d

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
    (x1r, y1r), d1 = find(x1, y1)
    (x2r, y2r), d2 = find(x2, y2)
    if (x1r, y1r) == (x2r, y2r): # already joined
        assert d1 == d2
        return (x1r, y1r), d1
    # join chunk2 onto chunk1
    chunks[(x2r, y2r)] = (x1r, y1r), None
    chunks[(x1r, y1r)] = None, d1 | d2
    return (x1r, y1r), d1 | d2

def find_blocker():
    for i, (x, y) in enumerate(coords):
        placedset.add((x, y))
        for dx in range(x-1, x+2):
            for dy in range(y-1, y+2):
                if (dx, dy) == (x, y):
                    continue
                if (dx, dy) not in placedset:
                    continue
                _, d = join(x, y, dx, dy)
                if (d & 0b0011) == 0b0011: # west/east touching
                    return i, (x, y)
                if (d & 0b1100) == 0b1100: # north/south touching
                    return i, (x, y)
                if (d & 0b0101) == 0b0101: # north/west touching
                    return i, (x, y)
                if (d & 0b1010) == 0b1010: # south/east touching
                    return i, (x, y)
t, (bx, by) = find_blocker()

print(f'blocking byte at x={bx}, y={by} at t={t}ns')
