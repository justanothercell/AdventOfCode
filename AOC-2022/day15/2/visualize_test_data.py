data = [
    'Sensor at x=2, y=18: closest beacon is at x=-2, y=15',
    'Sensor at x=9, y=16: closest beacon is at x=10, y=16',
    'Sensor at x=13, y=2: closest beacon is at x=15, y=3',
    'Sensor at x=12, y=14: closest beacon is at x=10, y=16',
    'Sensor at x=10, y=20: closest beacon is at x=10, y=16',
    'Sensor at x=14, y=17: closest beacon is at x=10, y=16',
    'Sensor at x=8, y=7: closest beacon is at x=2, y=10',
    'Sensor at x=2, y=0: closest beacon is at x=2, y=10',
    'Sensor at x=0, y=11: closest beacon is at x=2, y=10',
    'Sensor at x=20, y=14: closest beacon is at x=25, y=17',
    'Sensor at x=17, y=20: closest beacon is at x=21, y=22',
    'Sensor at x=16, y=7: closest beacon is at x=15, y=3',
    'Sensor at x=14, y=3: closest beacon is at x=15, y=3',
    'Sensor at x=20, y=1: closest beacon is at x=15, y=3',
]


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

min_x = 0
max_x = 0
min_y = 0
max_y = 0

for sensor in sensors:
    min_x = min(min_x, sensor.pos[0] - sensor.dist)
    max_x = max(max_x, sensor.pos[0] + sensor.dist)
    min_y = min(min_y, sensor.pos[1] - sensor.dist)
    max_y = max(max_y, sensor.pos[1] + sensor.dist)

print(f'min_bounds: {(min_x, min_y)}')
print(f'max_bounds: {(max_x, max_y)}')


for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        for sensor in sensors:
            if (x, y) == sensor.pos:
                print('S', end='')
                break
            elif (x, y) == sensor.beacon:
                print('B', end='')
                break
        else:
            for sensor in sensors:
                d = abs(x - sensor.pos[0]) + abs(y - sensor.pos[1])
                if d <= sensor.dist and not (x == sensor.beacon[0] and y == sensor.beacon[1]):
                    print('#', end='')
                    break
            else:
                print('.', end='')
    print()