with open('input.txt') as infile:
    data = infile.readlines()
    if len(data[-1]) == 0:
        data.pop()

xmases = 0

w = len(data[0])
h = len(data)

def xmas(x, y, dx, dy):
    global xmases
    for c in 'XMAS':
        if x < 0 or y < 0 or x >= w or y >= h:
            return
        if data[y][x] != c:
            return
        x += dx
        y += dy
    xmases += 1

for x in range(w):
    for y in range(h):
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]:
            xmas(x, y, dx, dy)

print(xmases)
