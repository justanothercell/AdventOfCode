with open('input.txt') as infile:
    tiles = [l.rstrip() for l in infile.readlines()]

# row: 6
# colum: 8
# facing: 0
# password: 6032
# *tiles, _, movements = [
#     '        ...#    ',
#     '        .#..    ',
#     '        #...    ',
#     '        ....    ',
#     '...#.......#    ',
#     '........#...    ',
#     '..#....#....    ',
#     '..........#.    ',
#     '        ...#....',
#     '        .....#..',
#     '        .#......',
#     '        ......#.',
#     '',
#     '10R5L5R10L4R5L5',
# ]

x_ranges = []
for y in range(len(tiles)):
    mi = None
    ma = len(tiles[y]) - 1
    for x in range(len(tiles[y])):
        if tiles[y][x] != ' ' and mi is None:
            mi = x
        if mi is not None and tiles[y][x] == ' ':
            ma = x - 1
            break
    x_ranges.append((mi, ma))

y_ranges = []
for x in range(len(tiles[0])):
    mi = None
    ma = len(tiles) - 1
    for y in range(len(tiles)):
        if tiles[y][x] != ' ' and mi is None:
            mi = y
        if mi is not None and tiles[y][x] == ' ':
            ma = y - 1
            break
    y_ranges.append((mi, ma))

x_pos = x_ranges[0][0]
y_pos = 0
facing = 0

for instr in re.findall(r'(\d+|[RL])', movements):
    try:
        for _ in range(int(instr)):
            next_x = x_pos
            next_y = y_pos
            match facing:
                case 0:
                    next_x += 1
                    if next_x > x_ranges[y_pos][1]:
                        next_x = x_ranges[y_pos][0]
                case 1:
                    next_y += 1
                    if next_y > y_ranges[x_pos][1]:
                        next_y = y_ranges[x_pos][0]
                case 2:
                    next_x -= 1
                    if next_x < x_ranges[y_pos][0]:
                        next_x = x_ranges[y_pos][1]
                case 3:
                    next_y -= 1
                    if next_y < y_ranges[x_pos][0]:
                        next_y = y_ranges[x_pos][1]
            if tiles[next_y][next_x] == '.':
                x_pos = next_x
                y_pos = next_y
            else:
                # print(facing, instr, 'bonk!')
                break
        #     print(x_pos, y_pos)
        # else:
        #     print(facing, instr, 'swoosh')
        # for y in range(len(tiles)):
        #     for x in range(len(tiles[y])):
        #         if (x, y) != (x_pos, y_pos):
        #             print(tiles[y][x], end='')
        #         else:
        #             print('X', end='')
        #     print()
        # print()
    except ValueError:
        match instr:
            case "L":
                facing = (facing + 3) % 4
            case "R":
                facing = (facing + 1) % 4

print(f'x_pos: {x_pos + 1}')
print(f'y_pos: {y_pos + 1}')
print(f'facing: {facing}')
print(f'password: {(y_pos + 1) * 1000 + (x_pos + 1) * 4 + facing}')
# x_pos: 86
# y_pos: 73
# facing: 2
# password: 73346
