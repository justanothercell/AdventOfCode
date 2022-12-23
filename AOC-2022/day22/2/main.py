import re

with open('input.txt') as infile:
    *tiles, _, movements = [l.rstrip() for l in infile.readlines()]
w = max(len(r) for r in tiles)
for i in range(len(tiles)):
    tiles[i] = tiles[i].ljust(w)
# face: C
# raw x_pos: 2
# raw y_pos: 0
# x_pos: 7
# y_pos: 5
# facing: 3
# password: 5031
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


class Face:
    def __init__(self, name, tiles, global_offset):
        self.name = name
        self.tiles = tiles
        self.global_offset = global_offset
        self.trans = {}


# sadly these faces are manually built and not connected algorithmically due to the different layouts of cubes
# it would probably be possible tho, just not a justifiable amount of work

# example:
#   A
# BCD
#   EF
# a = Face("A", [t[8:12] for t in tiles[0:4]], (8, 0))
# b = Face("B", [t[0:4] for t in tiles[4:8]], (0, 4))
# c = Face("C", [t[4:8] for t in tiles[4:8]], (4, 4))
# d = Face("D", [t[8:12] for t in tiles[4:8]], (8, 4))
# e = Face("E", [t[8:12] for t in tiles[8:12]], (8, 8))
# f = Face("F", [t[12:16] for t in tiles[8:12]], (12, 8))
# a.trans = {'n': lambda x, y: (s-x, 0, 1, b), 's': lambda x, y: (x, 0, 1, d), 'w': lambda x, y: (y, 0, 1, c), 'e': lambda x, y: (s, s-y, 2, f)}
# b.trans = {'n': lambda x, y: (s-x, 0, 1, a), 's': lambda x, y: (s-x, 0, s, e), 'w': lambda x, y: (s-y, 2, f), 'e': lambda x, y: (0, y, 0, c)}
# c.trans = {'n': lambda x, y: (0, x, 0, a), 's': lambda x, y: (0, s-x, 0, e), 'w': lambda x, y: (s, y, 2, b), 'e': lambda x, y: (0, y, 0, d)}
# d.trans = {'n': lambda x, y: (x, s, s, a), 's': lambda x, y: (x, 0, 1, e), 'w': lambda x, y: (s, y, 2, c), 'e': lambda x, y: (s-y, 0, 1, f)}
# e.trans = {'n': lambda x, y: (x, s, s, d), 's': lambda x, y: (s-x, s, s, b), 'w': lambda x, y: (s-y, s, s, c), 'e': lambda x, y: (0, y, 0, f)}
# f.trans = {'n': lambda x, y: (s, s-x, 2, d), 's': lambda x, y: (0, s-x, 0, b), 'w': lambda x, y: (s, y, 2, e), 'e': lambda x, y: (0, s-y, 0, a)}
# s = 3

# Note: I figured out all the transitions of the test data by thinking.
# To not descend further into madness I used a paper cube map for the real data.


