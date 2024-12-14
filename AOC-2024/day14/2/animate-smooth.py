import re
import time
from fractions import Fraction

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
    robots.append([Fraction(x), Fraction(y), Fraction(vx), Fraction(vy)])
    positions.add((x, y))

tick = 0
start = 6284
speed = Fraction(5, 10000)

while True:
    if tick > start:
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
        print(f'                             \rtick={float(tick)}')
        # time.sleep(0.25)
        print(f'\r\x1b[{6+h//2}A')
    else:
        print('\r\x1b[2A')
        print(f'                             \rtick={float(tick)}')
    if tick > start:
        positions.clear()
        tick += speed
    else:
        tick += 1
    for robot in robots:
        if tick > start:
            robot[0] = (robot[0] + robot[2] * speed) % w
            robot[1] = (robot[1] + robot[3] * speed) % h
            positions.add((round(robot[0]), round(robot[1])))
        else:
            robot[0] = (robot[0] + robot[2]) % w
            robot[1] = (robot[1] + robot[3]) % h

