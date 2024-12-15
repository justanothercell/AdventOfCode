from time import sleep

with open('input.txt') as infile:
    raw_map, raw_moves = infile.read().strip().split('\n\n')

map = []
x, y = 0, 0

for my, row in enumerate(raw_map.split('\n')):
    r = []
    for mx, c in enumerate(row):
        if c == '@':
            x, y = mx, my
            r.append(0)
        elif c == '#':
            r.append(-1)
        elif c == 'O':
            r.append(1)
        elif c == '.':
            r.append(0)
        else:
            assert False, f'unreachabe: tile {r}'
    map.append(r)

w, h = len(map[0]), len(map)

moves = raw_moves.replace('\n', '')

def display(p, first=False):
    if not first:
        print(f'\x1b[{h//2+1}A', end='');
    for my in range(0, h, 2):
        for mx in range(w):
             upper = 0 if my >= h else map[my][mx]
             lower = 0 if my+1 >= h else map[my+1][mx]
             if (mx, my) == (x, y):
                assert upper == 0, 'robot sits on something'
                print('\x1b[48;2;255;255;255m', end='')
             elif upper == -1:
                print('\x1b[48;2;255;0;0m', end='')
             elif upper == 0:
                print('\x1b[48;2;0;0;0m', end='')
             elif upper == 1:
                print('\x1b[48;2;0;255;0m', end='')
             else:
                assert False, f'unreachable: tile id {upper}'
             if (mx, my+1) == (x, y):
                assert lower == 0, 'robot sits on something'
                print('\x1b[38;2;255;255;255m', end='')
             elif lower == -1:
                print('\x1b[38;2;255;0;0m', end='')
             elif lower == 0:
                print('\x1b[38;2;0;0;0m', end='')
             elif lower == 1:
                print('\x1b[38;2;0;255;0m', end='')
             else:
                assert False, f'unreachable: tile id {lower}'
             print('▄\x1b[0m', end='')
        print()
    print(f'{p*100:03.00f}%')

def move(m) -> bool:
    global x, y
    if m == '^':
        dx, dy = 0, -1
    elif m == '>':
        dx, dy = 1, 0
    elif m == 'v':
        dx, dy = 0, 1
    elif m == '<':
        dx, dy = -1, 0
    else:
        assert False, f'unreachable: move instruction `{m}`'
    px, py = x + dx, y + dy
    while 0 <= px < w and 0 <= py < h:
        if map[py][px] == -1: # blocked, we cant move
            return False
        if map[py][px] == 0: # free, we can push stuff here and move
            x, y = x + dx, y + dy
            map[py][px], map[y][x] = map[y][x], map[py][px]
            return True
        px += dx
        py += dy
display(0, True)

count = len(moves)

for i, m in enumerate(moves):
    move(m)
    if i % 10 == 0:
        display(i / count)

display(1)

score = 0

for my in range(h):
    for mx in range(w):
        if map[my][mx] == 1:
            score += my * 100 + mx

print(score)
