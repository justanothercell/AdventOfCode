steps_list = []


def sim_for_start(a):
    with open('input.txt') as infile:
        str_map = [row.strip() for row in infile.readlines()]
    # steps_list: [29, 30, 30, 30, 31, 31]
    # min: 29
    # str_map = [
    #     'Sabqponm',
    #     'abcryxxl',
    #     'accszExk',
    #     'acctuvwj',
    #     'abdefghi',
    # ]
    map = [[x if x != 'S' else 'a' for x in row] for row in str_map]

    end = (0, 0)

    for y, row in enumerate(str_map):
        for x, t in enumerate(row):
            if t == 'S':
                str_map[y] = str_map[y].replace('S', 'a')
            if t == 'E':
                end = (x, y)
                str_map[y] = str_map[y].replace('E', 'z')

    start = None

    ac = 0
    for y, row in enumerate(str_map):
        for x, t in enumerate(row):
            if t == 'a':
                if ac == a:
                    start = (x, y)
                    map[y][x] = 0
                ac += 1

    if start is None:
        return False

    squares = []


    def dist(p1, p2):
        return abs(p2[0]-p1[0])+abs(p2[1]-p1[1])


    def add_square(x, y):
        squares.append((dist((x, y), end), (x, y)))
        squares.sort(key=lambda item: item[0])


    add_square(*start)


    def move(p1, p2, w):
        if 0 <= p2[0] < len(map[0]) and 0 <= p2[1] < len(map):
            if ord(str_map[p1[1]][p1[0]]) < ord(str_map[p2[1]][p2[0]]) - 1:
                return
            if isinstance(map[p2[1]][p2[0]], int):
                c = map[p2[1]][p2[0]]
                if c > w:
                    map[p2[1]][p2[0]] = w
                    add_square(*p2)
            else:
                map[p2[1]][p2[0]] = w
                add_square(*p2)


    def step():
        d, s = squares.pop(0)
        w = map[s[1]][s[0]]
        move(s, (s[0] - 1, s[1]), w + 1)
        move(s, (s[0] + 1, s[1]), w + 1)
        move(s, (s[0], s[1] - 1), w + 1)
        move(s, (s[0], s[1] + 1), w + 1)
        return isinstance(map[end[1]][end[0]], int)

    sim_steps = 0

    while len(squares) > 0:
        step()
        sim_steps += 1
    if isinstance(map[end[1]][end[0]], int):
        steps_list.append(map[end[1]][end[0]])
    return True


with open('input.txt') as infile:
    str_map = [row.strip() for row in infile.readlines()]

# str_map = [
#     'Sabqponm',
#     'abcryxxl',
#     'accszExk',
#     'acctuvwj',
#     'abdefghi',
# ]
num_a = sum([sum([1 if x == 'a' else 0 for x in row]) for row in str_map])

a = 0
while sim_for_start(a):
    print(a, '/', num_a)
    a += 1

steps_list.sort()

print(f'steps_list: {steps_list}')
print(f'min: {steps_list[0]}')

# steps_list: [459, 460, 460, 460, 461, 461, 461, 461, 462, 462, 462, 463, 463, 464, 464, 464, 465, 465, 465, 465, 466, 466, 466, 466, 467, 467, 467, 467, 468, 468, 468, 468, 468, 468, 469, 469, 469, 469, 469, 470, 470, 470, 471, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484]
# min: 459
