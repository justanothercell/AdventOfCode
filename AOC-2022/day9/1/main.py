with open('input.txt') as infile:
    movements = [row.strip() for row in infile.readlines()]

# visited: 13
#movements = [
#    'R 4',
#    'U 4',
#    'L 3',
#    'D 1',
#    'R 4',
#    'D 1',
#    'L 5',
#    'R 2',
#]

visited = set()

hx, hy = 0, 0
tx, ty = 0, 0

visited.add((tx, ty))


def sign(x):
    return -1 if x < 0 else 1


def move(mx, my):
    global hx, hy, tx, ty
    hx += mx
    hy += my
    dx, dy = abs(hx-tx), abs(hy-ty)
    if dx <= 1 and dy <= 1:
        return
    if dx > 0:
        tx += sign(hx-tx)
    if dy > 0:
        ty += sign(hy-ty)
    visited.add((tx, ty))


for m in movements:
    d, s = m.strip().split()
    s = int(s)
    for _ in range(s):
        if d == 'U':
            move(0, -1)
        if d == 'D':
            move(0, 1)
        if d == 'L':
            move(-1, 0)
        if d == 'R':
            move(1, 0)

print('visited:', len(visited))  # visited: 6563

