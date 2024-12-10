with open('input.txt') as infile:
    raw_data = infile.read().strip()

map = [[int(h) for h in row] for row in raw_data.split('\n')]
w, h = len(map[0]), len(map)

stack = []
trails = []

for y in range(h):
    for x in range(w):
        if map[y][x] == 0:
            stack.append((x, y, len(trails)))
            trails.append(set())

while len(stack) > 0:
    x, y, index = stack.pop()
    z = map[y][x]
    if z == 9:
        trails[index].add((x, y))
        continue
    if x > 0 and map[y][x-1] == z + 1:
        stack.append((x-1, y, index))
    if x < w-1 and map[y][x+1] == z + 1:
        stack.append((x+1, y, index))
    if y > 0 and map[y-1][x] == z + 1:
        stack.append((x, y-1, index))
    if y < h-1 and map[y+1][x] == z + 1:
        stack.append((x, y+1, index))

counts = [len(t) for t in trails]
print(counts)
print(sum(counts))
