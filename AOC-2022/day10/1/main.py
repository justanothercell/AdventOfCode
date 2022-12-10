with open('input.txt') as infile:
    instructions = [row.strip() for row in infile.readlines()]

# test_input.txt
# strengths: [420, 1140, 1800, 2940, 2880, 3960]
# accumulated: 13140

# instructions = [
#     'noop',
#     'addx 3',
#     'addx -5',
# ]

# cycle   instr   reg_x (during)   reg_x (after)
#     1    noop                1               1
#     2  addx 3                1               1
#     3  addx 3                1               4
#     4  addx -5               4               4
#     5  addx -5               4              -1

clock = 0

reg_x = 1

log_markers = [20, 60, 100, 140, 180, 220]
strengths = []

for instr in instructions:
    p_x = reg_x
    if instr.strip() == 'noop':
        clock += 1
    elif instr.strip().startswith('addx'):
        a = int(instr.strip()[5:])
        reg_x += a
        clock += 2
    if clock >= log_markers[0]:
        m = log_markers.pop(0)
        strengths.append(m * p_x)
        if len(log_markers) == 0:
            break

print(f'strengths: {strengths}')  # strengths: [240, 240, 3900, 3080, 3060, 4620]
print(f'accumulated: {sum(strengths)}')  # accumulated: 15140