# real data:
#  AB
#  C
# DE
# F
a = Face("A", [t[50:100] for t in tiles[0:50]], (50, 0))
b = Face("B", [t[100:150] for t in tiles[0:50]], (100, 0))
c = Face("C", [t[50:100] for t in tiles[50:100]], (50, 50))
d = Face("D", [t[0:50] for t in tiles[100:150]], (0, 100))
e = Face("E", [t[50:100] for t in tiles[100:150]], (50, 100))
f = Face("F", [t[0:50] for t in tiles[150:200]], (0, 150))
a.trans = {'n': lambda x, y: (0, x, 0, f), 's': lambda x, y: (x, 0, 1, c), 'w': lambda x, y: (0, s-y, 0, d), 'e': lambda x, y: (0, y, 0, b)}
b.trans = {'n': lambda x, y: (x, s, 3, f), 's': lambda x, y: (s, x, 2, c), 'w': lambda x, y: (s, y, 2, a), 'e': lambda x, y: (s, s-y, 2, e)}
c.trans = {'n': lambda x, y: (x, s, 3, a), 's': lambda x, y: (x, 0, 1, e), 'w': lambda x, y: (y, 0, 1, d), 'e': lambda x, y: (y, s, 3, b)}
d.trans = {'n': lambda x, y: (0, x, 0, c), 's': lambda x, y: (x, 0, 1, f), 'w': lambda x, y: (0, s-y, 0, a), 'e': lambda x, y: (0, y, 0, e)}
e.trans = {'n': lambda x, y: (x, s, 3, c), 's': lambda x, y: (s, x, 2, f), 'w': lambda x, y: (s, y, 2, d), 'e': lambda x, y: (s, s-y, 2, b)}
f.trans = {'n': lambda x, y: (x, s, 3, d), 's': lambda x, y: (x, 0, 1, b), 'w': lambda x, y: (y, 0, 1, a), 'e': lambda x, y: (y, s, 3, e)}
s = 49
# debugging: put the transitions int a string called 'd' and replace away all the 'lambda' and "'e'" to only be left
# with abcdef from transition destinations
# >>> sum([x == 'a' for x in d])
# 4
# >>> sum([x == 'b' for x in d])
# 4
# >>> sum([x == 'c' for x in d])
# 4
# >>> sum([x == 'd' for x in d])
# 4
# >>> sum([x == 'e' for x in d])
# 4
# >>> sum([x == 'f' for x in d])
# 4
# => 4 transitions to each face, looks good!
#    Note: before that there was an "a" transition missing, found it with this method.
#          You have no idea how blind to letters you become after staring at this for that long
#          trying to figure out the right transitions...
# Bugs manually found by looking at transition movement:
# f to a (n): new facing should be 1 not 0
# e to f (s): new y coord should be x not y; y was always 49
# d to e (e): new x should be 0 not 49
# d to e (e): facing should stay 0 not 2

x_pos = 0
y_pos = 0
facing = 0

face = a

for instr in re.findall(r'(\d+|[RL])', movements):
    try:
        for _ in range(int(instr)):
            next_x = x_pos
            next_y = y_pos
            next_d = facing
            next_f = face
            match facing:
                case 0:
                    next_x += 1
                    if next_x > s:
                        next_x, next_y, next_d, next_f = face.trans['e'](x_pos, y_pos)
                        print(f'transitioned from face {face.name} {x_pos, y_pos} to {next_f.name} {next_x, next_y} turning {facing} to {next_d}')
                case 1:
                    next_y += 1
                    if next_y > s:
                        next_x, next_y, next_d, next_f = face.trans['s'](x_pos, y_pos)
                        print(f'transitioned from face {face.name} {x_pos, y_pos} to {next_f.name} {next_x, next_y} turning {facing} to {next_d}')
                case 2:
                    next_x -= 1
                    if next_x < 0:
                        next_x, next_y, next_d, next_f = face.trans['w'](x_pos, y_pos)
                        print(f'transitioned from face {face.name} {x_pos, y_pos} to {next_f.name} {next_x, next_y} turning {facing} to {next_d}')
                case 3:
                    next_y -= 1
                    if next_y < 0:
                        next_x, next_y, next_d, next_f = face.trans['n'](x_pos, y_pos)
                        print(f'transitioned from face {face.name} {x_pos, y_pos} to {next_f.name} {next_x, next_y} turning {facing} to {next_d}')
            if next_f.tiles[next_y][next_x] == '.':
                x_pos = next_x
                y_pos = next_y
                facing = next_d
                face = next_f
            else:
                break
        x_g, y_g = x_pos + face.global_offset[0], y_pos + face.global_offset[0]
        for y in range(max(0, y_g - 7), min(y_g + 7, len(tiles))):
            for x in range(max(0, x_g - 7), min(x_g + 7, len(tiles[y]))):
                if (x, y) != (x_g, y_g):
                    print(tiles[y][x], end='')
                else:
                    print('X', end='')
            print()
        print()
    except ValueError:
        match instr:
            case "L":
                facing = (facing + 3) % 4
            case "R":
                facing = (facing + 1) % 4

print(f'face: {face.name}')
print(f'raw x_pos: {x_pos}')
print(f'raw y_pos: {y_pos}')
x_g, y_g = x_pos + face.global_offset[0], y_pos + face.global_offset[0]
print(f'x_pos: {x_g + 1}')
print(f'y_pos: {y_g + 1}')
print(f'facing: {facing}')
print(f'password: {(y_g + 1) * 1000 + (x_g + 1) * 4 + facing}')
# face: E
# raw x_pos: 47
# raw y_pos: 5
# x_pos: 98
# y_pos: 56
# facing: 0
# password: 56392
#
# 96353 -> didn't specify wrongness
# 135552 -> too high
# 82234 -> too low
