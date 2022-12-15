import time

with open('input.txt') as infile:
    data = [row.strip() for row in infile.readlines()]

# safe_min: -8
# safe_max: 28
# supervised: 26
# data = [
#     'Sensor at x=2, y=18: closest beacon is at x=-2, y=15',
#     'Sensor at x=9, y=16: closest beacon is at x=10, y=16',
#     'Sensor at x=13, y=2: closest beacon is at x=15, y=3',
#     'Sensor at x=12, y=14: closest beacon is at x=10, y=16',
#     'Sensor at x=10, y=20: closest beacon is at x=10, y=16',
#     'Sensor at x=14, y=17: closest beacon is at x=10, y=16',
#     'Sensor at x=8, y=7: closest beacon is at x=2, y=10',
#     'Sensor at x=2, y=0: closest beacon is at x=2, y=10',
#     'Sensor at x=0, y=11: closest beacon is at x=2, y=10',
#     'Sensor at x=20, y=14: closest beacon is at x=25, y=17',
#     'Sensor at x=17, y=20: closest beacon is at x=21, y=22',
#     'Sensor at x=16, y=7: closest beacon is at x=15, y=3',
#     'Sensor at x=14, y=3: closest beacon is at x=15, y=3',
#     'Sensor at x=20, y=1: closest beacon is at x=15, y=3',
# ]


class Sensor:
    def __init__(self, p, b):
        self.pos = p
        self.beacon = b
        self.dist = abs(b[0]-p[0]) + abs(b[1]-p[1])


sensors = []

for d in data:
    _, _, px, py, _, _, _, _, bx, by = d.strip().split()
    p = int(px[2:-1]), int(py[2:-1])
    b = int(bx[2:-1]), int(by[2:])
    sensors.append(Sensor(p, b))

safe_min = 0
safe_max = 0

for sensor in sensors:
    safe_min = min(safe_min, sensor.pos[0] - sensor.dist)
    safe_max = max(safe_max, sensor.pos[0] + sensor.dist)

print(f'safe_min: {safe_min}')
print(f'safe_max: {safe_max}')
# safe_min: -1744671
# safe_max: 5904101


# y = 10  # test data
y = 2_000_000  # real data

start = time.time()

supervised = 0
for x in range(safe_min, safe_max + 1):
    for sensor in sensors:
        d = abs(x-sensor.pos[0]) + abs(y-sensor.pos[1])
        if d <= sensor.dist and sensor.beacon != (x, y):
            supervised += 1
            # print('#', end='')
            break
    else:
        # print('.', end='')
        pass
    if x % 100000 == 0:
        print(x)
print()
print(f'duration: {time.time() - start}s')
# duration: 40.43449664115906s
print(f'supervised: {supervised}')
# supervised: 5142231

# this is very brute force but works
