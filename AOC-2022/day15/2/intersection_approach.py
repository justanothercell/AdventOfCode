from itertools import combinations

with open('input.txt') as infile:
    data = [row.strip() for row in infile.readlines()]


class Sensor:
    def __init__(self, p, b):
        self.pos = p
        self.beacon = b
        self.dist = abs(b[0] - p[0]) + abs(b[1] - p[1])


sensors = []

for d in data:
    _, _, px, py, _, _, _, _, bx, by = d.strip().split()
    p = int(px[2:-1]), int(py[2:-1])
    b = int(bx[2:-1]), int(by[2:])
    sensors.append(Sensor(p, b))


def line_intersect(l1p1, l1p2, l2p1, l2p2):
    dx1 = l1p2[0] - l1p1[0]
    dy1 = l1p2[1] - l1p1[1]
    dx2 = l2p2[0] - l2p1[0]
    dy2 = l2p2[1] - l2p1[1]
    if dy2 * dx1 - dx2 * dy1 != 0:
        t1 = -(dx2 * (l2p1[1] - l1p1[1]) + dy2 * l1p1[0] - l2p1[0] * dy2) / (dy2 * dx1 - dx2 * dy1)
        return l1p1[0] + dx1 * t1, l1p1[1] + dy1 * t1
    return None


# x1 + t1 * dx1 = x2 + t2 * dx2
# y1 + t1 * dy1 = y2 + t2 * dy2
#
# rewrite as:
# a + x * d = A + y * D
# b + x * f = B + y * F
# (for solvers)
# x = -(D(B-b)+Fa-AF)/(Fd-Df)
# y = (-af+Af+(b-D)d)/(Fd-Df)

intersections = []

for a, b in combinations(sensors, 2):
    lines_a = [((a.pos[0], a.pos[1] - a.dist), (a.pos[0] + a.dist, a.pos[1])),
               ((a.pos[0] + a.dist, a.pos[1]), (a.pos[0], a.pos[1] + a.dist)),
               ((a.pos[0], a.pos[1] + a.dist), (a.pos[0] - a.dist, a.pos[1])),
               ((a.pos[0] - a.dist, a.pos[1]), (a.pos[0], a.pos[1] - a.dist))]
    lines_b = [((b.pos[0], b.pos[1] - b.dist), (b.pos[0] + b.dist, b.pos[1])),
               ((b.pos[0] + b.dist, b.pos[1]), (b.pos[0], b.pos[1] + b.dist)),
               ((b.pos[0], b.pos[1] + b.dist), (b.pos[0] - b.dist, b.pos[1])),
               ((b.pos[0] - b.dist, b.pos[1]), (b.pos[0], b.pos[1] - b.dist))]
    for la in lines_a:
        for lb in lines_b:
            p = line_intersect(la[0], la[1], lb[0], lb[1])
            if p is not None:
                if abs(p[0]-a.pos[0]) + abs(p[1]-a.pos[1]) == a.dist:
                    if 0 <= p[0] <= 4_000_000 and 0 <= p[1] <= 4_000_000:
                        intersections.append(p)

print(f'intersections: {len(intersections)}')

for i, p in enumerate(intersections):
    for x in range(int(p[0]-1), int(p[0]+1)):
        for y in range(int(p[1] - 1), int(p[1] + 1)):
            for sensor in sensors:
                d = abs(x-sensor.pos[0]) + abs(y-sensor.pos[1])
                if d <= sensor.dist or sensor.beacon == (x, y):
                    break
            else:
                print(f'found: {(x, y)} frequency: {x * 4_000_000 + y}')
    if i % 100 == 0:
        print(i / len(intersections))

# found: (2721114, 3367718) frequency: 10884459367718
# note: it finds this two times
