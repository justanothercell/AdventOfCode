from time import sleep
from random import randint

with open('input.txt') as infile:
    raw_map, raw_moves = infile.read().strip().split('\n\n')

map = []
x, y = 0, 0
colors = [(255, 255, 0)]
boxid = 1
for my, row in enumerate(raw_map.split('\n')):
    r = []
    for mx, c in enumerate(row):
        if c == '@':
            x, y = mx*2, my
            r.append(0)
            r.append(0)
        elif c == '#':
            r.append(-1)
            r.append(-1)
        elif c == 'O':
            r.append(boxid)
            r.append(boxid)
            boxid += 1
            colors.append((randint(0, 128), randint(128, 255), randint(100, 200)))
        elif c == '.':
            r.append(0)
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
             else:
                r, g, b = colors[upper]
                print(f'\x1b[48;2;{r};{g};{b}m', end='')
             if (mx, my+1) == (x, y):
                assert lower == 0, 'robot sits on something'
                print('\x1b[38;2;255;255;255m', end='')
             elif lower == -1:
                print('\x1b[38;2;255;0;0m', end='')
             elif lower == 0:
                print('\x1b[38;2;0;0;0m', end='')
             else:
                r, g, b = colors[lower]
                print(f'\x1b[38;2;{r};{g};{b}m', end='')
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
    if map[y+dy][x+dx] == -1: # blocked, we cant move
        return False
    if map[y+dy][x+dx] == 0: # free, we can move
        x, y = x + dx, y + dy
        return True
    # now we need to check for boxes
    check = [(x+dx, y+dy)] # box parts to check for movability
    move = [] # positions already chekced to move
    moveset = set()
    while len(check) > 0: # still boxes to check
        bx, by = check.pop(0)
        if (bx, by) in moveset: # already checked this one
            continue
        if bx > 0 and map[by][bx] == map[by][bx-1]: # registring left half for checks
            check.append((bx-1, by))
        if bx < w-1 and map[by][bx] == map[by][bx+1]: # registring right half for checks
            check.append((bx+1, by))
        if bx+dx < 0 or bx+dx >= w or by+dy < 0 or by+dy >= h: # cannot move
            return False
        if map[by+dy][bx+dx] == -1: # cannot move
            return False
        if map[by+dy][bx+dx] == 0: # safe to move
            move.append((bx, by)) # register for moving, we dont want to check this one again
            moveset.add((bx, by))
            continue
        # need to move further boxes
        move.append((bx, by)) # register for moving, we dont want to check this one again
        moveset.add((bx, by))
        check.append((bx+dx, by+dy)) # check box in fromt
    # actually move the boxes
    for (bx, by) in move[::-1]: # boxes added last need to move first
        map[by+dy][bx+dx], map[by][bx] = map[by][bx], map[by+dy][bx+dx]
    # now move robot
    x, y = x + dx, y + dy
    return True # successfully moved all boxes
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
        if map[my][mx] > 0:
            if mx > 0 and map[my][mx] == map[my][mx-1]:
                continue # we only measure the left edges
            score += my * 100 + mx

print(score)
