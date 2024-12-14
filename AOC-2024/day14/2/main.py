import re
import time

pattern = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'

with open('input.txt') as infile:
    raw_robots = infile.read().strip().split('\n')

# input.txt
w, h = 101, 103
# small_input.txt
# w, h = 11, 7

robots = []

positions = set()

for raw_robot in raw_robots:
    match = re.match(pattern, raw_robot)
    x, y, vx, vy = [int(n) for n in match.groups()]
    dx, dy = (x + vx * 100) % w, (y + vy * 100) % h
    robots.append([x, y, vx, vy])
    positions.add((x, y))

tick = 0
max_score = 0
max_tick = 0

while True:
    score = 0
    for (x, y) in positions:
        if (w-x-1, y) in positions:
            score += 1
    print()
    if score > max_score:
        max_score = score
        max_tick = tick
        print()
        print()
        print()
        for y in range(0, h+2, 2): # h+2 because h is odd
            for x in range(w):
                upper = (x, y) in positions
                lower = (x, y+1) in positions
                if upper and lower:
                    print('█', end='')
                elif upper:
                    print('▀', end='')
                elif lower:
                    print('▄', end='')
                else:
                    print(' ', end='')
            print()
        print()
    print(f'                             \r{tick=}\t{score=}')
    print(f'                             \r{max_score=}\t{max_tick=}')
    tick += 1
    print('\r\x1b[4A')
    positions.clear()
    for robot in robots:
        robot[0] = (robot[0] + robot[2]) % w
        robot[1] = (robot[1] + robot[3]) % h
        positions.add((robot[0], robot[1]))
