with open('input.txt') as infile:
    data = [row.strip() for row in infile.readlines()]

# x=14, y=11
# frequency: 56000011
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


for y in range(0, 4_000_000, 100000):
    for x in range(0, 4_000_000, 100000):
        max_d = 0
        for sensor in sensors:
            d = abs(x - sensor.pos[0]) + abs(y - sensor.pos[1])
            max_d = max(max_d, (sensor.dist - d) / sensor.dist)
        c = chr(ord('a') + int(max_d * 26))
        print(c, end='')
    print()
