with open('input.txt') as infile:
    data = infile.readlines()
    if len(data[-1]) == 0:
        data.pop()

xmases = 0

w = len(data[0])
h = len(data)

def xmas(x, y):
    global xmases
    if data[y][x] != 'A':
        return
    found = False
    if data[y-1][x-1] == 'M' and data[y+1][x+1] == 'S':
        found = True
    if data[y-1][x-1] == 'S' and data[y+1][x+1] == 'M':
        found = True
    if not found:
        return
    found = False
    if data[y+1][x-1] == 'M' and data[y-1][x+1] == 'S':
        found = True
    if data[y+1][x-1] == 'S' and data[y-1][x+1] == 'M':
        found = True
    if not found:
        return
    xmases += 1

for x in range(1, w-1):
    for y in range(1, h-1):
        xmas(x, y)

print(xmases)
