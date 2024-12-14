import re

pattern = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'

with open('input.txt') as infile:
    raw_robots = infile.read().strip().split('\n')

# input.txt
w, h = 101, 103
# small_input.txt
# w, h = 11, 7

positions = {}

for raw_robot in raw_robots:
    match = re.match(pattern, raw_robot)
    x, y, vx, vy = [int(n) for n in match.groups()]
    dx, dy = (x + vx * 100) % w, (y + vy * 100) % h
    if (dx, dy) not in positions:
        positions[(dx, dy)] = 1
    else:
        positions[(dx, dy)] += 1

q0 = sum([c for (x, y), c in positions.items() if x < w // 2 and y < h // 2])
q1 = sum([c for (x, y), c in positions.items() if x > w // 2 and y < h // 2])
q2 = sum([c for (x, y), c in positions.items() if x < w // 2 and y > h // 2])
q3 = sum([c for (x, y), c in positions.items() if x > w // 2 and y > h // 2])

print(q0, q1, q2, q3)
print(q0 * q1 * q2 * q3)
