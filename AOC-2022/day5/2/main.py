with open('input.txt') as infile:
    logistics_file = infile.readlines()

split_index = logistics_file.index('\n')

schematic = logistics_file[:split_index-1]  # -1 removes the 1 2 3 4 5... index line
instructions = logistics_file[split_index+1:]  # +1 removes empty line

stacks_count = int(len(schematic[0]) / 4)

stacks = [[] for _ in range(stacks_count)]

for row in schematic[::-1]:
    for i in range(stacks_count):
        print(row[i * 4 + 1], end=' ')
        crate = row[i * 4 + 1]
        if crate != ' ':
            stacks[i].append(crate)
    print()

print()

for stack in stacks:
    print(stack)

print()

for line in instructions:
    _, amount, _, source, _, dest = line.strip().split(' ')
    amount, source, dest = int(amount), int(source) - 1, int(dest) - 1
    moving_crates = []
    for _ in range(amount):
        if len(stacks[source]) > 0:
            moving_crates.append(stacks[source].pop())
    [stacks[dest].append(crate) for crate in moving_crates[::-1]]

for stack in stacks:
    print(stack)

print()

top = [stack[-1] for stack in stacks]

print(f'top row: {top}')  # top row: ['P', 'R', 'T', 'T', 'G', 'R', 'F', 'P', 'B']
print(f'=> {"".join(top)}')  # => PRTTGRFPB
