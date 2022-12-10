with open('input.txt') as infile:
    instructions = [row.strip() for row in infile.readlines()]

# test_input output
# ##..##..##..##..##..##..##..##..##..##..
# ###...###...###...###...###...###...###.
# ####....####....####....####....####....
# #####.....#####.....#####.....#####.....
# ######......######......######......####
# #######.......#######.......#######.....

clock = 0


reg_x = 1

crt = [['.'] * 40 for _ in range(6)]


def print_crt():
    crt_x = clock % 40
    crt_y = clock // 40
    if abs(reg_x - crt_x) <= 1:
        crt[crt_y][crt_x] = '#'


for instr in instructions:
    p_x = reg_x
    if instr.strip() == 'noop':
        print_crt()
        clock += 1
    elif instr.strip().startswith('addx'):
        a = int(instr.strip()[5:])
        print_crt()
        clock += 1
        print_crt()
        clock += 1
        reg_x += a
    if clock > 240:
        break

print('output:')
for y in range(6):
    for x in range(40):
        print(crt[y][x], end='')
    print()

# ###..###....##..##..####..##...##..###..
# #..#.#..#....#.#..#....#.#..#.#..#.#..#.
# ###..#..#....#.#..#...#..#....#..#.#..#.
# #..#.###.....#.####..#...#.##.####.###..
# #..#.#....#..#.#..#.#....#..#.#..#.#....
# ###..#.....##..#..#.####..###.#..#.#....

# BPJAZGAP