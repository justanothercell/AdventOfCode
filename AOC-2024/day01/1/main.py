left = []
right = []

with open('input.txt') as infile:
    lines = infile.readlines()
    for line in lines:
        line = line.strip()
        if len(line) > 0:
            l, r = line.split()
            left.append(int(l))
            right.append(int(r))

left.sort()
right.sort()

diff = 0

for l, r in zip(left, right):
    diff += abs(r - l)

print(diff)
