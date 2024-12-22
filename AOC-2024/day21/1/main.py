with open('input.txt') as infile:
    codes = infile.read().strip().split('\n')

DOOR = 0
ROBOT = 1
DOOR_BUTTONS = { '0': (1, 3), '1': (0, 2), '2': (1, 2), '3': (2, 2), '4': (0, 1), '5': (1, 1), '6': (2, 1), '7': (0, 0), '8': (1, 0), '9': (2, 0), 'A': (2, 3), 'X': (0, 3) }
ROBOT_BUTTONS = { '^': (1, 0), '<': (0, 1), 'v': (1, 1), '>': (2, 1), 'A': (2, 0), 'X': (0, 0) }

def gen_moves(x, y, tx, ty, level):
    console = DOOR if level == 0 else ROBOT

    dx, dy = tx-x, ty-y
    h = '>' if dx > 0 else '<'
    v = 'v' if dy > 0 else '^'

    # get inaccessible spot (X)
    if console == DOOR:
        px, py = DOOR_BUTTONS['X']
    else:
        px, py = ROBOT_BUTTONS['X']
    # potential collision with X?
    if x == px and ty == py: # move x away first
        return h * abs(dx) + v * abs(dy) + 'A'
    if y == py and tx == px: # move y away first
        return v * abs(dy) + h * abs(dx) + 'A'

    if level == 3:
        # arbitrarily move since its the outermost layer
        return h * abs(dx) + v * abs(dy) + 'A'

    # moving horizontally first
    i1 = h * abs(dx) + v * abs(dy) + 'A'
    o1 = generate_inputs(i1, level+1)
    lv = level+1
    while lv < 3:
        o1 = generate_inputs(o1, lv+1)
        lv += 1
    # moving vertically first
    i2 = v * abs(dy) + h * abs(dx) + 'A'
    o2 = generate_inputs(i2, level+1)
    lv = level+1
    while lv < 3:
        o2 = generate_inputs(o2, lv+1)
        lv += 1
    if len(o1) <= len(o2):
        return i1
    else:
        return i2

def generate_inputs(code, level):
    assert code[-1] == 'A'
    console = DOOR if level == 0 else ROBOT
    if console == DOOR:
        x, y = DOOR_BUTTONS['A']
    else:
        x, y = ROBOT_BUTTONS['A']
    inputs = ''
    for c in code:
        if console == DOOR:
            tx, ty = DOOR_BUTTONS[c]
        else:
            tx, ty = ROBOT_BUTTONS[c]
        inputs += gen_moves(x, y, tx, ty, level)
        x, y = tx, ty
    return inputs

def simulate(inputs):
    pad0 = 'A'
    l1, pad1 = 'A', 'A'
    l2, pad2 = 'A', 'A'
    lc = ''
    # print(pad0, pad1, pad2)
    for c in inputs:
        o2 = pad2
        x, y = ROBOT_BUTTONS[pad2]
        if c == '^':
            pad2 = [b for b in ROBOT_BUTTONS if ROBOT_BUTTONS[b] == (x, y-1)][0]
        if c == 'v':
            pad2 = [b for b in ROBOT_BUTTONS if ROBOT_BUTTONS[b] == (x, y+1)][0]
        if c == '<':
            pad2 = [b for b in ROBOT_BUTTONS if ROBOT_BUTTONS[b] == (x-1, y)][0]
        if c == '>':
            pad2 = [b for b in ROBOT_BUTTONS if ROBOT_BUTTONS[b] == (x+1, y)][0]
        if c == 'A':
            if l2 == pad2 and lc != c:
                print('pad 2 did not move')
            o1 = pad1
            x, y = ROBOT_BUTTONS[pad1]
            if pad2 == '^':
                pad1 = [b for b in ROBOT_BUTTONS if ROBOT_BUTTONS[b] == (x, y-1)][0]
            if pad2 == 'v':
                pad1 = [b for b in ROBOT_BUTTONS if ROBOT_BUTTONS[b] == (x, y+1)][0]
            if pad2 == '<':
                pad1 = [b for b in ROBOT_BUTTONS if ROBOT_BUTTONS[b] == (x-1, y)][0]
            if pad2 == '>':
                pad1 = [b for b in ROBOT_BUTTONS if ROBOT_BUTTONS[b] == (x+1, y)][0]
            if pad2 == 'A':
                if l1 == pad1 and lc != c:
                    print('pad 1 did not move')
                x, y = DOOR_BUTTONS[pad0]
                if pad1 == '^':
                    pad0 = [b for b in DOOR_BUTTONS if DOOR_BUTTONS[b] == (x, y-1)][0]
                if pad1 == 'v':
                    pad0 = [b for b in DOOR_BUTTONS if DOOR_BUTTONS[b] == (x, y+1)][0]
                if pad1 == '<':
                    pad0 = [b for b in DOOR_BUTTONS if DOOR_BUTTONS[b] == (x-1, y)][0]
                if pad1 == '>':
                    pad0 = [b for b in DOOR_BUTTONS if DOOR_BUTTONS[b] == (x+1, y)][0]
                if pad1 == 'A':
                    print(f'inputting: {pad0}')
            l1 = o1
        l2 = o2
        lc = c
        # print(pad0, pad1, pad2, 'input:', c)

def main(codes):
    total = 0

    for i, code in enumerate(codes):
        print(f'{i}. {code}')
        i0 = generate_inputs(code, 0)
        print(f'   ({len(i0):4}) {i0}')
        i1 = generate_inputs(i0, 1)
        print(f'   ({len(i1):4}) {i1}')
        i2 = generate_inputs(i1, 2)
        print(f'   ({len(i2):4}) {i2}')
        l = len(i2)
        c = int(code[:-1])
        total += c*l
        print(f'complexity = {c}x{l} = {c*l}')
        simulate(i2)
        print()
    print(f'{total=}')

main(codes)
