import os
os.system("")

with open('input.txt') as infile:
    tiles_in = [l.strip() for l in infile.readlines()]

# width: 12
# height: 10
# empty: 110
# tiles_in = [
#     '....#..',
#     '..###.#',
#     '#...#.#',
#     '.#...##',
#     '#.###..',
#     '##.#.##',
#     '.#..#..',
# ]

in_w, in_h = len(tiles_in[0]), len(tiles_in)
s_w = in_w
s_h = in_h
w, h = in_w + s_w * 2, in_h + s_h * 2


class Elf:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.move = -1


elves = []
tiles = []
for y in range(w):
    row = []
    for x in range(h):
        if s_w <= x < w - s_w and s_h <= y < h - s_h:
            if tiles_in[y - s_h][x - s_w] == '#':
                row.append(1)
                elves.append(Elf(x, y))
            else:
                row.append(0)
        else:
            row.append(0)
    tiles.append(row)


def print_tiles(moves=None):
    for y in range(h):
        for x in range(w):
            if (x + y) % 2 == 0:
                print('\x1b[48;5;239m', end='')
            else:
                print('\x1b[48;5;241m', end='')
            if tiles[y][x] != 0:
                print(' # ', end='')
            elif moves is not None:
                if moves[y][x] == 0:
                    print('   ', end='')
                elif moves[y][x] == 1:
                    print(' * ', end='')
                else:
                    print(' x ', end='')
            else:
                print('   ', end='')
        print('\x1b[0m')
    print()


# print_tiles()

tick_count = 0
while tick_count < 10:
    moves_tiles = [[0 for _ in range(w)] for _ in range(h)]
    for elf in elves:
        if tiles[elf.y - 1][elf.x - 1] + tiles[elf.y - 1][elf.x] + tiles[elf.y - 1][elf.x + 1] + \
                tiles[elf.y][elf.x - 1] + tiles[elf.y][elf.x + 1] + \
                tiles[elf.y + 1][elf.x - 1] + tiles[elf.y + 1][elf.x] + tiles[elf.y + 1][elf.x + 1] == 0:
            elf.move = -1
        else:
            for i in range(4):
                if (tick_count + 3) % 4 == 3-i:        # N
                    if tiles[elf.y - 1][elf.x - 1] + tiles[elf.y - 1][elf.x] + tiles[elf.y - 1][elf.x + 1] == 0:
                        moves_tiles[elf.y - 1][elf.x] += 1
                        elf.move = 3
                        break
                if (tick_count + 2) % 4 == 3-i:  # S
                    if tiles[elf.y + 1][elf.x - 1] + tiles[elf.y + 1][elf.x] + tiles[elf.y + 1][elf.x + 1] == 0:
                        moves_tiles[elf.y + 1][elf.x] += 1
                        elf.move = 1
                        break
                if (tick_count + 1) % 4 == 3-i:  # W
                    if tiles[elf.y - 1][elf.x - 1] + tiles[elf.y][elf.x - 1] + tiles[elf.y + 1][elf.x - 1] == 0:
                        moves_tiles[elf.y][elf.x - 1] += 1
                        elf.move = 2
                        break
                if tick_count % 4 == 3-i:  # E
                    if tiles[elf.y - 1][elf.x + 1] + tiles[elf.y][elf.x + 1] + tiles[elf.y + 1][elf.x + 1] == 0:
                        moves_tiles[elf.y][elf.x + 1] += 1
                        elf.move = 0
                        break
            else:
                elf.move = -1
    # print_tiles(moves=moves_tiles)
    for elf in elves:
        p = elf.x, elf.y
        if elf.move == 0:  # E
            if moves_tiles[elf.y][elf.x + 1] == 1:
                tiles[elf.y][elf.x] = 0
                tiles[elf.y][elf.x + 1] = 1
                elf.x += 1
        elif elf.move == 1:  # S
            if moves_tiles[elf.y + 1][elf.x] == 1:
                tiles[elf.y][elf.x] = 0
                tiles[elf.y + 1][elf.x] = 1
                elf.y += 1
        elif elf.move == 2:  # W
            if moves_tiles[elf.y][elf.x - 1] == 1:
                tiles[elf.y][elf.x] = 0
                tiles[elf.y][elf.x - 1] = 1
                elf.x -= 1
        elif elf.move == 3:  # N
            if moves_tiles[elf.y - 1][elf.x] == 1:
                tiles[elf.y][elf.x] = 0
                tiles[elf.y - 1][elf.x] = 1
                elf.y -= 1
    # print_tiles()
    # print('======')
    # print()
    tick_count += 1
# print_tiles()
min_bounds = w, h
max_bounds = 0, 0
for elf in elves:
    min_bounds = min(min_bounds[0], elf.x), min(min_bounds[1], elf.y)
    max_bounds = max(max_bounds[0], elf.x), max(max_bounds[1], elf.y)
print(min_bounds, max_bounds)
width = max_bounds[0] - min_bounds[0] + 1
height = max_bounds[1] - min_bounds[1] + 1
empty = width * height - len(elves)
print(f'width: {width}')
print(f'height: {height}')
print(f'empty: {empty}')
# width: 82
# height: 81
# empty: 4052
