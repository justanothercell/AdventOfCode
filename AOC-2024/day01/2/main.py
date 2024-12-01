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

similarity = 0

while len(left) > 0:
    i = left.pop()
    n = 1
    k = 0
    while len(left) > 0 and left[-1] == i:
        left.pop()
        n += 1
    while len(right) > 0 and right[-1] > i:
        right.pop()
    while len(right) > 0 and right[-1] == i:
        right.pop()
        k += 1
    similarity += i * n * k

print(similarity)
