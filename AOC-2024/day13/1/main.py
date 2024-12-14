import re

pattern = r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)'

with open('input.txt') as infile:
    raw_data = infile.read().strip().split('\n\n')

total_cost = 0
total_won = 0

for raw_machine in raw_data:
    match = re.match(pattern, raw_machine)
    ax, ay, bx, by, px, py = [int(n) for n in match.groups()]

    cost = 1_000_000
    presses = None

    for i in range(100):
        if px - ax * i < 0 or py - ay * i < 0: # we overshot
            continue
        if (px - ax * i) % bx != 0: # can't express rest of x in terms of b
            continue
        if (py - ay * i) % by != 0: # can't express rest of y in terms of b
            continue
        if (px - ax * i) // bx != (py - ay * i) // by: # x and y of b don't match up
            continue
        j = (px - ax * i) // bx
        if i + j * 3 < cost:
            cost = i*3 + j
            presses = (i, j)
    if presses is not None:
        total_cost += cost
        total_won += 1
        print(f'got prize with {presses[0]}xA and {presses[1]}xB at a cost of {cost}')
    else:
        print('could not get prize')
print()
print(f'{total_cost=}\t{total_won=}')
