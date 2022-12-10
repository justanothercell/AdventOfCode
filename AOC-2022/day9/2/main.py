with open('input.txt') as infile:
    movements = [row.strip() for row in infile.readlines()]

# visited: 1
#movements = [
#   'R 4',
#   'U 4',
#   'L 3',
#   'D 1',
#   'R 4',
#   'D 1',
#   'L 5',
#   'R 2',
#]

visited = set()

rope = [(0, 0) for _ in range(10)]

visited.add(rope[-1])


def sign(x):
    return -1 if x < 0 else 1


def move(mx, my):
    hx, hy = rope[0]
    hx += mx
    hy += my
    rope[0] = hx, hy

    for i in range(1, len(rope)):
        rope[i] = update(*rope[i - 1], *rope[i])

    visited.add(rope[-1])


# parent x, parent y, x and y
def update(px, py, x, y):
    dx, dy = abs(px - x), abs(py - y)
    if dx <= 1 and dy <= 1:
        return x, y
    if dx > 0:
        x += sign(px - x)
    if dy > 0:
        y += sign(py - y)
    return x, y


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

print('visited:', len(visited))  # visited: 106
