import os

with open('input.txt') as infile:
    str_map = [row.strip() for row in infile.readlines()]

# steps: 31
# v..v<<<<
# >v.vv<<^
# .>vv>E^^
# ..v>>>^^
# ..>>>>>^
# str_map = [
#     'Sabqponm',
#     'abcryxxl',
#     'accszExk',
#     'acctuvwj',
#     'abdefghi',
# ]

os.system("")

map = [[x if x != 'S' else 0 for x in row] for row in str_map]


start = (0, 0)
end = (0, 0)

for y, row in enumerate(str_map):
    for x, t in enumerate(row):
        if t == 'S':
            start = (x, y)
            str_map[y] = str_map[y].replace('S', 'a')
        if t == 'E':
            end = (x, y)
            str_map[y] = str_map[y].replace('E', 'z')


def print_map():
    ms = '\x1b[H'
    for y, row in enumerate(map):
        for x, t in enumerate(row):
            if isinstance(t, int):
                if t == 0:
                    ms += f'\x1b[2;97;41mS\x1b[0m'
                else:
                    r = 100 if any([s == (x, y) for d, s in squares]) else 0
                    g = (ord(str_map[y][x]) - ord('a')) * 10 + 5
                    b = int(t / max_move * 200) + 55
                    ms += f'\x1b[48;2;{r};{g};{b}m{str_map[y][x]}\x1b[0m'
            elif t == 'E':
                ms += f'\x1b[2;97;41m{t}\x1b[0m'
            else:
                r = 0
                g = (ord(t) - ord('a')) * 10 + 5
                b = 0
                ms += f'\x1b[48;2;{r};{g};{b}m{t}\x1b[0m'
        ms += '\n'
    print(ms)

print_map()

squares = []


def dist(p1, p2):
    return abs(p2[0]-p1[0])+abs(p2[1]-p1[1])


def add_square(x, y):
    squares.append((dist((x, y), end), (x, y)))
    squares.sort(key=lambda item: item[0])


add_square(*start)


max_move = 0


def move(p1, p2, w):
    if 0 <= p2[0] < len(map[0]) and 0 <= p2[1] < len(map):
        if ord(str_map[p1[1]][p1[0]]) < ord(str_map[p2[1]][p2[0]]) - 1:
            return
        global max_move
        max_move = max(max_move, w)
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

print_interval = 20

while not step():
    sim_steps += 1
    if sim_steps % print_interval == 0:
        print_map()

print_map()
print(f'steps: {map[end[1]][end[0]]}')
print(f'max_move: {max_move}')

while len(squares) > 0:
    step()
    sim_steps += 1
    if sim_steps % print_interval == 0:
        print_map()


print_map()
print(f'steps fully explored: {map[end[1]][end[0]]}')
print(f'max_move fully explored: {max_move}')
# steps: 480
# max_move: 480
# steps fully explored: 468
# max_move fully explored: 489
