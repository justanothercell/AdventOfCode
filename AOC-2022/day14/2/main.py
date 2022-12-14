with open('input.txt') as infile:
    paths = infile.readlines()

# total: 93
# paths = [
#     '498,4 -> 498,6 -> 496,6',
#     '503,4 -> 502,4 -> 502,9 -> 494,9',
# ]

min_bounds = (500, 0)
max_bounds = (500, 0)

for path in paths:
    segments = path.split(' -> ')
    for segment in segments:
        x, y = [int(c) for c in segment.split(',')]
        min_bounds = min(x, min_bounds[0]), min(y, min_bounds[1])
        max_bounds = max(x, max_bounds[0]), max(y, max_bounds[1])

min_bounds = 500 - max_bounds[1] - 3, 0
max_bounds = 500 + max_bounds[1] + 3, max_bounds[1] + 1


size = max_bounds[0] - min_bounds[0] + 3, max_bounds[1] - min_bounds[1] + 3


print(f'min: {min_bounds}')
print(f'max: {max_bounds}')
print(f'size: {size}')
print()

map = [['.' for y in range(size[1])] for x in range(size[0])]


def print_map():
    for y in range(size[1]):
        for x in range(size[0]):
            print(map[x][y], end='')
        print()
    print()


for path in paths:
    segments = path.split(' -> ')
    p_pos = None
    for segment in segments:
        x, y = [int(c) for c in segment.split(',')]
        x -= min_bounds[0] - 1
        y -= min_bounds[1] - 1
        if p_pos is not None:
            if p_pos[0] != x:
                for dx in range(min(p_pos[0], x), max(p_pos[0], x) + 1):
                    map[dx][y] = '#'
            if p_pos[1] != y:
                for dy in range(min(p_pos[1], y), max(p_pos[1], y) + 1):
                    map[x][dy] = '#'
        p_pos = x, y


for x in range(size[0]):
    map[x][size[1]-1] = '#'


print_map()

total = 0


def drop_sand():
    x = 500 - min_bounds[0] + 1
    y = 1
    if map[x][y] != '.':
        return True
    while True:
        if y >= size[1] - 1:
            return True
        if map[x][y+1] == '.':
            y += 1
            continue
        if x > 0 and map[x-1][y+1] == '.':
            x -= 1
            y += 1
            continue
        if x <= size[0] - 2 and map[x+1][y+1] == '.':
            x += 1
            y += 1
            continue
        map[x][y] = 'c'
        return False


while not drop_sand():
    total += 1

print_map()
print(f'total: {total}')
# total: 22499